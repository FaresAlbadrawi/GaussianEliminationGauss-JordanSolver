import time

# Store number of variables and equations in an array

def takeDs():
  time.sleep(1)
  eq = int(input("\nPlease enter the number of equations:")) #Rows
  vr = int(input("Please enter the number of variables:")) #Columns-1
  Ds = [eq,vr]
  return Ds