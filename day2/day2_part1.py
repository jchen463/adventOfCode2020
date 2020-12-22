import sys

def main():

	file_object = open('input.txt')
	lines = file_object.read().splitlines()
	validPasswordCount = 0
	for line in lines:
		minOccurance = int(line[:line.index("-")])
		maxOccurance = int(line[line.index("-") + 1 : line.index(" ")])
		mustContainLetter = line[line.index(" ") + 1:line.index(":")]
		password = line[line.index(":")+2:]
		letterCount = password.count(mustContainLetter)
		if letterCount <= maxOccurance and letterCount >= minOccurance:
			validPasswordCount += 1
	print(validPasswordCount)

if __name__ == '__main__':
    main()
