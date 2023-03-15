# https://leetcode.com/problems/two-sum
# Time Complexity = O(nlogn)

from math import ceil

def twoSum(nums, target):
  numDict = {}
  x = 0
  for i, num in enumerate(nums):
    if num in numDict:
      if num * 2 == target:
        return [i, numDict[num]]
    else:
      numDict[num] = x
    x += 1
  
  for i, number in enumerate(nums):
    difference = target - number
    if difference in numDict and i != numDict[difference]:
      return [i, numDict[difference]]
    
    
def main():
    num_list = [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1]
    print(twoSum(num_list, 11))

if __name__ == "__main__":
    main()
    
    


    
# Initial Idea

# 1. Sort nums - (merge sort) O(nlogn)
# 2. Iterate through sorted nums
# 3. For each number, find the difference with target sum, and do a binary search. If found, then the pair is found - O(nlogn)
# Time complexity = nlog(n) + nlog(n) = O(nlogn)

# I then realised an issue, because I sort the list, I don't have the original indices of the numbers
# so although I the correct numbers, I couldn't create an output.

# This resulted in the complete idea

# 1. Make dictionary from list - O(n)
# 2. Iterate through sorted nums - O(n)
# 3. For each number, calculate difference and dictionary lookup the difference. If found then the pair is found. - O(1)
# Time complexity = n + n = O(2n)

# Complication with duplicates
# Since the only time duplicates are useful is IF the duplicate is the twosum
# We check if the sum of the duplicate is the solution when it comes up, if it doesn't we ignore the duplicate
    
# ===================================================== Archived ===================================================
# Do a binary search on a list and return the index of the target
def binarySearch(list, target):
  bottom_index = 0
  top_index = len(list) - 1
  found = 0

  while (found == 0):
    if bottom_index == top_index:
      return -1
  
    middle_index = ceil((top_index + bottom_index) / 2) # Get middle index
    if list[middle_index] == target:
      found = 1
    
    if list[middle_index] < target:
      bottom_index = middle_index
    else:
      top_index = middle_index
  
  return middle_index