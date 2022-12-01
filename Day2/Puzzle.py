TotalPaper = 0
TotalRibbon = 0

with open("Day2\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip()
        w,h,l = InputLine.split('x')
        w = int(w)
        h = int(h)
        l = int(l)
        #Puzzle 1
        SquareFaces = 2*l*w + 2*w*h + 2*h*l
        ShortestEdge = min(l*w, w*h, h*l)
        TotalPaper += SquareFaces + ShortestEdge

        #Puzzle 2
        SmallestPerimiter = (w+h+l - max(w, h, l)) * 2
        PresentVolume = w*h*l
        print(w, h, l, SmallestPerimiter, PresentVolume)
        TotalRibbon += SmallestPerimiter + PresentVolume

print(f'Puzzle 1: Wrapping Paper = {TotalPaper}')
print(f'Puzzle 2: Ribbon = {TotalRibbon}') #Too high 255829436