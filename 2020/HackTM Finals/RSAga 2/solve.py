from Crypto.Util.number import inverse, long_to_bytes, isPrime, inverse
from itertools import combinations
import math


def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < 1 << 50:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr


def factor(n, limit):
    number = n
    factors = []
    currentFactor = 3

    while True:
        if number % 2 == 0:
            factors.append(2)
            number //= 2
        else:
            break
        
    while currentFactor <= limit:
        if number % currentFactor == 0 and isPrime(currentFactor):
            factors.append(currentFactor)
            number //= currentFactor
        else:
            currentFactor += 2

    return factors

e = 65537
dpq = 0x43a3212823d9e613ee57bdbba906274a4e59cc56d4ea51ab76a9f97669195d77938bf1b860ff2640d3160fb6b817b7c52fa48eeeaf71ca886d4fd27da8f11f8804dc60d7559abc429e15643bba047b889ed9e541d0170ccf842c4f374be5e31adfe1beeaabce2fa9c399b6d9bf165b8a3ff2219a320a612de909c27bc910ca1a662674a242f785b270ea323b2c33f1fda365f3a0eaff7e44d0ba189f15321253ce28289f8e2d28d55098f74061ae02e454bbfd01de90c9be1a799d3047fdc6ceeb0830a32bc575f84550b8012495f5456a96e67ffca467b1f01c03eb39bbee774e4921292b1771a9bc69c0cf4a7b0c369f536e07875ddc48a2ed07da3549608b
dp_q = 0x114bfb65b949a828715008b409e90188aa0317898e2bde1964a0e41a84222634233b37e183bf3b4bf1d03379bbacd83dff3fc616dc126913c2e33fe8294b12f833d478de09f61d29c1b237578c60936864232a11abe3b88064df4867e596b2e3ea6eb2ea5d763208200c55196966c9c726c3ab0156ce6ec53861a3dc202d4338c
c = 0x4b98514669c01d287de7c4bad143d8560c35584b6fd44c2f6b877b6caa02d7eba6c59d5699014fddd639add17947db082477444f8948b76e94bfac5145b1f554f4e0e410751b144975d6e63cc937be72652ea45669de50f6bd2ffcd77eea4c0882a830acebe380f7a02aa6ee4aa3023c749fcb9d52243b55d103e8470d16f2fc02bfa2e3b701c5800a925fe30c406a915cf1a02386a01c4b3a16c1c1e5596452ce7385a721ca80f1a51b66a46cb903f2b90715e23a4e9d2b1ac33805b6af92bbe6b036b5a5b4f2efcff98b2a0e9924533e8909e034850de10c78a8dd28c108ec513f7ed8980a47678536c8f38af36d5a94c2b763d9faae9c7f338af70ffd51e3

print(f"Step 1 recovering n * phiN:")
nPhiN = e * (dpq * e -dp_q) + 1

print(f"n * phiN: {nPhiN}")

print("Step 2, recovering dp and dq..")


m = (dp_q) // 2
z = (m**2) - dpq
dp = abs(-m + isqrt(z))
dq = abs(-m - isqrt(z))
print(f"Recovered dp and dq..")



print(f"Step 3, recovering p")
r = 2#2**((nPhiN.bit_length() - 2048) - 1)

bfBitLength = nPhiN.bit_length() - 2048
print(f"Bruteforcing bit length: {bfBitLength}")
while True:#r.bit_length() == bfBitLength:
    if nPhiN % r == 0:
        phiN = nPhiN // r
        d = inverse(e, nPhiN // r)
        nDP = d - dp
        p = math.gcd(phiN, nDP) + 1

        n = 2
        while not isPrime(p) and p != 1:
            p = math.gcd(p, pow(n, phiN, p) - 1)
            n += 1
        if p.bit_length() == 1024 and isPrime(p):
            print(f"Recoverd p: {p}")
            break
    r += 2
print(f"Step 4, recovering q")
r = 2**((nPhiN.bit_length() - 2048) - 1)

phiN = nPhiN // (p - 1)
factors = factor(phiN, 10000)

z = 1

found = False
for i in range(1, len(factors)):
    perms = combinations(factors, i)
    for v in perms:
        num = 1
        for j in v:
            num *= j
        phiN2 = (phiN // num)
        q = phiN2 + 1
        if q.bit_length() == 1024 and isPrime(q):
            N = p * q
            d = inverse(e, phiN2)
            #if pow(2, phiN2, N) == 1:
            if dq == d % (q - 1):
                print(f"Recoverd q: {q}")
                found = True
                break
        z += 1
    if found:
        break
    print(f"Finished perm: {i}")

print(f"Step 5, decrypting")
phiN = (p - 1) * (q-1)
d = inverse(e, phiN)
N = p * q


print(f"Recovered N: {N}")
m = pow(c, d, N)
print(long_to_bytes(m).decode())