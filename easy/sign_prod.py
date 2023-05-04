# https://leetcode.com/problems/sign-of-the-product-of-an-array
# Time Complexity = O(n)


def arraySign(nums):
  sign = 0

  for num in nums:
    if num == 0:
      return 0  
    elif num < 0:
      sign += 1

  if sign % 2 == 0:
    return 1
  else:
    return -1

def main():
  nums = [-1,-2,-3,-4,3,2,1]

  print(arraySign(nums))

if __name__ == "__main__":
  main()