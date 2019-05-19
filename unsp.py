import sys

def check(a):
	bool = False
	for l in a:
		if l not in alphabet:
			continue
		else:
			bool = True
			break
	return bool	

alphabet = []
for _ in range(97,123):
	alphabet.append(chr(_))
alphabet.append("{")
alphabet.append("}")j
text = open(sys.argv[1],'r')
array = text.readlines()
new_array = []
for _ in array:
	if check(_) == True:
		new_array.append(_) 
text.close()
text = open(sys.argv[1],'w')
string = ''
for _ in new_array:
	string = string + _
text.write(string)
text.close()
