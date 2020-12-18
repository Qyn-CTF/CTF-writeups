from Crypto.Util.number import inverse, long_to_bytes, isPrime
import math

e = 65537
d = 0x5f3538b32864f0c1b9878ce92313c0853bf324123b94d419f92b370b839055ce520c4549d0a5c1fe9679bf41631cb8caf827c3b12d946ae9dccd5e437a71ae13064e0ab02828e915aabdf359b621de141ff424460726d3a8aa57c38cd06252b38be3b4a05c6ead7c6dba8c6ca244c35c5a0281e24c36540f991994adb75d7690891f1fa71a3c14ba41fb45563a9937ced564081b24459757c31ce6ecfb2a09aaf6dc19d18dfb3e70d68cded103a4be22f235e07d81e43ec231c32768c8699c5889969d43801f929f1567f36d93f7336173492b3a9d49d21cdbb0f6a8a0ef3e927aee0e39cf42e61a406adaaf8cc15f89f14cf94f2d4f229e34c0299aa0fa4ea1
dp = 0xda33b8da746b23bb54b7e5e042b41b66ba6940f60b300e684f54277d65205732beb1372374182bfc2c2ba51bbf1c3393c19cff6e66c1ebf344eb3d8f2a4d8e37daf21e4cedc295ea0e0c87e177fcc80fc81f66c8c9c31c942c77615bef15966411a14c8901afd28da9e547b1132bfb7cce743741ced778a9e7a0a3fa2c646701
c = 0x6b8c5eb7628781cd7faafbb75fd824602e813382eb6e52bbde9c6f61238b8a6365df3f2a1f361d40e2f3c584a505180df0e2755345ce9a20419d129284789ba81348c5e3b10d2b491a000f150615272cd1ba2ca8844c0233c1ac614388c1c000215324b10065738106f2e5e8c82956b7056860a156556688f614fbca3d509c4cce091f9634274a4735fc4e0ac9e2e09bffc41ef15953049b2d76b0551ce15f17c01604c531885a1c764d5473532ebe3343683685b9a2ab1e726513c4260401e1ad7744e109eb2e59b18c043045024c30029fb77eeec3e7095711d77f4135218ac38f0e3ed4928e5f92fbca86bb4b1b88ad43c861d4ba6dbd508cc41915afbbfb

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