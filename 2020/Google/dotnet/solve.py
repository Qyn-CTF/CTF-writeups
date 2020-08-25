from z3 import *

def encodeBase64Bytewise(LINNMON):
    result = ""
    for i in range(len(LINNMON)):
        result += chr(EncodeBase64Bytewise(LINNMON[i]))
    return result

def EncodeBase64Bytewise(arg):
    if (arg <= 9):
        return (arg + 48)
    if (arg-10 <= 25):
        return (arg + 55)
    if (arg - 36 <= 25):
        return (arg + 61)
    if (arg == 62):
        return 123
    if (arg == 63):
        return 125
    return -1

def calcChecksum(list):
    num = 16
    for i in range(len(list)):
        if i != len(list) - 2:
            num = list[i] + num
            if (i % 2 == 0):
                num = list[i] + num
            num3 = i 
            if num3 - num3 // 3 * 3 == 0:
                num = list[i] * 4294967294 + num 
            num4 = i
            if num4 - num4 // 5 * 5 == 0:
                num = list[i] * 4294967293 + num
            num5 = i   
            if num5 - num5 // 7 * 7 == 0:
                num = list[i] * 4 + num
    return num & 63
            
def xor(data, key):
    l = len(key)
    decoded = b""
    for i in range(0, len(data)):
        decoded += bytes([(data[i] ^ key[i % l])])
    return decoded

flag0 = BitVec('flag0',32)
flag1 = BitVec('flag1',32)
flag2 = BitVec('flag2',32)
flag3 = BitVec('flag3',32)
flag4 = BitVec('flag4',32)
flag5 = BitVec('flag5',32)
flag6 = BitVec('flag6',32)
flag7 = BitVec('flag7',32)
flag8 = BitVec('flag8',32)
flag9 = BitVec('flag9',32)
flag10 = BitVec('flag10',32)
flag11 = BitVec('flag11',32)
flag12 = BitVec('flag12',32)
flag13 = BitVec('flag13',32)
flag14 = BitVec('flag14',32)
flag15 = BitVec('flag15',32)
flag16 = BitVec('flag16',32)
flag17 = BitVec('flag17',32)
flag18 = BitVec('flag18',32)
flag19 = BitVec('flag19',32)
flag20 = BitVec('flag20',32)
flag21 = BitVec('flag21',32)
flag22 = BitVec('flag22',32)
flag23 = BitVec('flag23',32)
flag24 = BitVec('flag24',32)
flag25 = BitVec('flag25',32)
flag26 = BitVec('flag26',32)
flag27 = BitVec('flag27',32)
flag28 = BitVec('flag28',32)
flag29 = BitVec('flag29',32)
s = Solver()

