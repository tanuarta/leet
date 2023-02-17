# https://leetcode.com/problems/reverse-linked-list
# Time Complexity: O(n)


class Node:
  def __init__(self, data):
      self.val = data
      self.next = None

  def __repr__(self):
      return self.data


def reverse(head):
  if head == None:
    return None

  looper = head
  nxt = None
  prev = None
  
  while looper.next != None:
    nxt = looper.next
    looper.next = prev
    prev = looper
    
    looper = nxt
    
  looper.next = prev
  
  return looper

def main():
  head1 = Node(1)
  node1 = Node(2)
  node2 = Node(4)
  
  head1.next = node1
  node1.next = node2
  
  res = reverse(head1)
  
  print('============== results =============')
  while res != None:
    print(res.val)
    res = res.next


if __name__ == "__main__":
  main()