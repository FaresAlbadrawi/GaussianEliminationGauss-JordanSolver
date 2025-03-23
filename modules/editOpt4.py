# Replace a row defined by the user

def editOpt(arr):
  badR = int(input("\nThe equation you want to edit is the equation number: "))
  while badR < 1 or badR > len(arr):
    print("\nWrong input! Try again.")
    badR = int(input("\nThe equation you want to edit is the equation number: "))
  print("\nEquation number: ",badR,"\n")
  newR = []
  for j in range(len(arr[0])-1):
    newR.append(float(input(f'Enter coeffitient of variable number {j+1}: ')))
  newR.append(float(input(f'Enter the absolute term: ')))
  arr[badR-1] = newR
  print("\nThe augmented matrix after replacing the equation: ")
  for i in range(len(arr)):
    print(arr[i])


