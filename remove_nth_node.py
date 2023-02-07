# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# 31ms Runtime, 14mb Memory
# Time Complexity = O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

def sol(head, n):
  prevNode = None
  nextNode = None
  nodeToRemove = None
  
  looper = head
  counter = 0
  
  while looper != None:
    if prevNode != None:
      prevNode = prevNode.next
      
    if nodeToRemove != None:
      nodeToRemove = nodeToRemove.next
      
    if nextNode != None:
      nextNode = nextNode.next

    if counter == n - 1:
      nextNode = head
    if counter == n:
      nodeToRemove = head
    if counter == n + 1:
      prevNode = head
  
    looper = looper.next
    counter += 1

  if nodeToRemove != None:
    nodeToRemove = nodeToRemove.next
  
  if nextNode != None:
    nextNode = nextNode.next

  if prevNode == None and nodeToRemove != head:
    prevNode = head
  elif prevNode != None:
    prevNode = prevNode.next
  
  if counter == 1:
    return None
    
  if nodeToRemove == None:
    head = head.next
  elif prevNode == None:
    head.next = None
  else:
    prevNode.next = nextNode
  return head
    
def main():
  prev = None
  head = Node(-1)
  for n in range(10):
    if n == 0:
      node = Node(n)
      head.next = node
      prev = node
    else:
      node = Node(n)
      prev.next = node
      prev = node
      
  loop = head
  
  res = sol(head, 2)
  
  loop = res
  
  while loop != None:
    print(loop.data)
    loop = loop.next

if __name__ == '__main__':
  main()