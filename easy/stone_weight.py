# https://leetcode.com/problems/last-stone-weight
# Time Complexity = O(n)

import heapq


def lastStoneWeight(stones):
  
  for i, num in enumerate(stones):
    stones[i] *= -1 
  
  heapq.heapify(stones)
  
  while len(stones) > 1:
    num1 = heapq.heappop(stones)
    num2 = heapq.heappop(stones)
  
    if num1 - num2 != 0:
      heapq.heappush(stones, num1 - num2)
  
  if stones:
    return -stones[0]
  else:
    return 0

def main():
  stones = [2]

  print(lastStoneWeight(stones))

if __name__ == "__main__":
  main()