# https://leetcode.com/problems/first-bad-version
from math import floor

def isBadVersion(n):
  if n >= 3:
    return True
  else:
    return False


def binary_search(n):
  res = floor(n / 2)
  tmp = 1
  check = 0
  
  if isBadVersion(n) and not isBadVersion(n-1):
    return n
  
  while check == 0:
    if isBadVersion(res):
      if not isBadVersion(res - 1):
        return res
      n = res
      res = floor((tmp + res) / 2)
    else:
      tmp = res
      res = floor((res + n) / 2)
  
  return res

def main():
  num = 3
  print(binary_search(num))

if __name__ == "__main__":
  main()