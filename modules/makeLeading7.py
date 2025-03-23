import time

# This function takes an array whom first element != 0 and != 1

# Make the first element equals one if it doesn't

# The law used to make this happen is:
# Mutiplying the whole row by the multipicative inverse of the first element

def makeL(arr,n):
  bLeading = arr[0][n]
  if bLeading !=1:
    time.sleep(1)
    print("\nMake a leading in the row by mutiplying the whole row by the multipicative inverse of the first element")
    for i in range(len(arr[0])):
      arr[0][i] *= 1/bLeading
    time.sleep(1)
    print("\nThe augmented matrix:")
    for i in range(len(arr)):
      print(arr[i])