import time

#This function takes the array from the leading function : first element =1

# Make all elements under the leading equal zero

def zeros_UL(arr,n):
  for tR in range(1,len(arr)):
    x = -arr[tR][n]
    if x != 0:
      time.sleep(1)
      print(f"\nmultiply each element of the the first row by {x} and add it to the row number {tR+1}\n\nThe resulting agmented matrix:" )
      for i in range(len(arr[0])):
        arr[tR][i] = (arr[0][i]*x) + arr[tR][i]
      time.sleep(1)
      for i in range(len(arr)):
        print(arr[i])