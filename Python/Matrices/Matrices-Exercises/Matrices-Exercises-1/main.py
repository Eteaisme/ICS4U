canadianFRCTeams = ["865", "610", "2056"]
americanFRCTeams = ["254", "2910", "4414"]

FRCTeams = [canadianFRCTeams, americanFRCTeams]

for i in range(len(FRCTeams)):
    for j in range(len(FRCTeams[i])):
        print(FRCTeams[i][j], end = " ")
    print("")



print("")
timesTable = [([0] * 12) for i in range(12)]

for i in range (12):
    for j in range (12):
        timesTable[i][j] = ((i+1)*(j+1))
        

for i in range(len(timesTable)):
    for j in range(len(timesTable[i])):
        print(timesTable[i][j], end = " ")
    print("")