import time
# Store number of variables and equations in an array
from modules.takeDimensions1 import takeDs
# Take system elements from the user
from modules.takeElements2 import takeEle
# Searching for a zeros row
from modules.zerosRow3 import zerosRow
# Replace a row defined by the user
from modules.editOpt4 import editOpt
# Define the first non-zero column in the matrix
from modules.nonZeroCol5 import nZeroCol
# Make the first element != 0 by interchanging rows
from modules.arrangingMatrixR6 import arrangeMat
# Make the first element equals one if it doesn't
from modules.makeLeading7 import makeL
# Make all elements under the leading equal zero
from modules.zerosUnderLeading8 import zeros_UL
# Move the first column from the old matrix to a new one to repeat the steps
from modules.delFirstCol9 import delFirstCol

#After repeating the previous 5 steps to all rows, the old matrix becomes empty and the new matrix is full

#Checking the last row 
from modules.checkLastR10 import check_LR

# If the last row is valid do the gauss-jordan

# Make all elements Above the leading equal zero
from modules.zerosAboveLeading11 import zeros_AL
#Extract variables value from the matrix
from modules.varsOutput12 import varsOutput


def solve():
  Ds = augMatrix = newMat = []
  print("\nWelcome to my project. I hope you enjoy the experience.")
  tAgain = 'y'
  while tAgain == 'y':
    Ds = takeDs()
    if Ds[0] < Ds[1]: #Equations less than variables.
      print('\nRejected System: The variables are more than the equations')
      tAgain = input("\nIf you want to try again, please enter y. If not enter any other key: ")
      if tAgain == 'y':
        continue
      else:
        return '\nThanks for your time!'
    else:
      augMatrix = takeEle(Ds)
      if zerosRow(augMatrix) == True:
        print("\nZeros row is found. Try again..")
      
      else:
        change = input('\nIf you want to change anything, please enter y: ')
        if change != 'y':
          tAgain = 0
        while change == 'y':
          editRes = input('\nTo edit a specific equation enter e. To reset and return to the start enter r: ')
          if editRes == 'e':
            editOpt(augMatrix)
            tAgain = 0
            change = input('\nIf you want to change anything, please enter y: ')
          elif editRes == 'r':
            augMatrix.clear()
            Ds.clear()
            print("\nThe system is cleared! Try again..")
            tAgain = 'y'
            change = 0
          else:
            change = 0
            tAgain = 0

  while augMatrix != [] :
    if zerosRow(augMatrix) == True:
      time.sleep(1)
      return "\nThere are infinity solutions!"
    time.sleep(1)
    print("\nThe augmented matrix to solve:")
    for i in range(len(augMatrix)):
      print(augMatrix[i])
    n = nZeroCol(augMatrix)
    arrangeMat(augMatrix,n)
    makeL(augMatrix,n)
    zeros_UL(augMatrix,n)
    time.sleep(1)
    delFirstCol(augMatrix,newMat)
  time.sleep(1)
  print("\nThe matrix in the row-echlon form:")
  for i in range(len(newMat)):
    print(newMat[i])
  
  if check_LR(newMat) == 0:
    time.sleep(1)
    return "\nThere's no solution!"
  elif check_LR(newMat) == 2:
    time.sleep(1)
    return "\nThere are infinity solutions!"
  else:
    zeros_AL(newMat)
    return varsOutput(newMat)

print(solve())