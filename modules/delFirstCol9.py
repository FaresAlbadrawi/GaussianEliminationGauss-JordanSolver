# Move the first column from the old matrix to a new one to repeat the steps

def delFirstCol(old,new):
  print("\nMove the first row from the main matrix to another matrix and repeat the steps if possible")
  new.append(old.pop(0))
