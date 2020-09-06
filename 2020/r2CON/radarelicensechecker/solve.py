from subprocess import Popen, PIPE
from string import printable
import re
currentFlag = ""
flagLength = 34


def getOutput(input):
    try:
        process = Popen(["radarelicensechecker.exe", input + (flagLength - len(input)) * "A"], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        match = re.search(rb"ERROR: decryption error in block (\d+)", output)
        return int(match.groups(1)[0].decode())
    except:
        return -1

for i in range(len(currentFlag), flagLength):
    for char in printable:
        output2 = getOutput(currentFlag + char)
        if output2 != i:
            currentFlag += char
            print(f"\r[{len(currentFlag)}] {currentFlag}", end="")
            break
if len(currentFlag) == flagLength:
    print(f"\r[{len(currentFlag)}] FOUND FLAG: {currentFlag}")
else:
    print("Failed :(")