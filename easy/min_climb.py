# https://leetcode.com/problems/min-cost-climbing-stairs
# O(n)

def minCostClimbingStairs(cost):
  end = len(cost)
  costDict = {}

  start = 0

  while start != end:
    if start == 0:
      costDict[start] = cost[start]
    elif start == 1:
      costDict[start] = cost[start]
    elif costDict[start - 1] + cost[start] < costDict[start - 2] + cost[start]:
      costDict[start] = costDict[start - 1] + cost[start]
    else:
      costDict[start] = costDict[start - 2] + cost[start]
    
    start += 1
      
  if costDict[start - 1] < costDict[start - 2]:
    return costDict[start - 1]
  else:
    return costDict[start - 2]

def main():
  cost = [1,100,1,1,1,100,1,1,100,1]

  print(minCostClimbingStairs(cost))

if __name__ == "__main__":
  main()