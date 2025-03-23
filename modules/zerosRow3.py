#searching for a zeros row

def zerosRow(arr):
  zRow = False
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j] == 0:
        zRow = True
      else:
        zRow = False
        break
    if zRow == True:
      return zRow