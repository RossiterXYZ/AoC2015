import hashlib

PuzzleInput = 'bgvyzdsv'
Solved5 = False

for index in range(2_000_000):
    ConcatenatedString = PuzzleInput + str(index)
    md5 = hashlib.md5(ConcatenatedString.encode('ascii'))
    md5 = md5.hexdigest()
    if md5[:5] == "00000" and not Solved5:
        print(f'Puzzle 1: Five Zeroes = {index}')
        Solved5 = True
    if md5[:6] == "000000":
        print(f'Puzzle 2: Six! Zeroes = {index}')
        break