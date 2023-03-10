# https://leetcode.com/problems/top-k-frequent-words
# Time Complexity = nLog(n)

def topKFrequent(words, k):
  stringDict = {}
  
  for string in words:
    if string in stringDict:
      stringDict[string] += 1
    else:
      stringDict[string] = 1
  
  
  #sorted(footballers_goals.items(), key=lambda x:x[1])
  print(stringDict)
  stringDict = sorted(stringDict.items(), key=lambda x: (-x[1], x[0]))
  print(stringDict)
  
  res = []
  
  for i in range(0, k):
    res.append(stringDict[i][0])
  
  return res

def main():

  words = ["i","love","leetcode","i","love","coding"]
  k = 3

  print(topKFrequent(words, k))

if __name__ == "__main__":
  main()