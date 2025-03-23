import time

# If the last row is valid do the gauss-jordan

# INPUT: a matrix in row-echlon form
# OUTPUT: a matrix in reduced row-echlon form

# Make all elements Above the leading equal zero

def zeros_AL(newArr):
  for lRow in range(len(newArr)-1,0,-1):
    for tR in range(lRow):
      x = -newArr[tR][lRow]
      if x != 0:
        time.sleep(1)
        print(f"\nmultiply each element of the row number {lRow+1} by {x} and add it to the row number {tR+1}\n\nThe resulting agmented matrix:")
        for i in range(len(newArr[0])):
          newArr[tR][i] = (newArr[lRow][i]*x) + newArr[tR][i]
        time.sleep(1)
        for i in range(len(newArr)):
          print(newArr[i])
