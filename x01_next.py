#!python3

"""
There are 2 important pieces of data that are going to be used for this assignment:
curValue : (an integer)
data: a List that specifies whether the item should be skipped or not
False indicates it should be skipped, True indicates it should not be skipped.

Create a funtion that receives 2 input paramters, the curValue and the list Data
Return the index of the next item to be used
"""

def next(current , myList):
  '''
  determine the next item from the list. The list contains False/True Boolean values
  that indicate whether the current item can be used
  '''



  #current = base = int(input("item from the list : "))
  #myList = [False, True, False, True, True, False]
  base = current

  result = myList.count(True)

  while True : 
    if current >= len(myList): 
      current = 0 
    elif result == 0: 
      return None
    elif myList[current] is True and current == base:
      current +=1
    elif myList[current] is False : 
      current += 1 
    elif myList[current] is True: 
      print(current)
      break
    result = myList.count(True)
    
   
  return current
  




def main():
  data = [False, True, True, False, True, False]
  assert next( 3 , data ) == 4
  assert next( 4 , data ) == 1
  assert next( 1 , data ) == 2
  data = [True, True, False, False, True, False, True]
  assert next( 1 , data ) == 4
  assert next( 6 , data ) == 0
  assert next( 0 , data ) == 1
  assert next( 3 , data ) == 4
  data = [True, True, False]
  assert next( 1 , data ) == 0
  assert next( 0 , data ) == 1
  data = [False, False, False]
  assert next( 1, data ) == None
  

  
  
  
  
main()