import time
import os
from dilithium.dilithium import Dilithium2, Dilithium3, Dilithium5
from dilithium.modules import Module
from kyber_py.kyber import AnaDil_Kyber1, AnaDil_Kyber2, AnaDil_Kyber3
from sympy import Poly

import KyberPKE.kyberPKE
from transfer.U_to_U import u_to_u_int, u_backto_u_int

q = 3329
dili = Dilithium5
kyber = AnaDil_Kyber3
gamma_1 = dili.gamma_1

REPEAT = 15  # 测试重复次数


def matrix_to_coeff_list(matrix: "Module.Matrix"):
    """将 l×1 的 Module.Matrix 转成嵌套整数列表"""
    coeff_list = []
    for row in matrix.rows:
        poly = row[0]
        coeffs = poly.coeffs[:]
        coeffs += [0] * (matrix.parent.ring.n - len(coeffs))
        coeff_list.append(coeffs)
    return coeff_list


def keygen():
    seed = os.urandom(32)
    return dili.keygen(seed)


def ana_keygen():
    return KyberPKE.kyberPKE.keygen(kyber)


def sign(message: bytes, sk: bytes):
    return dili.sign_with_input(sk, message)


def verify(message: bytes, signature: bytes, pk: bytes):
    return dili.verify(pk, message, signature)


def ana_sign(plaintext, apk, message: bytes, sk: bytes):
    a = round((q - 1) / 2)
    while True:
        c_list = KyberPKE.kyberPKE.enc(apk, plaintext, kyber)
        c_list_new = [
            [u_to_u_int(x, 2 * a, 2 * gamma_1 - 2) - gamma_1 + 1 for x in poly]
            for poly in c_list
        ]
        sig_result = dili.ana_sign(sk, message, c_list_new)  # 返回 (flag, sig_bytes)
        if sig_result == 0:  # flag = 0 表示失败
            continue
        else:
            return c_list_new, sig_result[-1]


def dec(signature: bytes, ask):
    c_list_new, sig = signature
    c_tilde, z, h = dili._unpack_sig(sig)
    zz = matrix_to_coeff_list(z)
    a = round((q - 1) / 2)
    zz_transformed = [
                         [u_backto_u_int(coef + gamma_1 - 1, 2 * a, 2 * gamma_1 - 2) for coef in row]
                         for row in zz
                     ][:len(c_list_new)]
    plain = KyberPKE.kyberPKE.dec(ask, zz_transformed, kyber)
    return plain


def size_kb(x: bytes):
    return len(x) / 1024


def measure_time(func, *args, repeat=REPEAT):
    """手动统计平均时间"""
    times = []
    result = None
    for _ in range(repeat):
        start = time.perf_counter()
        result = func(*args)
        times.append(time.perf_counter() - start)
    avg_time = sum(times) / repeat
    print(f"[Timing] {func.__name__}: {avg_time:.6f}s (avg over {repeat} runs)")
    return result, avg_time


def main():
    print("=== Dilithium & Anamorphic-Dilithium Timing Test ===")
    message = b"Hello Dilithium"

    # =========================
    # KeyGen
    # =========================
    (pk, sk), t_keygen = measure_time(keygen)
    (apk, ask), t_ana_keygen = measure_time(ana_keygen)

    # =========================
    # Standard Sign
    # =========================
    signature, t_sign = measure_time(sign, message, sk)
    print("Standard verify:", measure_time(verify, message, signature, pk)[0])

    # =========================
    # Anamorphic Sign
    # =========================
    plaintext = os.urandom(32)
    print("Plaintext:\n", plaintext)

    ana_signature, t_ana_sign = measure_time(ana_sign, plaintext, apk, message, sk)
    print("AnaSignature Done")

    decrypted_plaintext, t_dec = measure_time(dec, ana_signature, ask)
    print("Decrypted Plaintext:\n", decrypted_plaintext)

    print("Anamorphic verify:", measure_time(verify, message, ana_signature[-1], pk)[0])

    # =========================
    # Sizes
    # =========================
    print("\n===== Sizes (KB) =====")
    print(f"pk size:  {size_kb(pk):.4f} KB")
    print(f"sk size:  {size_kb(sk):.4f} KB")
    print(f"apk size: {size_kb(apk):.4f} KB")  # <-- Anamorphic public key
    print(f"ask size: {size_kb(ask):.4f} KB")  # <-- Anamorphic secret key
    print(f"signature size: {size_kb(signature):.4f} KB")

    # =========================
    # Timing Summary
    # =========================
    print("\n===== Average Timing (s) =====")
    print(f"KeyGen:          {t_keygen:.6f}")
    print(f"Ana KeyGen:      {t_ana_keygen:.6f}")
    print(f"Sign:            {t_sign:.6f}")
    print(f"Ana Sign:        {t_ana_sign:.6f}")
    print(f"Decrypt:         {t_dec:.6f}")


if __name__ == "__main__":
    main()
