# https://leetcode.com/problems/is-subsequence
# Time Complexity = O(n)

def subsequence(s, t):
  sCounter = 0
  
  for i, char in enumerate(t):
    if sCounter >= len(s):
      break
  
    if char == s[sCounter]:
      sCounter += 1

  if sCounter == len(s):
    return True

  return False

def main():
  s = 'b'
  t = 'abc'
  print(subsequence(s, t))

if __name__ == "__main__":
  main()