from tkinter import *
import random
import time

window = Tk()
window.title("제로게임")

canvas = Canvas(window, width = 700, height= 490, bg="#FFF8E5")
canvas.pack()



count = 0 # 게임에서 터치하는 횟수
listmap = []

class Game:
	def __init__(self):
		pass
	def start(self, level):
		global count
		count = level
		for y in range(1, 11):
			for x in range(1, 11):
				globals()["x{}y{}".format(i, g)] = 0
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
	
window.mainloop()