table = []
for num1 in range(1,13):
	table.append([])
	for num2 in range(1,13):
		table[num1-1].append(num1 * num2)
	print(table[num1-1])
