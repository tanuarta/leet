# https://leetcode.com/problems/linked-list-cycle-ii
# Time Complexity = O(n)


class Node:
  def __init__(self, data):
      self.val = data
      self.next = None

  def __repr__(self):
      return self.data


def cycle(head):
  looper = head
  
  nodeDict = {}
  
  while looper != None:
    if looper in nodeDict:
      return looper
  
    nodeDict[looper] = 1
    looper = looper.next

  return None

def main():
  head = Node(3)
  node1 = Node(2)
  node2 = Node(0)
  node3 = Node(-4)
  
  head.next = node1
  node1.next = node2
  node2.next = node3
  node3.next = node1
  
  res = cycle(head)


if __name__ == "__main__":
  main()