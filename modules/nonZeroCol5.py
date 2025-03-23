# Define the first non-zero column in the matrix

def nZeroCol(arr):
  for column in range(len(arr[0])):
    for row in range(len(arr)):
      if arr[row][column] != 0:
        return column



