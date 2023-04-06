class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def func(head):
  return

def main():
  head = Node(1)
  node1 = Node(2)
  node2 = Node(4)
  
  head.next = node1
  node1.next = node2
  
  res = func(head)
  
  
  print('============== results =============')
  while res != None:
    print(res.val)
    res = res.next


if __name__ == "__main__":
  main()