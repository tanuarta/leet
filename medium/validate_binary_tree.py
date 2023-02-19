# https://leetcode.com/problems/validate-binary-search-tree/submissions/900877750
# Time Complexity = O(2n)

def __init__(self, val=0, left=None, right=None):
  self.val = val
  self.left = left
  self.right = right

def isValid(root, arr):
  if root == None:
    return arr

  arr = isValid(root.left, arr)

  arr.append(root.val)

  arr = isValid(root.right, arr)

  return arr

def isValidBST(root):
  arr = []

  res = isValid(root, arr)
  print(res)
  prev = 0
  for (i, num) in enumerate(res):
    if i == 0:
      prev = num
    elif prev >= num:
      return False
    prev = num
  
  return True
