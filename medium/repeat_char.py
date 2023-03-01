# https://leetcode.com/problems/longest-repeating-character-replacement
# Time Complexity = O(26n) = O(n)

import time

def characterReplacement(s, k):
  strLength = len(s)
  start = 0
  end = 0
  res = 1
  charDict = {}
  
  while end != strLength:
    if s[end] in charDict:
      charDict[s[end]] += 1
    else:
      charDict[s[end]] = 1
    
    mostCharNum = max(charDict.values())
    
    if end - start + 1 - mostCharNum > k:
      charDict[s[start]] -= 1
      end += 1
      start += 1
    else:
      if end - start + 1 > res:
        res = end - start + 1
    
      end += 1

  return res

def main():
  s = 'KJRGKSKKOKLPADMAGODEDNEBMJMKGAPNLSAKADRLHHDRMJTMFBSIQGHENKABISHQNRFJKEPMFIPNDNEOBRJEHFLIHMDLMCIHLHQN'
  k = 5
    
  print(characterReplacement(s, k))

if __name__ == "__main__":
  main()
  
  
# Solution not using inbuilt MAX() function to calculate the max value in a dictionary
# Was confused what was wrong with my algorithm because I thought there was no further optimisation. Thought I was dumb :()
# It turns out I was dumb and there was a built in method to calculate what I manually did

def characterReplacementOLD(s, k):
  strLength = len(s)
  start = 0
  end = 0
  res = 1
  charDict = {}
  
  while end != strLength:
    if s[end] in charDict:
      charDict[s[end]] += 1
    else:
      charDict[s[end]] = 1
    
    mostCharNum = 0
    mostChar = ''
    totalDict = 0
    
    for key in charDict:
      if charDict[key] > mostCharNum:
        mostCharNum = charDict[key]
        mostChar = key
      elif charDict[key] == mostCharNum:
        mostChar += key
      
      totalDict += charDict[key]
    
    if end - start + 1 - mostCharNum > k:
      charDict[s[start]] -= 1
      end += 1
      start += 1
    else:
      if end - start + 1 > res:
        res = end - start + 1
    
      end += 1

  return res