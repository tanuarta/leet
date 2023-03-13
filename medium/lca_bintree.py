# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# Time Complexity = O(n)

def lowestCommonAncestor(root, p, q):
  if root == None:
    return None

  if p.val > q.val:
    small = q
    big = p
  else:
    small = p
    big = q

  res = None

  if small.val <= root.val and big.val >= root.val:
    return root
  elif small.val <= root.val and big.val <= root.val:
    res = lowestCommonAncestor(root.left, small, big)
  elif small.val >= root.val and big.val >= root.val:
    res = lowestCommonAncestor(root.right, small, big)

  return res