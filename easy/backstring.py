# https://leetcode.com/problems/backspace-string-compare
# Time Complexity = O(n+m)


def backspaceCompare(s, t):
  stack1 = []
  
  for char in s:
    if char == '#' and stack1:
      stack1.pop()
    else:
      stack1.append(char)
  
  stack2 = []
  
  for char in t:
    if char == '#' and stack2:
      stack2.pop()
    elif char != '#':
      stack2.append(char)
  
  print(f'stack1 = {stack1} and stack2 = {stack2}')
  
  return stack1 == stack2

def main():
  s = "y#fo##f"
  t = "y#f#o##f"

  print(backspaceCompare(s, t))

if __name__ == "__main__":
  main()