import math

from sympy import symbols, Poly

# =========================
# 参数
# =========================
n = 512
l = 2
t = 2
q = 3329
delta = math.floor(q / t)
eta1 = 1
eta2 = 2
eta3 = 1
eta4 = 1
x = symbols('x')
fx = Poly(x ** n + 1, x, domain='ZZ')