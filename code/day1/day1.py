def part1(path):
	f = open(path, 'r')

	ans = 0
	nums = 0
	for x in f:
		if x == '' or x == '\n':
			ans = max(ans, nums)
			nums = 0
		else:
			nums += int(x)

	print('Answer Part 1: ', max(ans, nums))

def part2(path):
	f = open(path, 'r')

	ans = [0, 0, 0]
	nums = 0
	for x in f:
		if x == '' or x == '\n':
			#TODO: this can be optimize
			if nums > min(ans):
				ans.remove(min(ans))
				ans.append(nums)
			nums = 0
		else:
			nums += int(x)
	
	if nums > min(ans):
		ans.remove(min(ans))
		ans.append(nums)

	print('Answer Part 2: ', sum(ans))

if __name__ == '__main__':
	#use correct path
	path = './code/day1/input.txt'

	part1(path=path)
	part2(path=path)