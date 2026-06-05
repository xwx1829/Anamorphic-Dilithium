import os
import time
import kyber_py
from kyber_py.kyber import AnaDil_Kyber1, AnaDil_Kyber2, AnaDil_Kyber3

print(kyber_py.__file__)


# =========================
# PKE KeyGen
# =========================
def keygen(kyber):
    pk, sk = kyber._cpapke_keygen()
    return pk, sk


# =========================
# PKE Enc
# =========================
def enc(pk, m, kyber):
    coins = os.urandom(32)
    c = kyber._cpapke_enc_list(pk, m, coins)
    return c


# =========================
# PKE Dec
# =========================
def dec(sk, c, kyber):
    m = kyber._cpapke_dec_list(sk, c)
    return m


# =========================
# main (correctness test)
# =========================
if __name__ == "__main__":

    kyber = AnaDil_Kyber1

    print("=== Kyber PKE Correctness Test ===")
    print()

    # =========================
    # KeyGen
    # =========================
    print("KeyGen...")
    pk, sk = keygen(kyber)
    print("pk len =", len(pk))
    print("sk len =", len(sk))
    print()

    # =========================
    # message
    # =========================
    m = os.urandom(32)
    print("original m =", m)
    print()

    # =========================
    # Enc
    # =========================
    print("Enc...")
    c = enc(pk, m, kyber)

    print("ciphertext blocks =", len(c))
    print("poly length =", len(c[0]))
    print()

    # =========================
    # Dec
    # =========================
    print("Dec...")
    m2 = dec(sk, c, kyber)

    print("recovered m =", m2)
    print()

    # =========================
    # correctness
    # =========================
    print("correct =", m == m2)

    # REPEAT = 20
    #
    # # =========================
    # # KeyGen timing
    # # =========================
    # t0 = time.perf_counter()
    # for _ in range(REPEAT):
    #     pk, sk = keygen()
    # t1 = time.perf_counter()
    #
    # keygen_time = (t1 - t0) / REPEAT
    #
    # # =========================
    # # prepare test message
    # # =========================
    # m = os.urandom(32)
    # coins = os.urandom(32)
    #
    # # =========================
    # # Enc timing
    # # =========================
    # t0 = time.perf_counter()
    # for _ in range(REPEAT):
    #     c = enc(pk, m, coins)
    # t1 = time.perf_counter()
    #
    # enc_time = (t1 - t0) / REPEAT
    #
    # # =========================
    # # Dec timing
    # # =========================
    # t0 = time.perf_counter()
    # for _ in range(REPEAT):
    #     m2 = dec(sk, c)
    # t1 = time.perf_counter()
    #
    # dec_time = (t1 - t0) / REPEAT
    #
    # # correctness check
    # print(m)
    # print(m2)
    # print("correct =", m == m2)
    #
    # # sizes (KB)
    # print("pk size = %.3f KB" % (len(pk) / 1024))
    # print("sk size = %.3f KB" % (len(sk) / 1024))
    # print("ct size = %.3f KB" % (len(c) / 1024))
    #
    # # timing
    # print()
    # print("KeyGen avg time =", keygen_time, "sec")
    # print("Enc    avg time =", enc_time, "sec")
    # print("Dec    avg time =", dec_time, "sec")
