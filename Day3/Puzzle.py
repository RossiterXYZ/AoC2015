Location = [{"x": 0, "y": 0}, {"x": 0, "y": 0}]
Parity = 0
Yr1HouseSet = {"0.0"}
Yr2HouseSet = {"0.0"}

with open("Day3\Input.txt") as InputFile:
    for InputLine in InputFile:
        for char in InputLine:
            Parity = (Parity + 1) % 2
            if char == "<":
                Location[Parity]["x"] -= 1
            if char == ">":
                Location[Parity]["x"] += 1
            if char == "^":
                Location[Parity]["y"] -= 1
            if char == "v":
                Location[Parity]["y"] += 1
            Yr1HouseSet.add(str(Location[1]["x"]+Location[0]["x"]) + '.' +  str(Location[1]["y"]+Location[0]["y"]))
            Yr2HouseSet.add(str(Location[Parity]["x"]) + '.' +  str(Location[Parity]["y"]))

print(f'Puzzle 1: Only Santa = {len(Yr1HouseSet)}')
print(f'Puzzle 2: RoboSanta = {len(Yr2HouseSet)}')