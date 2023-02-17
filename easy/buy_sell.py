# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Time Complexity = O(n)

def buySell(prices):
  bestSell = 0
  buy = 0
  sell = 0
  
  
  for i, num in enumerate(prices):
    print(f'buy = {buy} \nsell = {sell}')
    if i == 0:
      buy = num
    else:
      if num < buy:
        buy = num
        sell = buy - 1
      elif num > sell:
        sell = num
        
      if sell - buy > bestSell:
        bestSell = sell - buy
  
  return bestSell
  

def main():
  prices = [2, 4, 1]
  
  print(buySell(prices))

if __name__ == "__main__":
  main()