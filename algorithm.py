from typing import List

def saveToList():
  f = open("test.txt", "r")
  list_of_int = []
  lines = f.readlines()
  for line in lines:
    for c in line:
      if c.isdigit():
        list_of_int.append(format(c))
  f.close()
  return list_of_int





