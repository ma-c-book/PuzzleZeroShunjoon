import random
import time
'''
t = input()
T = len(t)
print(T)

sum = 0
for i in t:
	globals()["s{}".format(i)] = int(i)*(int(i)+1)/2

for i in (t):
	sum += f"s{i}"
print(sum)
'''
count = 0 # 게임에서 터치하는 횟수
listmap = []

class Game:
	def __init__(self):
		pass
	def start(self, level):
		global count
		count = level
		for i in range(1, 11):
			for g in range(1, 11):
				globals()["v{}h{}".format(i, g)] = 0
		for i in range(level):
			plus(random.randint(1, 10), random.randint(1,10), True)

def show():
	for i in range(1,11):
		for g in range(1, 11):
			print(globals()["v{}h{}".format(i,g)], end=" ")
			listmap.append(globals()["v{}h{}".format(i,g)])
		print()
	#print(listmap)

def plus(a, b, c):
	if c == True:
		for i in range(1, 11):
			globals()["v{}h{}".format(i, b)] += 1
			globals()["v{}h{}".format(a, i)] += 1
		globals()["v{}h{}".format(a, b)] -= 1
	else:
		pass


def minus(a, b, c):
	if c == True:
		for i in range(1, 11):
			globals()["v{}h{}".format(i, b)] -= 1
			globals()["v{}h{}".format(a, i)] -= 1
		globals()["v{}h{}".format(a, b)] += 1
		global count
		count -= 1
	else:
		pass


# def check(a, b):
a = int(input("레벨을 선택하세요 예) 1\n"))
print("3초후 게임 플레이를 시작합니다.")
time.sleep(3)
game1 = Game()
game1.start(a)
show()

while count > 0:
	a, b = map(int, input("터치하고 하는 점의 좌표쌍을 넣어주세요 예) 1,1 \n").split(","))
	minus(b, a, True)
	show()
clear = True
for i in range(1, 11):
	if globals()["v{}h{}".format(i, i)] != 0:
		clear = False
		print("실패")
		break
if clear:
	print("축하합니다")
'''
reverse = False
time.sleep(3)
while count > 0:
	for i in range(1, 11):
		for g in range(1, 11):
			x, y = i, g
			temp = 1
			if globals()["v{}h{}".format(i, g)] > 0:
				while 0 < x < 11 and 0 < y < 11:
					if reverse == False:
						x += 1
						y += 1
					else:
						x -= 1
						y -= 1
					if x > 10 or y > 10:
						x -= 1
						y -= 1
						reverse = True
					if globals()["v{}h{}".format(i+x, g+y)] + globals()["v{}h{}".format(i, g)] -2 < globals()["v{}h{}".format(i, g)]
'''


#		"v{}h{}".format(i, b) += 1
#		"v{}h{}".format(a, i) += 1
#		"v{}h{}".format(a, b) -= 1