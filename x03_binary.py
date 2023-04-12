#!python3

"""
Create a function that takes an integer value from 0-255 and
converts it into a list.  Each element is equal to the power
of 2 that corresponds to that place value
"""

def toBinary(value):
  '''
  input: value (int)
  return : list of values
  '''
  c= 0
  myList = []
  while len(myList) != 8:
    c += 1
    if value >= 1:
      if value%2 == 0:
          myList.append(0)
      if value%2 != 0:
          myList.append(1)
    value = value // 2
    if value < 1: 
      myList.append(0)
  print(myList)
  
  try :
    if len(myList) != 8:
      myList.remove[8]
  except : 
    print(myList)
      



  
  return myList

def toDecimal(myList):
  c = 0
  decimal = 0
  for i in myList :
    if i == 0: 
      c +=1
    if i == 1:
      decimal = decimal + pow(2, c)
      c += 1
    


  '''
  input: list of values
  return int
  convert binary to decimal
  '''
  return decimal

def problem1():
  assert toBinary(0) == [0,0,0,0,0,0,0,0]
  assert toBinary(1) == [1,0,0,0,0,0,0,0]
  assert toBinary(2) == [0,1,0,0,0,0,0,0]
  assert toBinary(5) == [1,0,1,0,0,0,0,0]
  assert toBinary(10) == [0,1,0,1,0,0,0,0]
  assert toBinary(30) == [0,1,1,1,1,0,0,0]
  assert toBinary(45) == [1,0,1,1,0,1,0,0]

def problem2():
  assert toDecimal([0,0,0,0,0,0,0,0]) == 0
  assert toDecimal([1,0,0,0,0,0,0,0]) == 1
  assert toDecimal([0,1,0,0,0,0,0,0]) == 2
  assert toDecimal([1,0,1,0,0,0,0,0]) == 5
  assert toDecimal([0,1,0,1,0,0,0,0]) == 10
  assert toDecimal([0,1,1,1,1,0,0,0]) == 30
  assert toDecimal([1,0,1,1,0,1,0,0]) == 45
  
if __name__ == "__main__":
  problem1()
  problem2()
