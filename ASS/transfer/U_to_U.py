import math
import random


def u_to_u_int(x, a, b):  # x ← U(Z_[0,a])
    tau = math.floor(b / a)
    r = b % tau
    d = random.randint(0, tau - 1)
    yy = tau * x + d

    i = math.floor(yy / tau) + 1
    p = (r + 1) / (b + 1)

    # sample ε
    if yy <= (a - 1) * tau + r:
        # ε = τ with prob ip, else 0
        if random.random() < i * p:
            eps = tau
        else:
            eps = 0
    else:
        # ε ∈ [aτ - y', aτ + r - y'] with prob ap, else 0
        if random.random() < a * p:
            eps = random.randint(a * tau - yy, a * tau + r - yy)
        else:
            eps = 0
    y = yy + eps
    return y


def u_backto_u_int(y, a, b):
    tau = math.floor(b / a)
    x = math.floor(y / tau)
    return x


# =========================
# main
# =========================
def main():
    a = 3329
    b = 131072
    N = 50

    for _ in range(N):
        x = random.randint(0, a)
        y = u_to_u_int(x, a, b)
        x_rec = u_backto_u_int(y, a, b)

        print(f"x={x}, y={y}, x'={x_rec}, x-x'={x - x_rec}")


if __name__ == "__main__":
    main()
