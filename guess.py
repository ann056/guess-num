import random
start = input ('請設定起始數字：')
end = input ('請設定結束數字：')
start = int(start)
end = int(end)
answer = random.randint (start, end)
count = 0
while True:
	count += 1 # count = count + 1
	number = input('請猜數字：')
	number = int(number)
	if number == answer:
		print('終於猜對了！')
		break
	elif number > answer:
		print('數字猜太大了')
	elif number < answer:
		print('數字猜太小了')
	print('這是你猜的第', count, '次')

