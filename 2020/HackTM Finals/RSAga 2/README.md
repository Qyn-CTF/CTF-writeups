## First looks
We're given $dp \times dq$ and $dp + dq$ where $dq = d \bmod (q-1)$ and $dp = d \bmod (p-1)$, we're also given $e = 65537$, and the ciphertext. Our goal is to recover the modulus $N = p \times q$ to finally decrypt the ciphertext. 

## Solving
### Recovering $dp, dq$
We can combine $dp \equiv d \bmod (p-1)$ and $dq \equiv d \bmod (q-1)$ to the following: $(dp-d) \times (dq-d) \equiv 0 \bmod \varphi(N)$ where $\varphi(N) = (p-1)\times(q-1)$. This is essentially a quadratic equation: $d^2 + dpq - d \times (dp + dq - d) \equiv 0 \bmod \varphi(N)$. We can then use the *simplified* quadratic formula to solve this: $dp,dq = \dfrac{dp + dq}{2} \pm \sqrt{(\dfrac{dp + dq}{2})^2 - dp \times dq}$ since $(\dfrac{dp + dq}{2})^2 - dp \times dq$ is a perfect square. Now we know $dp, dq$.  

### Recovering a factor of $\varphi(N)$
In the previous section, we combined two equations to get this: $d^2 + dpq - d \times (dp + dq - d) \equiv 0 \bmod \varphi(N)$, however, $d = \dfrac{\varphi(N) + 1}{e}$. So $(\dfrac{\varphi(N) + 1}{e}))^2 + dpq - (\dfrac{\varphi(N) + 1}{e}) \times (dp + dq - d) \equiv 0 \bmod \varphi(N)$, so by multiplying with $e$, we can simplify, because of the $\bmod \varphi(N)$ we get: $e \times (dpq \times e - (dp + dq)) + 1 \equiv 0 \bmod \varphi(N)$.  
So $e \times (dpq \times e - (dp + dq)) + 1$ is a factor of $\varphi(N)$.  

### Recovering $\varphi(N)$
We can now recover the original $\varphi(N)$, since $e \times (dpq \times e - (dp + dq)) + 1$ is build up from a lot of smaller prime factors:
```python
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

nPhiN = e * (dpq * e -dp_q) + 1

factors = factor(nPhiN, 100000)
```
Alternatively, use `factordb`.  
We can now enumerate through all the factors in such a way that the order doesn't matter and that we don't check the same factor multiple times, even though it occurs in `factors` multiple times. For simplicity, I just used `itertools.combinations` (Which will be a bit less efficient, since it doesn't satisfy the last rule, but it works):
```python
for i in range(1, len(factors)):
    perms = combinations(factors, i)
    for combs in perms:
        num = 1
        for comb in combs:
            num *= comb
        phiN = nPhiN // num
    #...
    print(f"Finished perm: {i}")
```
From here we can get a value for $d = e^{-1} \bmod \varphi(N)$ and at that point we can run the solution script from `RSAga 1` since we recovered $dp, dq$ in the first step and modifying it a bit.  
*Note, there are many ways to solve this from this point*

Which finally gives us the flag:
`HackTM{36f1a66ce55057caeebfa274c1d0abc67e3fd95c83ec0252812b38dfd2a1fd60d6172d793c3124acd02b5504cb7ce19c87896b5ac24bb324528f4b934f0232a3}`