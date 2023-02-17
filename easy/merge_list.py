# https://leetcode.com/problems/merge-two-sorted-lists
# Time Complexity = 0(n+m)

class Node:
  def __init__(self, data):
      self.val = data
      self.next = None

  def __repr__(self):
      return self.data

def merge(list1, list2):
  '''
  looper = list2
  
  while looper != None:
    print(looper.val)
    looper = looper.next
  '''

  if list1 == None:
    return list2
  elif list2 == None:
    return list1
    

  if list1.val <= list2.val:
    looper1 = list1
    head = list1
    looper2 = list2
  else:
    looper1 = list2
    head = list2
    looper2 = list1
    
  tmp = None
  prev = list2
  
  while looper1 != None:
    print(f'looper1 = {looper1.val}')
    print(f'first looper2 = {looper2.val}')
    
    if prev == None:
      break
     
    if looper1.next == None:
      looper1.next = looper2
      break
     
    if looper1.next.val >= looper2.val:
      tmp = looper1.next
      looper1.next = looper2
      looper1 = tmp
      print(f'next looper1 = {looper1.val}')
      
      while looper2 != None:
        print(f'looper2 = {looper2.val}')
        
        if looper2.next == None:
          prev = looper2.next
          looper2.next = looper1
          break
        
        if looper1 != None and looper2.next.val >= looper1.val:
          print(f'looper2.next = {looper2.next.val}')
          print('breaking')
          tmp = looper2.next
          looper2.next = looper1
          looper2 = tmp
          break
        else:
          looper2 = looper2.next
          
    else:
      looper1 = looper1.next

  return head

def main():
  head1 = Node(1)
  node1 = Node(2)
  node2 = Node(4)
  
  head1.next = node1
  node1.next = node2
      
  head2 = Node(5)
  
  '''
  node3 = Node(3)
  node4 = Node(4)
  
  head2.next = node3
  node3.next = node4
  '''
      
  res = merge(head2, head1)
  
  
  print('============== results =============')
  while res != None:
    print(res.val)
    res = res.next


if __name__ == "__main__":
  main()