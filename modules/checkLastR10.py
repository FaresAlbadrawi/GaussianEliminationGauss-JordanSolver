# This function takes the final output when the augMatrix is empty and the newMat is full

# 0 = "There's no solution!"
# 1 = "There's a solution!"
# 2 = "There are infinity solutions!"

#Checking the last row 

def check_LR(newArr):
  if newArr[len(newArr)-1][len(newArr[0])-2] == newArr[len(newArr)-1][len(newArr[0])-1] == 0 :
    return 2
  elif newArr[len(newArr)-1][len(newArr[0])-2] == 0 and newArr[len(newArr)-1][len(newArr[0])-1] != 0 :
    return 0
  else:
    return 1