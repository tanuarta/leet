# https://leetcode.com/problems/boats-to-save-people/
# Time Complexity = O(nlogn)

# O(nlogn) solution
def numRescueBoats(people, limit):
	people.sort()

	end = len(people) - 1
	start = 0

	res = 0

	while end >= start:
		if people[end] >= limit or people[end] + people[start] > limit:
			res += 1
			end -= 1
		elif people[end] + people[start] <= limit:
			res += 1
			end -= 1
			start += 1

	return res


def main():
	people = [3,2,2,1]
	limit = 3
	print(numRescueBoats(people, limit))

if __name__ == "__main__":
  main()