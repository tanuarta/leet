# https://leetcode.com/problems/longest-substring-without-repeating-characters
# 56ms Runtime, 14mb Memory
# Time Complexity = O(n)

def longest_sub(string):
  char_dict = {}
  start = 0
  end = 0
  res = 0
  
  if len(string) == 1:
    return 1
  
  for char in string:
    if char in char_dict and char_dict[char] >= start:
      print(f'start = {start} char = {char_dict[char]}')
      start = char_dict[char] + 1
      if start < len(string) and string[start] == char and start != end:
        start += 1
        
    char_dict[char] = end
    end += 1
    if end - start > res:
        res = end - start

  return res

def main():
  string = "bbtablud"
  print(longest_sub(string))

if __name__ == "__main__":
  main()