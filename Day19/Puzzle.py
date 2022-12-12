def ParseFile(_File):
    DataFile = {'Substitutions': [], 'Molecule': []}
    with open(_File) as InputFile:
        TmpData = [Individual for Individual in InputFile.read().strip().split("\n")]
        for Index in range(len(TmpData)):
            if TmpData[Index] == '':
                DataFile["Molecule"].append(TmpData[Index+1])
                return DataFile
            DataFile["Substitutions"].append(TmpData[Index].split(" => "))

def RunMachine(_Data):
    DistinctMolecules = set()
    for MoleculeIndex in range(len(_Data["Molecule"])):
        MoleculeString = _Data["Molecule"][MoleculeIndex]
        for BaseIndex in range(len(MoleculeString)):
            for SubIndex in range(len(_Data["Substitutions"])):
                SubText = _Data["Substitutions"][SubIndex][0]
                if SubText == MoleculeString[BaseIndex:BaseIndex+len(SubText)]:
                    DistinctMolecules.add(f'{MoleculeString[:BaseIndex]}{_Data["Substitutions"][SubIndex][1]}{MoleculeString[BaseIndex+len(SubText):]}')
    return DistinctMolecules

def BuildCompound(_Data, _Target): #TODO BUILD IT BACKWARDS
    LocalData = _Data.copy()
    Count = 0
    while Count < 100 and not _Target in LocalData["Molecule"]:
        Output = list(RunMachine(LocalData))
        for Index in reversed(range(len(Output))):
            if len(Output[Index]) > len(_Target):
                Output.pop(Index)
        LocalData["Molecule"] = list(Output)
        Count += 1
        print(Count, len(LocalData["Molecule"]))

    return [Count, LocalData["Molecule"]]

TrainingData = ParseFile("Day19\Input.txt")

Part1 = len(RunMachine(TrainingData))

print("Warning! Part 2 Never Terminates")
TargetData = TrainingData["Molecule"][0]
TrainingData["Molecule"] = ['e']
Part2 = BuildCompound(TrainingData, TargetData)

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}')