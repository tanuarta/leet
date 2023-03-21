# https://leetcode.com/problems/longest-common-prefix
# Time Complexity = Size of shortest String * Number of Strings = O(n)

def longestCommonPrefix(strs):
  res = ''
  check = 0
  index = 0
  
  while check == 0:
    for i, string in enumerate(strs):
      if string == '': return ''
      elif index == len(string):
        return res
      if i == 0:
        toAdd = string[index]
      else:
        if toAdd != string[index]:
          return res
    res += toAdd
    index += 1
  
  return res

def main():
  strs = ["flower", "flower", "flower", "flower"]

  print(longestCommonPrefix(strs))

if __name__ == "__main__":
  main()