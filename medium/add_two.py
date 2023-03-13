# https://leetcode.com/problems/add-two-numbers
# Time Complexity = O(n+m)

class Node:
  def __init__(self, data):
      self.val = data
      self.next = None

  def __repr__(self):
      return self.data


def addTwoNumbers(head, head2):

  size1 = 0
  looper = head
  while looper != None:
    size1 += 1
    looper = looper.next
    
  size2 = 0
  looper = head2
  while looper != None:
    size2 += 1
    looper = looper.next

  if size1 >= size2:
    looper1 = head
    looper2 = head2
  else:
    looper1 = head2
    looper2 = head
    
  marker = 0
  looperRes = None
  res = None
  while looper2 != None:
    print(f'===== looper1 = {looper1.val} and looper2 = {looper2.val} =====')
  
    num = looper1.val + looper2.val + marker
    marker = 0
    
    print(f'num = {num}')
    
    if num > 9:
      marker = 1
      digit = int(str(num)[-1])
      if res == None:
        res = Node(digit)
        looperRes = res
      else:
        looperRes.next = Node(digit)
        looperRes = looperRes.next
    else:
      if res == None:
        res = Node(num)
        looperRes = res
      else:
        looperRes.next = Node(num)
        looperRes = looperRes.next
      
    looper1 = looper1.next
    looper2 = looper2.next
    
  print(res.val)

  while looper1 != None:
    num = looper1.val + marker
    marker = 0
    if num > 9:
      marker = 1
      digit = int(str(num)[-1])
      if looperRes == None:
        looperRes = Node(digit)
      else:
        looperRes.next = Node(digit)
        looperRes = looperRes.next
    else:
      if res == None:
        res = Node(num)
        looperRes = res
      else:
        looperRes.next = Node(num)
        looperRes = looperRes.next
      
      
    looper1 = looper1.next

  if marker == 1:
    looperRes.next = Node(1)
    looperRes = looperRes.next

  return res

def main():
  head = Node(9)
  node1 = Node(9)
  node2 = Node(9)
  
  head.next = node1
  node1.next = node2
  
  head2 = Node(9)
  node3 = Node(9)
  node4 = Node(9)
  node5 = Node(9)
  node6 = Node(9)
  
  head2.next = node3
  node3.next = node4
  node4.next = node5
  node5.next = node6
  
  res = addTwoNumbers(head, head2)
  
  print('============== results =============')
  while res != None:
    print(res.val)
    res = res.next


if __name__ == "__main__":
  main()

