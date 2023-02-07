def palin(num):
  if num < 0:
    return False
  
  num = str(num)
  
  start = 0
  end = len(num) - 1
  
  while start < end:
    if num[start] != num[end]:
      return False
    start += 1
    end -= 1
  
  return True



def main():
  num = 111111111112
  print(palin(num))

if __name__ == "__main__":
  main()