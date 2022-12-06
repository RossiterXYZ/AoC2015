
def ScoreVariation(_Input, _Slots, _Calories = False):
    _Input.append(_Slots)
    Scoring = [0, 0, 0, 0, 0]
    Score = 1
    Index = 0
    IngredientIndex = 0

    for Entry in _Input:
        Scoring = [(Scoring[i]+Ingredients[IngredientIndex][i]*(Entry - Index)) for i in range(len(Scoring))]
        IngredientIndex += 1
        Index = Entry

    for Index in range(4):
        if _Calories and Scoring[4] != 500:
            Score = 0
        if Scoring[Index] < 1:
            Score = 0
        Score *= Scoring[Index]

    return Score

def FindGlobalMaximum(_IngredientCount, _Slots, _Calories = False):
    Variation = [0 for _ in range(_IngredientCount - 1)]
    MaxVariation = [_Slots for _ in range(_IngredientCount - 1)]

    #A really dense way of calculating non-overlapping sets, quite happy with this one.
    #I'd love to hear if you have a more concise solution. (That isn't an import.)
    Maximum = ScoreVariation(Variation.copy(), _Slots, _Calories)
    Index = 0
    while not Variation == MaxVariation:
        for Index in range(_IngredientCount - 1):
            if Index == _IngredientCount - 2:
                Variation[Index] += 1
            elif Variation[Index + 1] == 100:
                Variation[Index] += 1
            if Variation[Index] == 101:
                Variation[Index] = Variation[Index - 1]

        NewScore = ScoreVariation(Variation.copy(), _Slots, _Calories)
        if NewScore > Maximum:
            Maximum = NewScore
    return Maximum

Ingredients = []
with open("Day15\Input.txt") as InputFile:
    for InputLine in InputFile:
        Key, _, Capacity, _, Durability, _, Flavour, _, Texture, _, Calories = InputLine.split(' ')
        Ingredients.append([int(Capacity[:-1]), int(Durability[:-1]), int(Flavour[:-1]), int(Texture[:-1]), int(Calories[:-1])])

print(f'Puzzle 1: Best Cookie = {FindGlobalMaximum(len(Ingredients), 100, False)}')
print(f'Puzzle 2: Lite Cookie = {FindGlobalMaximum(len(Ingredients), 100, True)}')