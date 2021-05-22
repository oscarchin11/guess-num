# 产生一个随机整数1～100 (不要打印出来)
# 让使用者重复输入数字去猜
# 猜对的话 印出 "终于猜对了"
# 猜错的话 要告诉他 比答案大/小

import random
start = input('请决定随机数字范围开始值：')
end = input('请决定随机数字范围结束值：')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count +=1  #count = count + 1
	num = input('请猜数字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('这次你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这次你猜的第', count, '次')