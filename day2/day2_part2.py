import sys

def main():

	file_object = open('input.txt')
	lines = file_object.read().splitlines()
	validPasswordCount = 0
	for line in lines:
		pos1 = int(line[:line.index("-")])
		pos2 = int(line[line.index("-") + 1 : line.index(" ")])
		mustContainLetter = line[line.index(" ") + 1:line.index(":")]
		password = line[line.index(":")+2:]
		if (password[pos1-1] == mustContainLetter and password[pos2-1] != mustContainLetter) or \
		(password[pos1-1] != mustContainLetter and password[pos2-1] == mustContainLetter):
			validPasswordCount += 1

if __name__ == '__main__':
    main()
