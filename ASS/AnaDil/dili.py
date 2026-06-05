from dilithium.dilithium import Dilithium2, Dilithium3, Dilithium5
import os
import time

REPEAT = 10

dili = Dilithium5


def keygen():
    seed = os.urandom(32)
    return dili.keygen(seed)


def sign(message: bytes, sk: bytes):
    return dili.sign_with_input(sk, message)


def verify(message: bytes, signature: bytes, pk: bytes):
    return dili.verify(pk, message, signature)


def size_kb(x: bytes):
    return len(x) / 1024


def main():
    print("=== Dilithium (your implementation) ===")
    print("Repeat =", REPEAT)

    message = b"Hello Dilithium"

    keygen_times = []
    sign_times = []
    verify_times = []

    pk_sizes = []
    sk_sizes = []
    sig_sizes = []

    for _ in range(REPEAT):
        # =========================
        # KeyGen
        # =========================
        t0 = time.perf_counter()
        pk, sk = keygen()
        t1 = time.perf_counter()
        keygen_times.append(t1 - t0)

        pk_sizes.append(size_kb(pk))
        sk_sizes.append(size_kb(sk))

        # =========================
        # Sign
        # =========================
        t0 = time.perf_counter()
        signature = sign(message, sk)
        t1 = time.perf_counter()
        sign_times.append(t1 - t0)

        sig_sizes.append(size_kb(signature))

        # =========================
        # Verify
        # =========================
        t0 = time.perf_counter()
        verify(message, signature, pk)
        t1 = time.perf_counter()
        verify_times.append(t1 - t0)

    print("\n===== Average Results =====")

    print("pk size: %.4f KB" % (sum(pk_sizes) / REPEAT))
    print("sk size: %.4f KB" % (sum(sk_sizes) / REPEAT))
    print("signature size: %.4f KB" % (sum(sig_sizes) / REPEAT))

    print("\nKeyGen time: %.6f s" % (sum(keygen_times) / REPEAT))
    print("Sign time:   %.6f s" % (sum(sign_times) / REPEAT))
    print("Verify time: %.6f s" % (sum(verify_times) / REPEAT))

    # 再测一次正确性
    pk, sk = keygen()
    signature = sign(message, sk)

    print("\nCorrectness check:")
    print("Verify (correct):", verify(message, signature, pk))
    print("Verify (tampered):", verify(b"Hello Hacker", signature, pk))


if __name__ == "__main__":
    main()
