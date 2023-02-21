# https://leetcode.com/problems/fibonacci-number
# O(n)

def fib(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
    
  sum = fib(n - 1) + fib(n - 2)
  
  return sum

def main():
  n = 6
  print(fib(n))

if __name__ == "__main__":
  main()