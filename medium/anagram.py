# https://leetcode.com/problems/find-all-anagrams-in-a-string


def findAnagrams(s, p):
  start = 0
  end = len(p) - 1
  res = []
  
  if len(s) < len(p):
    return res
  
  charDict = {}
  
  for char in p:
    if char in charDict:
      charDict[char] += 1
    else:
      charDict[char] = 1
  
  for i in range(start, end + 1):
    if s[i] in charDict:
      charDict[s[i]] -= 1
  
  print(charDict)
  
  check = 1
  
  for key in charDict:
    if charDict[key] != 0:
      check = 0
      
  if check == 1:
    res.append(start)
  
  if s[start] in charDict:
    charDict[s[start]] += 1
      
  start += 1
  
  end += 1
  if end != len(s) and s[end] in charDict:
    charDict[s[end]] -= 1
  
  while end != len(s):
    print(f'start = {start} end = {end}')
    print(charDict)
      
    check = 1
    for key in charDict:
      print(f'{key} is {charDict[key]}')
      if charDict[key] != 0:
        check = 0
    
    if check == 1:
      print(f'added = {start}')
      res.append(start)
        
    if s[start] in charDict:
      charDict[s[start]] += 1    
    start += 1
    
    end += 1
    if end != len(s) and s[end] in charDict:
      charDict[s[end]] -= 1

  return res

def main():
  s = "abaacbabc"
  p = "abc"
  print(findAnagrams(s, p))

if __name__ == "__main__":
  main()