s.add(
    flag0 != flag1, flag0 != flag2, flag0 != flag3, flag0 != flag4, flag0 != flag5, flag0 != flag6, flag0 != flag7, flag0 != flag8, flag0 != flag9, flag0 != flag10, flag0 != flag11, flag0 != flag12, flag0 != flag13, flag0 != flag14, flag0 != flag15, flag0 != flag16, flag0 != flag17, flag0 != flag18, flag0 != flag19, flag0 != flag20, flag0 != flag21, flag0 != flag22, flag0 != flag23, flag0 != flag24, flag0 != flag25, flag0 != flag26, flag0 != flag27, flag0 != flag28, flag0 != flag29, flag1 != flag0, flag1 != flag2, flag1 != flag3, flag1 != flag4, flag1 != flag5, flag1 != flag6, flag1 != flag7, flag1 != flag8, flag1 != flag9, flag1 != flag10, flag1 != flag11, flag1 != flag12, flag1 != flag13, flag1 != flag14, flag1 != flag15, flag1 != flag16, flag1 != flag17, flag1 != flag18, flag1 != flag19, flag1 != flag20, flag1 != flag21, flag1 != flag22, flag1 != flag23, flag1 != flag24, flag1 != flag25, flag1 != flag26, flag1 != flag27, flag1 != flag28, flag1 != flag29, flag2 != flag0, flag2 != flag1, flag2 != flag3, flag2 != flag4, flag2 != flag5, flag2 != flag6, flag2 != flag7, flag2 != flag8, flag2 != flag9, flag2 != flag10, flag2 != flag11, flag2 != flag12, flag2 != flag13, flag2 != flag14, flag2 != flag15, flag2 != flag16, flag2 != flag17, flag2 != flag18, flag2 != flag19, flag2 != flag20, flag2 != flag21, flag2 != flag22, flag2 != flag23, flag2 != flag24, flag2 != flag25, flag2 != flag26, flag2 != flag27, flag2 != flag28, flag2 != flag29, flag3 != flag0, flag3 != flag1, flag3 != flag2, flag3 != flag4, flag3 != flag5, flag3 != flag6, flag3 != flag7, flag3 != flag8, flag3 != flag9, flag3 != flag10, flag3 != flag11, flag3 != flag12, flag3 != flag13, flag3 != flag14, flag3 != flag15, flag3 != flag16, flag3 != flag17, flag3 != flag18, flag3 != flag19, flag3 != flag20, flag3 != flag21, flag3 != flag22, flag3 != flag23, flag3 != flag24, flag3 != flag25, flag3 != flag26, flag3 != flag27, flag3 != flag28, flag3 != flag29, flag4 != flag0, flag4 != flag1, flag4 != flag2, flag4 != flag3, flag4 != flag5, flag4 != flag6, flag4 != flag7, flag4 != flag8, flag4 != flag9, flag4 != flag10, flag4 != flag11, flag4 != flag12, flag4 != flag13, flag4 != flag14, flag4 != flag15, flag4 != flag16, flag4 != flag17, flag4 != flag18, flag4 != flag19, flag4 != flag20, flag4 != flag21, flag4 != flag22, flag4 != flag23, flag4 != flag24, flag4 != flag25, flag4 != flag26, flag4 != flag27, flag4 != flag28, flag4 != flag29, flag5 != flag0, flag5 != flag1, flag5 != flag2, flag5 != flag3, flag5 != flag4, flag5 != flag6, flag5 != flag7, flag5 != flag8, flag5 != flag9, flag5 != flag10, flag5 != flag11, flag5 != flag12, flag5 != flag13, flag5 != flag14, flag5 != flag15, flag5 != flag16, flag5 != flag17, flag5 != flag18, flag5 != flag19, flag5 != flag20, flag5 != flag21, flag5 != flag22, flag5 != flag23, flag5 != flag24, flag5 != flag25, flag5 != flag26, flag5 != flag27, flag5 != flag28, flag5 != flag29, flag6 != flag0, flag6 != flag1, flag6 != flag2, flag6 != flag3, flag6 != flag4, flag6 != flag5, flag6 != flag7, flag6 != flag8, flag6 != flag9, flag6 != flag10, flag6 != flag11, flag6 != flag12, flag6 != flag13, flag6 != flag14, flag6 != flag15, flag6 != flag16, flag6 != flag17, flag6 != flag18, flag6 != flag19, flag6 != flag20, flag6 != flag21, flag6 != flag22, flag6 != flag23, flag6 != flag24, flag6 != flag25, flag6 != flag26, flag6 != flag27, flag6 != flag28, flag6 != flag29, flag7 != flag0, flag7 != flag1, flag7 != flag2, flag7 != flag3, flag7 != flag4, flag7 != flag5, flag7 != flag6, flag7 != flag8, flag7 != flag9, flag7 != flag10, flag7 != flag11, flag7 != flag12, flag7 != flag13, flag7 != flag14, flag7 != flag15, flag7 != flag16, flag7 != flag17, flag7 != flag18, flag7 != flag19, flag7 != flag20, flag7 != flag21, flag7 != flag22, flag7 != flag23, flag7 != flag24, flag7 != flag25, flag7 != flag26, flag7 != flag27, flag7 != flag28, flag7 != flag29, flag8 != flag0, flag8 != flag1, flag8 != flag2, flag8 != flag3, flag8 != flag4, flag8 != flag5, flag8 != flag6, flag8 != flag7, flag8 != flag9, flag8 != flag10, flag8 != flag11, flag8 != flag12, flag8 != flag13, flag8 != flag14, flag8 != flag15, flag8 != flag16, flag8 != flag17, flag8 != flag18, flag8 != flag19, flag8 != flag20, flag8 != flag21, flag8 != flag22, flag8 != flag23, flag8 != flag24, flag8 != flag25, flag8 != flag26, flag8 != flag27, flag8 != flag28, flag8 != flag29, flag9 != flag0, flag9 != flag1, flag9 != flag2, flag9 != flag3, flag9 != flag4, flag9 != flag5, flag9 != flag6, flag9 != flag7, flag9 != flag8, flag9 != flag10, flag9 != flag11, flag9 != flag12, flag9 != flag13, flag9 != flag14, flag9 != flag15, flag9 != flag16, flag9 != flag17, flag9 != flag18, flag9 != flag19, flag9 != flag20, flag9 != flag21, flag9 != flag22, flag9 != flag23, flag9 != flag24, flag9 != flag25, flag9 != flag26, flag9 != flag27, flag9 != flag28, flag9 != flag29, flag10 != flag0, flag10 != flag1, flag10 != flag2, flag10 != flag3, flag10 != flag4, flag10 != flag5, flag10 != flag6, flag10 != flag7, flag10 != flag8, flag10 != flag9, flag10 != flag11, flag10 != flag12, flag10 != flag13, flag10 != flag14, flag10 != flag15, flag10 != flag16, flag10 != flag17, flag10 != flag18, flag10 != flag19, flag10 != flag20, flag10 != flag21, flag10 != flag22, flag10 != flag23, flag10 != flag24, flag10 != flag25, flag10 != flag26, flag10 != flag27, flag10 != flag28, flag10 != flag29, flag11 != flag0, flag11 != flag1, flag11 != flag2, flag11 != flag3, flag11 != flag4, flag11 != flag5, flag11 != flag6, flag11 != flag7, flag11 != flag8, flag11 != flag9, flag11 != flag10, flag11 != flag12, flag11 != flag13, flag11 != flag14, flag11 != flag15, flag11 != flag16, flag11 != flag17, flag11 != flag18, flag11 != flag19, flag11 != flag20, flag11 != flag21, flag11 != flag22, flag11 != flag23, flag11 != flag24, flag11 != flag25, flag11 != flag26, flag11 != flag27, flag11 != flag28, flag11 != flag29, flag12 != flag0, flag12 != flag1, flag12 != flag2, flag12 != flag3, flag12 != flag4, flag12 != flag5, flag12 != flag6, flag12 != flag7, flag12 != flag8, flag12 != flag9, flag12 != flag10, flag12 != flag11, flag12 != flag13, flag12 != flag14, flag12 != flag15, flag12 != flag16, flag12 != flag17, flag12 != flag18, flag12 != flag19, flag12 != flag20, flag12 != flag21, flag12 != flag22, flag12 != flag23, flag12 != flag24, flag12 != flag25, flag12 != flag26, flag12 != flag27, flag12 != flag28, flag12 != flag29, flag13 != flag0, flag13 != flag1, flag13 != flag2, flag13 != flag3, flag13 != flag4, flag13 != flag5, flag13 != flag6, flag13 != flag7, flag13 != flag8, flag13 != flag9, flag13 != flag10, flag13 != flag11, flag13 != flag12, flag13 != flag14, flag13 != flag15, flag13 != flag16, flag13 != flag17, flag13 != flag18, flag13 != flag19, flag13 != flag20, flag13 != flag21, flag13 != flag22, flag13 != flag23, flag13 != flag24, flag13 != flag25, flag13 != flag26, flag13 != flag27, flag13 != flag28, flag13 != flag29, flag14 != flag0, flag14 != flag1, flag14 != flag2, flag14 != flag3, flag14 != flag4, flag14 != flag5, flag14 != flag6, flag14 != flag7, flag14 != flag8, flag14 != flag9, flag14 != flag10, flag14 != flag11, flag14 != flag12, flag14 != flag13, flag14 != flag15, flag14 != flag16, flag14 != flag17, flag14 != flag18, flag14 != flag19, flag14 != flag20, flag14 != flag21, flag14 != flag22, flag14 != flag23, flag14 != flag24, flag14 != flag25, flag14 != flag26, flag14 != flag27, flag14 != flag28, flag14 != flag29, flag15 != flag0, flag15 != flag1, flag15 != flag2, flag15 != flag3, flag15 != flag4, flag15 != flag5, flag15 != flag6, flag15 != flag7, flag15 != flag8, flag15 != flag9, flag15 != flag10, flag15 != flag11, flag15 != flag12, flag15 != flag13, flag15 != flag14, flag15 != flag16, flag15 != flag17, flag15 != flag18, flag15 != flag19, flag15 != flag20, flag15 != flag21, flag15 != flag22, flag15 != flag23, flag15 != flag24, flag15 != flag25, flag15 != flag26, flag15 != flag27, flag15 != flag28, flag15 != flag29, flag16 != flag0, flag16 != flag1, flag16 != flag2, flag16 != flag3, flag16 != flag4, flag16 != flag5, flag16 != flag6, flag16 != flag7, flag16 != flag8, flag16 != flag9, flag16 != flag10, flag16 != flag11, flag16 != flag12, flag16 != flag13, flag16 != flag14, flag16 != flag15, flag16 != flag17, flag16 != flag18, flag16 != flag19, flag16 != flag20, flag16 != flag21, flag16 != flag22, flag16 != flag23, flag16 != flag24, flag16 != flag25, flag16 != flag26, flag16 != flag27, flag16 != flag28, flag16 != flag29, flag17 != flag0, flag17 != flag1, flag17 != flag2, flag17 != flag3, flag17 != flag4, flag17 != flag5, flag17 != flag6, flag17 != flag7, flag17 != flag8, flag17 != flag9, flag17 != flag10, flag17 != flag11, flag17 != flag12, flag17 != flag13, flag17 != flag14, flag17 != flag15, flag17 != flag16, flag17 != flag18, flag17 != flag19, flag17 != flag20, flag17 != flag21, flag17 != flag22, flag17 != flag23, flag17 != flag24, flag17 != flag25, flag17 != flag26, flag17 != flag27, flag17 != flag28, flag17 != flag29, flag18 != flag0, flag18 != flag1, flag18 != flag2, flag18 != flag3, flag18 != flag4, flag18 != flag5, flag18 != flag6, flag18 != flag7, flag18 != flag8, flag18 != flag9, flag18 != flag10, flag18 != flag11, flag18 != flag12, flag18 != flag13, flag18 != flag14, flag18 != flag15, flag18 != flag16, flag18 != flag17, flag18 != flag19, flag18 != flag20, flag18 != flag21, flag18 != flag22, flag18 != flag23, flag18 != flag24, flag18 != flag25, flag18 != flag26, flag18 != flag27, flag18 != flag28, flag18 != flag29, flag19 != flag0, flag19 != flag1, flag19 != flag2, flag19 != flag3, flag19 != flag4, flag19 != flag5, flag19 != flag6, flag19 != flag7, flag19 != flag8, flag19 != flag9, flag19 != flag10, flag19 != flag11, flag19 != flag12, flag19 != flag13, flag19 != flag14, flag19 != flag15, flag19 != flag16, flag19 != flag17, flag19 != flag18, flag19 != flag20, flag19 != flag21, flag19 != flag22, flag19 != flag23, flag19 != flag24, flag19 != flag25, flag19 != flag26, flag19 != flag27, flag19 != flag28, flag19 != flag29, flag20 != flag0, flag20 != flag1, flag20 != flag2, flag20 != flag3, flag20 != flag4, flag20 != flag5, flag20 != flag6, flag20 != flag7, flag20 != flag8, flag20 != flag9, flag20 != flag10, flag20 != flag11, flag20 != flag12, flag20 != flag13, flag20 != flag14, flag20 != flag15, flag20 != flag16, flag20 != flag17, flag20 != flag18, flag20 != flag19, flag20 != flag21, flag20 != flag22, flag20 != flag23, flag20 != flag24, flag20 != flag25, flag20 != flag26, flag20 != flag27, flag20 != flag28, flag20 != flag29, flag21 != flag0, flag21 != flag1, flag21 != flag2, flag21 != flag3, flag21 != flag4, flag21 != flag5, flag21 != flag6, flag21 != flag7, flag21 != flag8, flag21 != flag9, flag21 != flag10, flag21 != flag11, flag21 != flag12, flag21 != flag13, flag21 != flag14, flag21 != flag15, flag21 != flag16, flag21 != flag17, flag21 != flag18, flag21 != flag19, flag21 != flag20, flag21 != flag22, flag21 != flag23, flag21 != flag24, flag21 != flag25, flag21 != flag26, flag21 != flag27, flag21 != flag28, flag21 != flag29, flag22 != flag0, flag22 != flag1, flag22 != flag2, flag22 != flag3, flag22 != flag4, flag22 != flag5, flag22 != flag6, flag22 != flag7, flag22 != flag8, flag22 != flag9, flag22 != flag10, flag22 != flag11, flag22 != flag12, flag22 != flag13, flag22 != flag14, flag22 != flag15, flag22 != flag16, flag22 != flag17, flag22 != flag18, flag22 != flag19, flag22 != flag20, flag22 != flag21, flag22 != flag23, flag22 != flag24, flag22 != flag25, flag22 != flag26, flag22 != flag27, flag22 != flag28, flag22 != flag29, flag23 != flag0, flag23 != flag1, flag23 != flag2, flag23 != flag3, flag23 != flag4, flag23 != flag5, flag23 != flag6, flag23 != flag7, flag23 != flag8, flag23 != flag9, flag23 != flag10, flag23 != flag11, flag23 != flag12, flag23 != flag13, flag23 != flag14, flag23 != flag15, flag23 != flag16, flag23 != flag17, flag23 != flag18, flag23 != flag19, flag23 != flag20, flag23 != flag21, flag23 != flag22, flag23 != flag24, flag23 != flag25, flag23 != flag26, flag23 != flag27, flag23 != flag28, flag23 != flag29, flag24 != flag0, flag24 != flag1, flag24 != flag2, flag24 != flag3, flag24 != flag4, flag24 != flag5, flag24 != flag6, flag24 != flag7, flag24 != flag8, flag24 != flag9, flag24 != flag10, flag24 != flag11, flag24 != flag12, flag24 != flag13, flag24 != flag14, flag24 != flag15, flag24 != flag16, flag24 != flag17, flag24 != flag18, flag24 != flag19, flag24 != flag20, flag24 != flag21, flag24 != flag22, flag24 != flag23, flag24 != flag25, flag24 != flag26, flag24 != flag27, flag24 != flag28, flag24 != flag29, flag25 != flag0, flag25 != flag1, flag25 != flag2, flag25 != flag3, flag25 != flag4, flag25 != flag5, flag25 != flag6, flag25 != flag7, flag25 != flag8, flag25 != flag9, flag25 != flag10, flag25 != flag11, flag25 != flag12, flag25 != flag13, flag25 != flag14, flag25 != flag15, flag25 != flag16, flag25 != flag17, flag25 != flag18, flag25 != flag19, flag25 != flag20, flag25 != flag21, flag25 != flag22, flag25 != flag23, flag25 != flag24, flag25 != flag26, flag25 != flag27, flag25 != flag28, flag25 != flag29, flag26 != flag0, flag26 != flag1, flag26 != flag2, flag26 != flag3, flag26 != flag4, flag26 != flag5, flag26 != flag6, flag26 != flag7, flag26 != flag8, flag26 != flag9, flag26 != flag10, flag26 != flag11, flag26 != flag12, flag26 != flag13, flag26 != flag14, flag26 != flag15, flag26 != flag16, flag26 != flag17, flag26 != flag18, flag26 != flag19, flag26 != flag20, flag26 != flag21, flag26 != flag22, flag26 != flag23, flag26 != flag24, flag26 != flag25, flag26 != flag27, flag26 != flag28, flag26 != flag29, flag27 != flag0, flag27 != flag1, flag27 != flag2, flag27 != flag3, flag27 != flag4, flag27 != flag5, flag27 != flag6, flag27 != flag7, flag27 != flag8, flag27 != flag9, flag27 != flag10, flag27 != flag11, flag27 != flag12, flag27 != flag13, flag27 != flag14, flag27 != flag15, flag27 != flag16, flag27 != flag17, flag27 != flag18, flag27 != flag19, flag27 != flag20, flag27 != flag21, flag27 != flag22, flag27 != flag23, flag27 != flag24, flag27 != flag25, flag27 != flag26, flag27 != flag28, flag27 != flag29, flag28 != flag0, flag28 != flag1, flag28 != flag2, flag28 != flag3, flag28 != flag4, flag28 != flag5, flag28 != flag6, flag28 != flag7, flag28 != flag8, flag28 != flag9, flag28 != flag10, flag28 != flag11, flag28 != flag12, flag28 != flag13, flag28 != flag14, flag28 != flag15, flag28 != flag16, flag28 != flag17, flag28 != flag18, flag28 != flag19, flag28 != flag20, flag28 != flag21, flag28 != flag22, flag28 != flag23, flag28 != flag24, flag28 != flag25, flag28 != flag26, flag28 != flag27, flag28 != flag29, flag29 != flag0, flag29 != flag1, flag29 != flag2, flag29 != flag3, flag29 != flag4, flag29 != flag5, flag29 != flag6, flag29 != flag7, flag29 != flag8, flag29 != flag9, flag29 != flag10, flag29 != flag11, flag29 != flag12, flag29 != flag13, flag29 != flag14, flag29 != flag15, flag29 != flag16, flag29 != flag17, flag29 != flag18, flag29 != flag19, flag29 != flag20, flag29 != flag21, flag29 != flag22, flag29 != flag23, flag29 != flag24, flag29 != flag25, flag29 != flag26, flag29 != flag27, flag29 != flag28, 


    flag0 >= 0,
    flag1 >= 0,
    flag2 >= 0,
    flag3 >= 0,
    flag4 >= 0,
    flag5 >= 0,
    flag6 >= 0,
    flag7 >= 0,
    flag8 >= 0,
    flag9 >= 0,
    flag10 >= 0,
    flag11 >= 0,
    flag12 >= 0,
    flag13 >= 0,
    flag14 >= 0,
    flag15 >= 0,
    flag16 >= 0,
    flag17 >= 0,
    flag18 >= 0,
    flag19 >= 0,
    flag20 >= 0,
    flag21 >= 0,
    flag22 >= 0,
    flag23 >= 0,
    flag24 >= 0,
    flag25 >= 0,
    flag26 >= 0,
    flag27 >= 0,
    flag28 >= 0,
    flag29 >= 0,

    flag0 <= 255,
    flag1 <= 255,
    flag2 <= 255,
    flag3 <= 255,
    flag4 <= 255,
    flag5 <= 255,
    flag6 <= 255,
    flag7 <= 255,
    flag8 <= 255,
    flag9 <= 255,
    flag10 <= 255,
    flag11 <= 255,
    flag12 <= 255,
    flag13 <= 255,
    flag14 <= 255,
    flag15 <= 255,
    flag16 <= 255,
    flag17 <= 255,
    flag18 <= 255,
    flag19 <= 255,
    flag20 <= 255,
    flag21 <= 255,
    flag22 <= 255,
    flag23 <= 255,
    flag24 <= 255,
    flag25 <= 255,
    flag26 <= 255,
    flag27 <= 255,
    flag28 <= 255,
    flag29 <= 255,


    flag0 ^ 18 <= 63,
    flag1 ^ 43 <= 63,
    flag2 ^ 47 <= 63,
    flag3 ^ 5 <= 63,
    flag4 ^ 35 <= 63,
    flag5 ^ 44 <= 63,
    flag6 ^ 59 <= 63,
    flag7 ^ 17 <= 63,
    flag8 ^ 3 <= 63,
    flag9 ^ 21 <= 63,
    flag10 ^ 6 <= 63,
    flag11 ^ 43 <= 63,
    flag12 ^ 44 <= 63,
    flag13 ^ 37 <= 63,
    flag14 ^ 26 <= 63,
    flag15 ^ 42 <= 63,
    flag16 ^ 24 <= 63,
    flag17 ^ 34 <= 63,
    flag18 ^ 57 <= 63,
    flag19 ^ 14 <= 63,
    flag20 ^ 30 <= 63,
    flag21 ^ 5 <= 63,
    flag22 ^ 16 <= 63,
    flag23 ^ 23 <= 63,
    flag24 ^ 37 <= 63,
    flag25 ^ 49 <= 63,
    flag26 ^ 48 <= 63,
    flag27 ^ 16 <= 63,
    flag28 ^ 28 <= 63,
    flag29 ^ 49 <= 63,

    flag1 == 25,
    flag2 == 23,
    flag9 == 9,
    flag20 == 45,
    flag26 == 7,
    flag8 >= 15,
    flag12 <= 4,
    flag14 >= 48,
    flag29 >= 1,

    flag0 + flag1 + flag4 + flag2 + flag3 <= 140,
    flag0 + flag1 + flag4 + flag2 + flag3 >= 130,

    flag5 + flag6 + flag7 + flag8 + flag9 <= 150,
    flag5 + flag6 + flag7 + flag8 + flag9 >= 140,

    flag10 + flag11 + flag12 + flag13 + flag14 <= 160,
    flag10 + flag11 + flag12 + flag13 + flag14 >= 150,

    flag15 + flag16 + flag17 + flag18 + flag19 <= 170,
    flag15 + flag16 + flag17 + flag18 + flag19 >= 160,

    flag20 + flag21 + flag22 + flag23 + flag24 <= 180,
    flag20 + flag21 + flag22 + flag23 + flag24 >= 170,

    flag0 + flag5 + flag10 + flag15 + flag20 + flag25 <= 178,
    flag0 + flag5 + flag10 + flag15 + flag20 + flag25 >= 172,

    flag1 + flag6 + flag11 + flag16 + flag21 + flag26  <= 168,
    flag1 + flag6 + flag11 + flag16 + flag21 + flag26 >= 162,

    flag2 + flag7 + flag12 + flag17 + flag22 + flag27 <= 158,
    flag2 + flag7 + flag12 + flag17 + flag22 + flag27 >= 152,

    flag3 + flag8 + flag13 + flag18 + flag23 <= 148,
    flag3 + flag8 + flag13 + flag18 + flag23 >= 142,

    flag4 + flag9 + flag14 + flag19 + flag24 + flag29 <= 138,
    flag4 + flag9 + flag14 + flag19 + flag24 + flag29 >= 132,

    ((flag7 + (flag27*3)) * 3 - (flag5 * 13)) <= 85,
    ((flag7 + (flag27*3)) * 3 - (flag5 * 13)) >= 57,

    ((flag22 * 3) + (RotateLeft(flag14, 2) - (flag20 * 5))) - 12 <= 70,

    (flag13 + (((flag14 + (flag16 * 2)) * 2 + (flag15 - (flag18 * 2)) * 3) - flag17 * 5)) == 0,

    flag5 == (flag6*2),
    flag29 +flag7 == 59,
    flag0 == (flag17 * 6),
    flag8 == (flag9 * 4),
    RotateLeft(flag11, 1) == (flag13 * 3),
    flag13+flag29+flag11+flag4 == flag19,
    flag10 == (flag12 * 13)
)
while s.check() == sat:
    m = s.model()

    input = [m[flag0].as_long(), m[flag1].as_long(), m[flag2].as_long(), m[flag3].as_long(), m[flag4].as_long(), m[flag5].as_long(), m[flag6].as_long(), m[flag7].as_long(), m[flag8].as_long(), m[flag9].as_long(), m[flag10].as_long(), m[flag11].as_long(), m[flag12].as_long(), m[flag13].as_long(), m[flag14].as_long(), m[flag15].as_long(), m[flag16].as_long(), m[flag17].as_long(), m[flag18].as_long(), m[flag19].as_long(), m[flag20].as_long(), m[flag21].as_long(), m[flag22].as_long(), m[flag23].as_long(), m[flag24].as_long(), m[flag25].as_long(), m[flag26].as_long(), m[flag27].as_long(), m[flag28].as_long(), m[flag29].as_long()]
    checksum = calcChecksum(input)
    if checksum == m[flag28]:
        result = xor(input, [
            18,
            43,
            47,
            5,
            35,
            44,
            59,
            17,
            3,
            21,
            6,
            43,
            44,
            37,
            26,
            42,
            24,
            34,
            57,
            14,
            30,
            5,
            16,
            23,
            37,
            49,
            48,
            16,
            28,
            49
        ])
        print(encodeBase64Bytewise(result))
        break

    s.add(Or(flag0 != m[flag0].as_long(), flag1 != m[flag1].as_long(), flag2 != m[flag2].as_long(), flag3 != m[flag3].as_long(), flag4 != m[flag4].as_long(), flag5 != m[flag5].as_long(), flag6 != m[flag6].as_long(), flag7 != m[flag7].as_long(), flag8 != m[flag8].as_long(), flag9 != m[flag9].as_long(), flag10 != m[flag10].as_long(), flag11 != m[flag11].as_long(), flag12 != m[flag12].as_long(), flag13 != m[flag13].as_long(), flag14 != m[flag14].as_long(), flag15 != m[flag15].as_long(), flag16 != m[flag16].as_long(), flag17 != m[flag17].as_long(), flag18 != m[flag18].as_long(), flag19 != m[flag19].as_long(), flag20 != m[flag20].as_long(), flag21 != m[flag21].as_long(), flag22 != m[flag22].as_long(), flag23 != m[flag23].as_long(), flag24 != m[flag24].as_long(), flag25 != m[flag25].as_long(), flag26 != m[flag26].as_long(), flag27 != m[flag27].as_long(), flag28 != m[flag28].as_long(), flag29 != m[flag29].as_long())) # prevent next model from using the same assignment as a previous model

