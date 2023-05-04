# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
# Time Complexity = O(n)

def average(salary):
  max = salary[0]
  min = salary[0]
  sum = 0

  for wage in salary:
    if wage > max:
      max = wage
    elif wage < min:
      min = wage

    sum += wage

  return (sum - max - min) / (len(salary) - 2)

def main():
  salary = [1000,2000,3000]
    
  print(average(salary))

if __name__ == "__main__":
  main()