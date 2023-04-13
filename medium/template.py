# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

def successfulPairs(spells, potions, success):
  res = []
  

  for spell in spells:
    spellSum = 0
    for potion in potions:
      print(spell * potion)
      if spell * potion >= sucess:
        spellSum += 1

    res.append(spellSum)

  return res

def main():
  spells = [5,1,3]
  potions = [1,2,3,4,5]
  success = 7

  print(successfulPairs(spells, potions, success))

if __name__ == "__main__":
  main()