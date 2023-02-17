# https://leetcode.com/problems/longest-palindrome
# Time Complexity = O(n)


def longest_palind(s):
  charDict = {}
  long_sum = 0
  middle = 0
  
  for char in s:
    if char in charDict:
      charDict[char] += 1
    else:
      charDict[char] = 1
  
  if len(charDict) == 1:
    return charDict[s[0]]
  
  for char in charDict:
    if charDict[char] % 2 == 0:
      long_sum += charDict[char]
    if charDict[char] % 2 == 1:
      if middle == 0:
        long_sum += charDict[char]
        middle = 1
      else:
        long_sum += charDict[char] - 1
  
  return long_sum

def main():
  s = 'aaabbccd'
  
  print(longest_palind(s))

if __name__ == "__main__":
  main()