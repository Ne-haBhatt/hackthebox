first_state = 69420
last_state = 999

f_in = open("deterministic.txt", "r")

next = first_state
dic = {}

with open("deterministic.txt") as f_in:
	for line in f_in:
		values = line.strip().split(" ") # split the line in [state, value, next_state]

		# dic[state] = (value, next_state)
		try:
			dic[int(values[0])] = (int(values[1]), int(values[2])) # with int() ignore the ascii values
		except:
			pass

result = []

while next != last_state:
	temp = dic[next]
	result.append(temp[0])
	next = temp[1]

print(' '.join(str(i) for i in result))
