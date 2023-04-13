# https://leetcode.com/problems/optimal-partition-of-string/
# Time Complexity = O(n)

def partitionString(s):
	charDict = {}
	res = 1

	for char in s:
		if char in charDict:
			res += 1
			charDict = {}

		charDict[char] = 1

	return res

def main():
	s = "abacaba"

	print(partitionString(s))

if __name__ == "__main__":
  main()