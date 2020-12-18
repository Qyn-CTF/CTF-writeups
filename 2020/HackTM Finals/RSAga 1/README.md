## First looks
We're given $dp = d \bmod p-1$, $d$ and $e = 65537$. We're also given the ciphertext. Our goal is to recover the modulus $N = p \times q$  

## Solving
We know that $d \times e = 1 \bmod \varphi(N)$. Which means that $d \times e - 1 = \it{n} \times \varphi(N)$ for any $\it{n} \in \mathbb{N}$ and since $\it{n} < \varphi(N)$ is $\it{n} < e = 65537$. This allows us to bruteforce $\varphi(N)$.  
We also know that $dp - d = \it{k} \times (p-1)$, and since $\varphi(N) = (p-1) \times (q-1)$ they both contain a factor of $p-1$. So we can set $nP = GCD(dp - d, \varphi(N))$. Now, since $nP$ is a factor of $p - 1$, we can simply try out simple factors $< 100$.  
When the result ($nP + 1$) is prime and bit length of 1024, it's probably our value of $p - 1$, however, we can verify this by using Euler's theorm: $n^{\varphi(N)} = 1 \bmod N$ for any $\it{n} \in \mathbb{N}$, and $N$ is a multiple of $p$ the following holds true: $n^{\varphi(N)} = 1 \bmod (nP + 1)$. So $nP == GCD(n^{\varphi(N)} - 1, nP)$.  

We can then do the same for $q$ and retrieve $N$

#### Side node
It's also possible to use Euler's theorm to retrieve $p$ by: $p = GCD(n^{\varphi(N)} - 1, nP)$ and checking whether $p$ is not $1$ and is prime

### Code
```python
from Crypto.Util.number import inverse, long_to_bytes, isPrime
import math

e = 65537
d = 0xbdf70cdd2e1a1044beb1d4d01cb7053cc1178b27d3d2eba2639894a396e1fe2e35a34e869b4dd1d474346c80bfe290d588673322c32eb3f7e722761f2cb6f0d98085efe0c9f39f430dc11cff01df514826b4de2026ab589238a90f4e3e63ec34b0e67a53eafb383bb3cac9a4ca27ac2049ce02de431142a88fb1a981a7b109141a77ef7ec8223b2228c1cebc667259fda28fa37ad7741536102ceb79d49fd55165af732395de55953826bc3e46f96886aad59ee8530d01692706c07f5cab6edac031cfee7f5adeca38b7b658232148e04e56494cbd3db4cda24c553e7fbc5087f3919994919847ccf28e352f09685ebfb6ada898d60295b674abf909d8944001
dp = 0x5bbcca611e9d82ad17fe3430571a2e571f5fbffe8491ed3b4ac6f056cf86746da7770bbba469b4e648a2b4c03645c9d21c3fc9d1fe52aebacb0cc97b2ae7bf4287dd3ed3219f081725fc34595b7d8bdccb4a2baff5461b42329f4e07ea132a24e9f52e3161813f93098164f56f2af3dc3099a0e779f12d74dbe61abe04827001
c = 0xae5ff79b741ed77e531c1a8ef87084abda154321685c46e5b00ed351c5ebfa4c3adac5e6b4adbb009a57bee28e3fcfd6df24fb6c5aad77073b836d2f6d3042f81bb3381466763dd2a0459c2096718bcdba3000823aa1cc807c71e56f43a5e62a70066ab7dafca015ee8b62aa21aa6353cb18bb4d26317a0f623ab5b01de50da1146f920b69434c0b62c1878e4b312d298afa70ebc5b52170abd06d8aadbd5abc0686ef84f234617ae7f3e3de428ce6c53c553be235a49e42ce80b7ae0ba051c00f8cd9d15c5c84f1eae18f129832409fa52fb9227d7a48184ec9fcfb20805878e0f233390604415df34306ee4c47f8486501a1b741b310bff98c41e9c9dbad30

kphiN = e * d - 1
nDP = d - dp

checkRange = 100
for k in range(3, e + 1):
    if kphiN % k == 0:
        phiN = kphiN // k
        p = math.gcd(phiN, nDP)
        nP = p
        n = 2
        while not isPrime(nP + 1) and n < checkRange:
            nP = p // n
            n += 1

        p = nP + 1
        if p.bit_length() == 1024 and isPrime(p) and p == math.gcd(p, pow(5, phiN, p) - 1):
            print(p)
            print("Found p")
            break

for k in range(3, 65537 + 1):
    if kphiN % k == 0:
        phiN = kphiN // k
        if phiN % (p - 1) != 0:
            continue
        q = (phiN // (p - 1))
        nQ = q
        n = 2
        #while not isPrime(q) and q != 1:
        #    q = math.gcd(q, pow(n, phiN, q) - 1)
        #    n += 1
        while not isPrime(nQ + 1) and n < checkRange:
            nQ = q // n
            n += 1
            
        q = nQ + 1
        if q.bit_length() == 1024 and isPrime(q) and q == math.gcd(q, pow(5, phiN, q) - 1):
            print(q)
            print("Found q")
            break
    
assert q != 1 or p != -1, "Was unable to recover p and/or q"

N = p * q
m = pow(c, d, N)
print(long_to_bytes(m).decode())
```

Which prints the flag: `HackTM{0ac4d80522000109a3e010feee5dc627ee37413754489996dde528724ea2189dabfb722f2877d8a3f8f3c8f994fee230c24fb54a77dafbedfc30b7ccdb0b9851}`