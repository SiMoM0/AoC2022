f = open('input.txt', 'r')

ans = 0
nums = 0
for x in f:
	if x == '' or x == '\n':
		ans = max(ans, nums)
		nums = 0
	else:
		nums += int(x)

print('Answer: ', max(ans, nums))