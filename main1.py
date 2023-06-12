from tkinter import *
import tkinter as tk
import random
import time

class MainWin(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.board = [[0] * 10 for _ in range(10)]
        self.buttons = {}

        self.init_widgets()

    def init_widgets(self):
        
        for i in range(10):
            for j in range(10):
                if j == 0:
                    btn = tk.Button(
                    self,
                    width=5,
                    height=2,
                    text=str(self.board[i][j]),
                    command=lambda x=i, y=j: self.on_click(x, y),
                    )
                    btn.grid(row=i+3, column=j+1, sticky=E)
                    self.buttons[(i, j)] = btn
                else:
                    btn = tk.Button(
                        self,
                        width=5,
                        height=2,
                        text=str(self.board[i][j]),
                        command=lambda x=i, y=j: self.on_click(x, y),
                    )
                    btn.grid(row=i+3, column=j+1)
                    self.buttons[(i, j)] = btn
        
        self.level_var = tk.IntVar()
        tk.Label(self, text="레벨을 입력해주세요").grid(row=0, column=0,  sticky="nsew")
        self.level_entry = tk.Entry(self, width=50, borderwidth=1, textvariable=self.level_var)
        self.level_entry.grid(row=1, column=0, ipadx=10)
        tk.Button(self, text="확인", command=self.start).grid(row=2, column=0, sticky="nsew")
        
        
        # entry.insert(0, "Hello python")

        # self.t = tk.Text(self)
# afjaw;eoifjaweoiaj;efoi 수정중
        
        # self.t.grid(row=1, column=12, columnspan=10)
        
    
    def start(self):
        self.board = [[0] * 10 for _ in range(10)]
        level = self.level_var.get()
        if level == 7777777:
            self.hack()
        else:
            for i in range(level):
                self.plus(random.randint(1, 10), random.randint(1, 10))
            for i in range(10):
                for j in range(10):
                    self.buttons[(i, j)].config(text=str(self.board[i][j]))

            label = tk.Label(self, text="Level : "+str(level))
            label.grid(row=3, column=0)
            self.label2.grid_forget()
        
    def on_click(self, row, col):
        # 버튼을 클릭했을 때 실행되는 함수
        # 여기서 리스트 값을 변경하고 버튼의 텍스트를 업데이트할 수 있습니다.
        self.board[row][col] += 1
        for i in range(10):
            self.board[row][i] -= 1
        for g in range(10):
            self.board[g][col] -= 1
        # self.buttons[(row, col)].config(text=str(self.board[row][col]))
        for i in range(10):
            for j in range(10):
                self.buttons[(i, j)].config(text=str(self.board[i][j]))
        print(self.board)
        for i in self.board:
            if min(i) < 0:
                self.label2 = tk.Label(self, text="Game Over..")
                self.label2.grid(row=4, column=0)
                break
        if self.board[0].count(0) == 10:
            self.label2 = tk.Label(self, text="You Win!")
            self.label2.grid(row=4, column=0)


    def plus(self, a, b):
        for i in range(10):
            self.board[a - 1][i] += 1
        for g in range(10):
            self.board[g][b - 1] += 1
        self.board[a - 1][b - 1] -= 1
        self.buttons[(a - 1, b - 1)].config(text=str(self.board[a - 1][b - 1]))
        

    def minus(self, a, b):
        self.board[a - 1][b - 1] += 1
        for i in range(10):
            self.board[a - 1][i] -= 1
        for g in range(10):
            self.board[g][b - 1] -= 1
        self.buttons[(a - 1, b - 1)].config(text=str(self.board[a - 1][b - 1]))

    a, b = 0, 1
    def hack(self):
        a, b = 0, 1
        survive = True
        count = 0
        while survive: # 게임이 끝날 때까지 반복

            # 모든 수가 같을 때
            if self.check1(self.board[a], self.board[b])[0]== 0: # check 함수의 반환값이 0이라면, a와 b에 1씩 더해줌
                print("모든 수가 같음")
                count +=1

                a += 1; b+= 1
                time.sleep(1)
                print(a, b)
                print(self.board)
            # 모든 수가 작을 때
            elif self.check1(self.board[a], self.board[b])[0] == -1: # 반환값이 -1, 즉 2행의 값이 모두 1행의 값보다 크면, 2행의 값들 중에, 1행 - 2행에서 가장 값이 큰 수, 즉 양이 아닌 정수 중에 0에 가장 가까운 수를 빼줌
                print("모든 수가 작음")
                newlist = self.check1(self.board[a], self.board[b])[1]
                self.minus(b+1, newlist.index(max(newlist))+1)
                print(a,b)
            # 모든 수가 클 때
            elif self.check1(self.board[a], self.board[b])[0] == 1: # 반환값이 1, 즉 1행의 값이 모두 2행의 값보다 크면, 1행의 값들 중에, 1행 -2행에서 가장 작은 수를 빼줌
                print("모든 수가 큼")
                newlist = self.check1(self.board[a], self.board[b])[1]
                self.minus(a+1, newlist.index(min(newlist))+1)
                print(a,b)
            # 섞여 있을 때
            else:
                print("섞임") # 반환값이 1, 즉 어떤 것은 1행의 값이 2행의 값보다 크고 나머지는 아니라면, 2행의 값들 중에 1행-2행에서 가장 큰 수 한 번, 1행의 값들 가장 작은 수 한 번 빼준다.
                newlist = self.check1(self.board[a], self.board[b])[1]
                self.minus(b+1, newlist.index(max(newlist))+1)
                self.minus(a+1, newlist.index(min(newlist))+1)
                print(a,b)
            if b == 10: # 9항과 10항을 비교할 때, 만약에 보드가 전부 0이라면, 반복문을 종료한다.
                    if sum(self.board[0]) == 0:
                        print("게임 끝!")
                        break
                    else:
                        a = 0; b = 1
                        print("처음으로")

    def check1(self,row1, row2):  # 1행과 2행의 차를 비교하는 함수
        check = [0,0,0,0,0,0,0,0,0,0] # 1행과 2행의 차를 담을 수 있는 10개의 공간 리스트 check를 만들어준다.
        for i in range(10):
            check[i] = row1[i] - row2[i] # 1행에서 2행을 뺀 값을 저장해준다.
        if check.count(0) == 10: # 1행과 2행의 차가 전부 0일 때 0을 반환함
            return 0, check
        elif max(check) <= 0: # check 리스트 의 최댓값이 0보다 작으면, 즉 모든 수가 0보다 작으면, 2행의 값이 모두 1행보다 크다는 걸 의미하고, -1을 반환한다.
            return -1, check
        elif min(check) >= 0:
            return 1, check # 최솟값이 0보다 크면, 1행이 2행보다 크다는 걸 의미하고 1을 반환한다.
        else:
            return 2, check # 1행과 - 2행의 값이 양수, 음수라면 2를 반환한다.
       
    def check2(self,g, i):
        print(g, i)
        time.sleep(1)
        if min([y[i] for y in self.board]) + min(self.board[i]) -2 < self.board[g][i] -1:
            return False
        else:
            return True


if __name__ == "__main__":
    app = MainWin(None)
    app.mainloop()
