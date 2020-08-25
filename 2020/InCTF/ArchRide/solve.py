from z3 import *
from pwn import *
import struct
import bz2

def solve(vals):
    x0 = BitVec('x0', 32)
    x1 = BitVec('x1', 32)
    x2 = BitVec('x2', 32)
    x3 = BitVec('x3', 32)
    x4 = BitVec('x4', 32)
    x5 = BitVec('x5', 32)
    x6 = BitVec('x6', 32)
    x7 = BitVec('x7', 32)
    x8 = BitVec('x8', 32)
    x9 = BitVec('x9', 32)
    x10 = BitVec('x10', 32)
    x11 = BitVec('x11', 32)
    x12 = BitVec('x12', 32)
    x13 = BitVec('x13', 32)
    s = Solver()
    s.add(
    x4 ^ x0 ^ x2 == vals[0],
    x4 ^ x2 ^ x6 == vals[1],
    x6 ^ x4 ^ x8 == vals[2],
    x8 ^ x6 ^ x10 == vals[3],
    x10 ^ x8 ^ x12 == vals[4],
    x12 ^ x10 ^ x1 == vals[5],
    x1 ^ x12 ^ x3 == vals[6],
    x3 ^ x1 ^ x5 == vals[7],
    x5 ^ x3 ^ x7 == vals[8],
    x7 ^ x5 ^ x9 == vals[9],
    x9 ^ x7 ^ x11 == vals[10],
    x11 ^ x9 ^ x13 == vals[11],
    x13 ^ x11 ^ x0 == vals[12],
    x0 ^ x13 ^ x2 == vals[13],

    x1 ^ x0 ^ x2 == vals[14],
    x2 ^ x1 ^ x3 == vals[15],
    x3 ^ x2 ^ x4 == vals[16],
    x4 ^ x3 ^ x5 == vals[17],
    x5 ^ x4 ^ x6 == vals[18],
    x6 ^ x5 ^ x7 == vals[19],
    x7 ^ x6 ^ x8 == vals[20],
    x8 ^ x7 ^ x9 == vals[21],
    x9 ^ x8 ^ x10 == vals[22],
    x10 ^ x9 ^ x11 == vals[23],
    x11 ^ x10 ^ x12 == vals[24],
    x12 ^ x11 ^ x13 == vals[25],
    x13 ^ x12 ^ x0 == vals[26],
    x0 ^ x13 ^ x1 == vals[27],)
    s.check()
    return chr(s.model().eval(x0).as_long()) + chr(s.model().eval(x1).as_long())  + chr(s.model().eval(x2).as_long()) + chr(s.model().eval(x3).as_long())+ chr(s.model().eval(x4).as_long())+ chr(s.model().eval(x5).as_long())+ chr(s.model().eval(x6).as_long())+ chr(s.model().eval(x7).as_long())+ chr(s.model().eval(x8).as_long())+ chr(s.model().eval(x9).as_long())+ chr(s.model().eval(x10).as_long())+ chr(s.model().eval(x11).as_long())+ chr(s.model().eval(x12).as_long())+ chr(s.model().eval(x13).as_long())


def solveXor(data, offset1, offset2): 
    vals = struct.unpack(14* "I", data[offset1:offset1 + 4*14])
    
    vals += struct.unpack(14* "I", data[offset2:offset2 + 4*14])
    return solve(vals)


def unpack(password, data, endian):
    res = []
    key = password.encode()
    for i in range(len(data)//8):
        #struct.unpack is really slow
        byte = int.from_bytes(data[i*8:(i+1)*8], endian)
        res.append((byte ^ key[i %  0xd]) & 0xff)
    return bytes(res)


def start(filename, p, p2):
    p2.status("Reading file")
    with open(filename, "rb") as file:
        data = file.read()
    p.status("Decompressing")
    try:
        decompressed = bz2.decompress(data)
    except:
        return False

    endian = "little"
    if b"/lib/ld-linux-aarch64.so.1" in decompressed: #aarch64
        password = solveXor(decompressed, 0x2010, 0x2048)
        start = 0x2080
    elif b"/lib/ld-linux-armhf.so.3" in decompressed: #arm
        password = solveXor(decompressed, 0x1008, 0x1040)
        start = 0x1078
    elif b"/lib64/ld64.so.1" in decompressed: #powerpc64 though this file is also used in aarch64, but that's been checked first
        password = solveXor(decompressed, 0x10133, 0x1016b)
        start = 0x101a0
        endian = "big"
    elif b"/lib64/ld-linux-x86-64.so.2" in decompressed or b"/lib/ld-linux.so.2" in decompressed: #64/x86
        password = solveXor(decompressed, 0x2020, 0x2060)
        start = 0x20a0
    else:
        log.err("Found unknown arch")
        return False

    p2.status("Found password: {0}".format(password))

    p.status("Decrypting")


    decrypted = unpack(password, decompressed[start:], endian)

    with open("surprise", "wb") as file:
        file.write(decrypted)

    p.status("Done")
    return True

success = True
layers = 1
with log.progress('Starting') as p, log.progress("Starting") as p2, log.progress("Starting") as p3:
    while success:
        p3.status("Doing {0}".format(layers))
        file = "surprise"
        success = start(file, p, p2)
        if success:
            layers += 1
    p.success("Finished run the ./surprise for the flag")
    p3.success("Found: {0} layers".format(layers))