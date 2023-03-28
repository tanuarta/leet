import math

def searchRange(nums, target):
  index = round(len(nums) / 2)
  top = len(nums) - 1
  bottom = 0
  
  lowestIndex = -1
  highestIndex = -1
  prevNum = -1
  found = 0

  if not nums: return [-1, -1]

  if nums[0] == target:
    lowestIndex = 0
  else:
    while True:
      if nums[index] < target:
        bottom = index
      elif nums[index] > target:
        top = index
      elif nums[index] == target:
        found = 1
        if lowestIndex == index:
          break
        lowestIndex = index
        top = index
      
      index = math.ceil((bottom + top) / 2)
      if prevNum == index and found == 0:
        return [-1, -1]
      else:
        prevNum = index
  
  top = len(nums) - 1
  bottom = 0
  
  if nums[-1] == target:
    highestIndex = len(nums) - 1
  else:
    while True:
      if nums[index] < target:
        bottom = index
      elif nums[index] > target:
        top = index
      elif nums[index] == target:
        if highestIndex == index:
          break
        highestIndex = index
        bottom = index
      
      index = math.floor((bottom + top) / 2)
  
  return [lowestIndex, highestIndex]

def main():
  nums = [1,2,3]
  target = 2


  print(searchRange(nums, target))

if __name__ == "__main__":
  main()