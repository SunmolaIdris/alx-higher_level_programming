#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

total = 0
length = len(argv)
for i in range(1, length):
    total += int(argv[i])
print('{}'.format(total))
