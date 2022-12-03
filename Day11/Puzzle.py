def IncrementPasswordString(_Input):
    Input = list(_Input)
    for Index in reversed(range(len(Input))):
        if Input[Index] == 'z':
            Input[Index] = 'a'
        else:
            Input[Index] = chr(ord(Input[Index])+1)
            break
    return "".join(Input)

def FollowsRules(_Password):
    #No i o l
    Letters = set(_Password)
    if 'i' in Letters or 'o' in Letters or 'l' in Letters:
        return False

    #Triple Increment
    TripletFound = False
    for Index in range(len(_Password) - 2):
        Triplet = {ord(_Password[Index]), ord(_Password[Index + 1]) - 1, ord(_Password[Index + 2]) - 2}
        if len(Triplet) == 1:
            TripletFound = True
            break
    if not TripletFound:
        return False

    #Two Pairs
    PairsFound = False
    for Index1 in range(len(_Password) - 3):
        for Index2 in range(Index1 + 2, len(_Password) - 1):
            String1 = _Password[Index1:Index1+2]
            String2 = _Password[Index2:Index2+2]
            if String1[0] == String1[1] and String2[0] == String2[1] and String1 != String2:
                PairsFound = True
                break
    if not PairsFound:
        return False

    return True

Password1 = 'hepxcrrq'
while not FollowsRules(Password1):
    Password1 = IncrementPasswordString(Password1)

Password2 = IncrementPasswordString(Password1)
while not FollowsRules(Password2):
    Password2 = IncrementPasswordString(Password2)


print(f'Puzzle 1: First Password = {Password1}')
print(f'Puzzle 2: Second Password = {Password2}')