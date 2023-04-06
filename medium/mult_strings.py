# Incomplete

def multiply(num1, num2):
	res = ''
	carry = 0

	if len(num1) > len(num2):
		num1Pointer = len(num1) - 1
		num2Pointer = len(num2) - 1
	else:
		temp = num1
		num1 = num2
		num2 = temp
		num1Pointer = len(num1) - 1
		num2Pointer = len(num2) - 1
		
	while num2Pointer >= 0:
		while num1Pointer >= 0:
			mult = int(num1[num1Pointer]) * int(num2[num2Pointer]) + carry
			res = str(mult) + res
			if mult >= 10:
				carry = 1
			else:
				carry = 0
		num2Pointer -= 1

	return res

def main():
	num1 = '10'
	num2 = '3'

	print(multiply(num1, num2))

if __name__ == "__main__":
  main()