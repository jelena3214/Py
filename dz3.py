def rotateMatrix(n, tempmatrix):
    for i in range(n):
        for j in range(i):
            tempmatrix[i][j], tempmatrix[j][i] = tempmatrix[j][i], tempmatrix[i][j]
    for i in range(n):
        for j in range(n//2):
            tempmatrix[i][j], tempmatrix[i][n-j-1] = tempmatrix[i][n-j-1], tempmatrix[i][j]
    return tempmatrix
def inP():
    dimensions = list(map(lambda x: int(x), input().split()))
    if dimensions[0] != dimensions[1]: quit()
    rotation = int(input())
    if rotation != 90 and rotation != 180 and rotation != 270: quit()
    return dimensions, rotation
def readMatrix(n):
    tmatrix = []
    for i in range(n):
        a = list(map(lambda x: int(x), input().split()))
        tmatrix.append(a)
    return tmatrix
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix) - 1 != i:
                print(matrix[i][j], end=" " if j != len(matrix[i]) - 1 else "\n")
            else:
                print(matrix[i][j], end=" " if j != len(matrix[i]) - 1 else "")
def rot(rotation):
    if rotation == 90:
        printMatrix(rotateMatrix(matrixDimension, matrix))
    elif rotation == 180:
        a = rotateMatrix(matrixDimension, matrix)
        printMatrix(rotateMatrix(matrixDimension, a))
    else:
        a = rotateMatrix(matrixDimension, matrix)
        b = rotateMatrix(matrixDimension, a)
        printMatrix(rotateMatrix(matrixDimension, b))
dimensions, rotation = inP()
matrixDimension = dimensions[0]
matrix = readMatrix(matrixDimension)
rot(rotation)