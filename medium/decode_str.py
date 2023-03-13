# https://leetcode.com/problems/decode-string
# Time Complexity = O(n)

def decodeString(s):
  res = ''
  stack = []
  check = 0

  temp = ''
  numChar = ''
  for char in s:
    print(f'=============== Looking at {char} ===============')
    if char.isnumeric():
      if temp:
        stack.append(temp)
        temp = ''
      numChar += char
      print(f'stack = {stack}')
      
    elif char == ']':
      print(f'stack = {stack}')
      print(f'temp = {temp}')
      check -= 1
      print(check)
      if check == 0:
        if temp:
          stack.append(temp)
          temp = ''
        while len(stack) != 1:
          print(f'stack = {stack}')
          char = stack.pop()
          num = stack.pop()
          if not num.isnumeric():
            stack.append(num + char)
          else:
            stack.append(char * int(num))
        res = res + stack[0]    
        stack = []
      elif temp:
        num = stack.pop()
        if not num.isnumeric():
          stack.append(num + temp)
          temp = ''
        else: 
          char = temp
          temp = ''
          if stack:
            stack.append(char * int(num))
          else: 
            res = res + char * int(num)
      else:
        char = stack.pop()
        num = stack.pop()
        if not num.isnumeric():
          stack.append(num + char)
        else:
          if stack:
            stack.append(char * int(num))
          else: 
            res = res + char * int(num)
        print(f'stack = {stack}')
      
      print(f'res = {res}')
        
    elif char == '[':
      stack.append(numChar)
      numChar = ''
      if temp:
        stack.append(temp)
      temp = ''
      check += 1
    elif check > 0:
      print(f'char = {char}')
      temp += char
    else:
      res = res + char


  if stack:
    return stack[0]
  else: 
    return res

def main():
  s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
  #s = "1[a1[b1[c]d]s]"

  print(decodeString(s))

if __name__ == "__main__":
  main()