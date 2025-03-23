# After ensuring the system is valid

def takeEle(Dimentions):
  arr = []
  numOfEqu = Dimentions[0]
  numOfVar = Dimentions[1]
  for i in range(numOfEqu):
    row = []
    print("Equation number: ",i+1)
    for j in range(numOfVar):
      row.append(float(input(f'Enter coeffitient of variable number {j+1}: ')))
    row.append(float(input(f'Enter the absolute term: ')))
    arr.append(row)
  print("The augmanted matrix of your linear system:")
  for i in range(len(arr)):
    print(arr[i])
  return arr