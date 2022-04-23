
import sys

def reverse_string(line): 
    if len(line) == 0: 
        return line 
    else:
    	return line[::-1]

n = len(sys.argv)
string = ""
for x in range(1, n):
	string += sys.argv[x]
	if x < n - 1:
		string += " "
print(reverse_string(string.swapcase()))
