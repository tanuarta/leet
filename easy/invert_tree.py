# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Time Complexity = O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
  if root == None:
    return root

  invertTree(root.left)
  invertTree(root.right)
  
  temp = root.right
  root.right = root.left
  root.left = temp
  
  return root

def main():
  head = TreeNode(2)
  node1 = TreeNode(1)
  node2 = TreeNode(3)
  
  head.left = node1
  head.right = node2
  
  res = invertTree(head)
  printTree(res)


def printTree(head):
  if head == None:
    return
  
  printTree(head.left)
  print(head.val)
  printTree(head.right)
  
  return
  

if __name__ == "__main__":
  main()