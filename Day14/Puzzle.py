import math
Furthest = 0
HighScore = 0
RaceLength = 2503
ReindeerData = []
with open("Day14\Input.txt") as InputFile:
    for InputLine in InputFile:
        Name, _, _, Speed, _, _, Duration, _, _, _, _, _, _, Rest, _ = InputLine.split(' ')
        Speed = int(Speed)
        Duration = int(Duration)
        Rest = int(Rest)
        ReindeerData.append({'Speed': Speed, 'Duration': Duration, 'Rest': Rest, 'Distance': 0, 'Score': 0})

# Made obsolete by the second puzzle
#        Intervals = math.floor(RaceLength / (Duration + Rest))
#        Remainder = RaceLength - (Intervals * (Duration + Rest))
#
#        Distance = Intervals * Speed * Duration
#        if Remainder >= Duration:
#            Distance += Speed * Duration
#        else:
#            Distance += Speed * Remainder
#
#        if Distance > Furthest:
#            Furthest = Distance

for RaceTimer in range(RaceLength):
    for Index in range(len(ReindeerData)):
        Reindeer = ReindeerData[Index]
        Interval = Reindeer['Rest'] + Reindeer['Duration']
        if RaceTimer % Interval < Reindeer['Duration']:
            Reindeer["Distance"] += Reindeer["Speed"]
    FurthestIndex = 0
    for Index in range(1, len(ReindeerData)):
        if ReindeerData[Index]["Distance"] > ReindeerData[FurthestIndex]["Distance"]:
            FurthestIndex = Index
    ReindeerData[FurthestIndex]["Score"] += 1

for Reindeer in ReindeerData:
    if Reindeer["Distance"] > Furthest:
        Furthest = Reindeer["Distance"]
    if Reindeer["Score"] > HighScore:
        HighScore = Reindeer["Score"]

print(f'Puzzle 1: Distance Race = {Furthest}')
print(f'Puzzle 2: Scoring Race = {HighScore}')