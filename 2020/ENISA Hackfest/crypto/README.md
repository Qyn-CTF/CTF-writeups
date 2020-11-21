# crypto (200pts, 31 solved) Misc & Cryptography [Easy]            

## First look
We're getting an encrypted message: `f59d4ea17bf649c6bf1b3967fe2203b570fd180c4100247847348e20b86c6c7febacc33b5c2f9b8262e40edf114d55286f5d7634735e3671674c5a` and a _small_ crypto function.

## Solving
All we need to do is reimplement this algorithm in z3, it's just copying a lot of code and since we know the flag is in format: `DCTF{..` and we can guess that it ends with a `}` ->
```python
from z3 import *

a_vec = BitVec("a", 64)
b_vec = BitVec("a", 64)
c_vec = BitVec("b", 64)

a, b, c = a_vec, b_vec, c_vec

enc = "f59d4ea17bf649c6bf1b3967fe2203b570fd180c4100247847348e20b86c6c7febacc33b5c2f9b8262e40edf114d55286f5d7634735e3671674c5a"
flag_enc = bytes.fromhex(enc[40:])
flag = [BitVec('x%d' % i, 64) for i in range(len(flag_enc))]

s = Solver()

for item in flag:
    s.add(item >= 0x20)
    s.add(item <= 0x7D)


for idx, item in enumerate(flag_enc):
    s.add(((flag[idx] - (a&0xFF)) ^ (b&0xFF) ^ (c&0xFF)) &0xFF == item)
    a = RotateRight(a, 1)
    b = RotateLeft(b, 1)
    c = RotateLeft(c, 1)


AND = []
for idx in range(len(flag) - 4):
    toAdd = []
    for idx_1, c in enumerate("DCTF{"):
        toAdd.append(flag[idx + idx_1] == ord(c))
    AND.append(And(toAdd))

s.add(Or(AND))

s.add(flag[len(flag) - 1] == ord("}"))

while True:
    if s.check() == sat:
        m = s.model()
        aa = m[a_vec].as_long()
        bb = m[b_vec].as_long()
        cc = m[c_vec].as_long()
        
        flag_dec = ""
        for item in flag:
            f = m[item].as_long()
            flag_dec += chr(f)
        print(flag_dec)
        notAgain = []
        notAgain.append(a_vec != m[a_vec].as_long())
        notAgain.append(b_vec != m[b_vec].as_long())
        notAgain.append(c_vec != m[c_vec].as_long())
        s.add(Or(notAgain))
    else:
        break
```
After a little bit, we start seeing stuff like `Flag is: DCTF{_th1s_w4s_4un_}`, which obviously is our flag: `DCTF{_th1s_w4s_4un_}`