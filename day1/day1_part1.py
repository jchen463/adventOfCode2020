import sys

def main():

	file_object = open('input.txt')
	expenses = file_object.read().splitlines()
	expenses = [int(i) for i in expenses] 

	for i, expense in enumerate(expenses, start=1):
		for secondExpense in expenses[i:]:
			if(expense + secondExpense == 2020):
				print(expense * secondExpense)


if __name__ == '__main__':
    main()
