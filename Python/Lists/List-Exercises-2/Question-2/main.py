def lockerProblem(numberOfLockers):
    currentStudentLockers = []
    totalStudentLockers = []
    for i in range (int(numberOfLockers)):
        currentStudentLockers.append(i)
        totalStudentLockers += currentStudentLockers

    return totalStudentLockers
    

print(lockerProblem(1000))