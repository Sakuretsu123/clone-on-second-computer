#!python3
import time
""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
  c = 0 
  a1 = a
  b1 = b
  i = 0
  p = 0
  m = 0
  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """

    
 
  myList = []
 
  myList.append(str(a))
  myList.append(str(b))

  
  while True:
      time.sleep(0.1)
      c = int(a) + int(b) 
      if a == a1 and b == b1 and i != 0: 
        print(myList)
        m = str(''.join(myList))
        break
      if c < 10 : 
        myList[p]
        myList.append(str(c))
        print(myList)
        a = myList[-2]
        b = myList[-1]
        a = int(a)
        b = int(b)
        i += 1
      elif c >= 10: 
        i += 1
        c = str(c)
        a = c[0]
        b = c[1]
        a = int(a)
        b = int(b)

  return m






def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
  
#omg it worked so proud 