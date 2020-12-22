import sys

def main():

	file_object = open('input.txt')
	expenses = file_object.read().splitlines()
	expenses = [int(i) for i in expenses] 

	for i, expense in enumerate(expenses, start=1):
		for j, secondExpense in enumerate(expenses[i:], start=1):
			for thirdExpense in expenses[i + j:]:
				if(expense + secondExpense + thirdExpense == 2020):
					print(expense * secondExpense * thirdExpense)


if __name__ == '__main__':
    main()
