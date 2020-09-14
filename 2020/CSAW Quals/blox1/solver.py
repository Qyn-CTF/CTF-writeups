board = {}

rxors = [3, 2, 3, 2, 2, 0, 1, 3, 1, 0, 0, 2, 2, 2, 2, 0, 3, 0, 1, 0, 0, 0, 0, 0]
rsums = [2, 2, 2, 2, 2, 3, 1, 2, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 1, 3, 0, 0, 0, 0]


NROWS = 20
NCOLS = 12

for y in range(NROWS):
    for x in range(NCOLS):
        board[y,x] = 0

def check_rows(blk):
    result = True

    for y in range(5):
        xor = 0
        sum = 0

        targetSum = rsums[blk * 5 + y]
        targetXor = rxors[blk * 5 + y]

        if targetSum == 3:
            for x in range(3):
                board[y + 0xf, x + blk * 3] = 1
        elif targetSum == 2:
            if targetXor == 1:
                board[y + 0xf, 1 + blk * 3] = 1
                board[y + 0xf, 2 + blk * 3] = 1
            elif targetXor == 2:
                board[y + 0xf, 0 + blk * 3] = 1
                board[y + 0xf, 2 + blk * 3] = 1
            elif targetXor == 3:
                board[y + 0xf, 0 + blk * 3] = 1
                board[y + 0xf, 1 + blk * 3] = 1
        elif targetSum == 1:
            board[y + 0xf, (targetXor - 1) + blk * 3] = 1

        for x in range(3):
            if (y + 0xf, x + blk * 3) in board and board[y + 0xf, x + blk * 3] != 0:
                xor ^= (x + 1)
                sum += 1
        
        if xor != rxors[blk * 5 + y] or sum != rsums[blk * 5 + y]:
            result = False
            break

    return result

for i in range(4):
    check_rows(i)

for y in range(NROWS):
    res = ""
    for x in range(NCOLS):
        if board[y,x] == 0:
            res += " "
        else:
            res += "X"
        res += " "
    print(res)