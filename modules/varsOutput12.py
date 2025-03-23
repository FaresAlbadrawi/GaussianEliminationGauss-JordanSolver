import time

#Extract variables value from the matrix

def varsOutput(newArr):
  time.sleep(1)
  print("\nThe variables values:")
  for i in range(len(newArr)):
    time.sleep(1)
    print(f'X{i+1} = {round(newArr[i][len(newArr[i])-1],2)}')
  time.sleep(1)
  return 'Done!'

