ones = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
nonsense = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

# generate numbers 
numbers = []
for x in range(1, 1000):
	add = str(x)
	while len(add)< 3:
		add = "0" + add
	numbers.append(add)

# this can be greatly simplified if we are just counting
# i want the whole string to print and will revisit once i know 
# the answer, i can do it the simplified way 
total = len('onethousand')
for y in numbers:
	word = ''
	# "x hundred and" (includes and-checking)
	if y[0] != '0':
		word = ones[int(y[0])] + 'hundred'
		if y[1:3] != '00':
			word += 'and'
	if '0' != y[1] != '1':
		word += tens[int(y[1])] + ones[int(y[2])]
	# dealing with 10-19
	if y[1] == '1':
		word += nonsense[int(y[2])]
	# dealing with 0-9
	if y[1] == '0':
		#special case of whole hundreds
		if y[2] != '0':
			word += ones[int(y[2])]
	total += len(word)
	print(word)

print(total)