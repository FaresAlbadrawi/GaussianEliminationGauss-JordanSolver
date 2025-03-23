import time

# The first element != 0 by interchanging rows

def arrangeMat(arr,nonz):
  if arr[0][nonz] == 0:
    for r in range(1,len(arr)):
      if arr[r][nonz] == 1:
        arr[0],arr[r] = arr[r], arr[0]
        time.sleep(1)
        print(f'\nTo make a leading we interchanged rows number 1 and {r+1}')
        time.sleep(1)
        print("\nThe augmented matrix after interchanging rows: ")
        for i in range(len(arr)):
          print(arr[i])
        return None
    for r in range(1,len(arr)):
      if arr[r][nonz] != 0:
        arr[0],arr[r] = arr[r], arr[0]
        time.sleep(1)
        print(f"\nTo make the first element of the nonzero column doesn't equal 0, we interchanged rows number 1 and {r+1}")
        time.sleep(1)
        print("\nThe augmented matrix after interchanging rows: ")
        for i in range(len(arr)):
          print(arr[i])
        return None
