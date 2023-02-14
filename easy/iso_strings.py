# https://leetcode.com/problems/isomorphic-strings
# Time Complexity = O(n)


def iso(s, t):

  charDict1 = {}
  charDict2 = {}

  for i, char in enumerate(s):
    if char not in charDict1:
      charDict1[char] = t[i]
    else:
      if charDict1[char] != t[i]:
        return False
      
    if t[i] not in charDict2:
      charDict2[t[i]] = char
    else:
      if charDict2[t[i]] != char:
        return False
    
  return True

def main():
  s = 'badc'
  t = 'baba'
  print(iso(s, t))

if __name__ == "__main__":
  main()