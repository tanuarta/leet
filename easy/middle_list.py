# https://leetcode.com/problems/middle-of-the-linked-list
# Time Complexity = 0(n)

import math

class Node:
  def __init__(self, data):
      self.val = data
      self.next = None

  def __repr__(self):
      return self.data


def middle(head):
  counter = 1
  looper = head
  
  nodeDict = {}
  
  while looper != None:
    nodeDict[counter] = looper
    counter += 1
    looper = looper.next
  
  return nodeDict[math.ceil(counter/2)]
  

def main():
  head = Node(1)
  node1 = Node(2)
  node2 = Node(4)
  
  head.next = node1
  node1.next = node2
  
  res = middle(head)
  
  
  print('============== results =============')
  while res != None:
    print(res.val)
    res = res.next


if __name__ == "__main__":
  main()