def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print("")
myMatrix = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
matrix_print(myMatrix)