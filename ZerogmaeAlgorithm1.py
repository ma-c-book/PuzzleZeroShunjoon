import random
import sys
import time



board = [[0,0,0,0,0,0,0,0,0,0], # 10X10 보드 생성
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
row = 0
survive = True

def check1(row1, row2):  # 1행과 2행의 차를 비교하는 함수
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
        
  # 비교하는 두 행의 인덱스
a, b = 0, 1
def solve1(board): # 게임을 알아서 풀어주는 함수
    a, b = 0, 1 # 비교하는 행의 인덱스
    for i in board:
        print(i)
    count = 0
    while survive: # 게임이 끝날 때까지 반복
        print(board[a], board[b])
        # 모든 수가 같을 때
        if check1(board[a], board[b])[0]== 0: # check 함수의 반환값이 0이라면, a와 b에 1씩 더해줌
            print("모든 수가 같음")
            count +=1
                      
            a += 1; b+= 1
            time.sleep(1)
            print(a, b)
        # 모든 수가 작을 때
        elif check1(board[a], board[b])[0] == -1: # 반환값이 -1, 즉 2행의 값이 모두 1행의 값보다 크면, 2행의 값들 중에, 1행 - 2행에서 가장 값이 큰 수, 즉 양이 아닌 정수 중에 0에 가장 가까운 수를 빼줌
            print("모든 수가 작음")
            newlist = check1(board[a], board[b])[1]
            minus(b+1, newlist.index(max(newlist))+1)
            print(a,b)
        # 모든 수가 클 때
        elif check1(board[a], board[b])[0] == 1: # 반환값이 1, 즉 1행의 값이 모두 2행의 값보다 크면, 1행의 값들 중에, 1행 -2행에서 가장 작은 수를 빼줌
            print("모든 수가 큼")
            newlist = check1(board[a], board[b])[1]
            minus(a+1, newlist.index(min(newlist))+1)
            print(a,b)
        # 섞여 있을 때
        else:
            print("섞임") # 반환값이 1, 즉 어떤 것은 1행의 값이 2행의 값보다 크고 나머지는 아니라면, 2행의 값들 중에 1행-2행에서 가장 큰 수 한 번, 1행의 값들 가장 작은 수 한 번 빼준다.
            newlist = check1(board[a], board[b])[1]
            minus(b+1, newlist.index(max(newlist))+1)
            minus(a+1, newlist.index(min(newlist))+1)
            print(a,b)
        if b == 10: # 9항과 10항을 비교할 때, 만약에 보드가 전부 0이라면, 반복문을 종료한다.
                if sum(board[0]) == 0:
                    print("게임 끝!")
                    break
                else:
                    a = 0; b = 1
                    print("처음으로")


def solve2(board):
    while survive:
        for i in range(10):
            for g in range(10):
                if sum(board[0]) == 0:
                    print("게임 끝!")
                    break
                if check2(g,i):
                    minus(g+1,i+1)
                    
def check2(g, i):
    print(g, i)
    time.sleep(1)
    if min([y[i] for y in board]) + min(board[i]) -2 < board[g][i] -1:
        return False
    else:
        return True
    '''
    if 0 in board[i]:
        return False
    for f in board:
        if f[0] == 0:
            return False'''

    
def plus(a, b): # 가로행과 세로행에 1씩 더해주는 함수, 게임을 만들 때 사용함
    for i in range(10):
        board[a-1][i] += 1
    for g in range(10):
        board[g][b-1] += 1
    board[a-1][b-1] -= 1

answer = []
def minus(a, b): # 가로행과 세로행에 1씩 빼주는 함수, 게임을 할 때 사용함
    board[a-1][b-1] += 1
    for i in range(10):
        board[a-1][i] -= 1
    for g in range(10):
        board[g][b-1] -= 1
    time.sleep(0.2)
    answer.append([a,b])
    for i in board:
         print(i)

def start(level): # 게임이 시작될 때 실행하는 함수, 레벨 입력값에 따라 plus 함수를 무작위 위치에 입력값 횟수로 게임 보드를 생성함
    for i in range(level):
        plus(random.randint(1, 10), random.randint(1, 10))
    for g in board:
        print(g)

level = int(input("레벨을 입력해주세요")) # 게임이 시작하면 레벨 입력값을 받는 코드
start(level) # start 함수 실행

while survive: # 게임이 끝날 때까지 계속 좌표입력값을 받음과 동시에, 게임이 오버됐는지 확인하는 함수

        a, b = map(int, input().split(","))
        if a == 777 and b == 777:
            solve1(board)
            print("You Win")
            print(answer)
            break
        if a == 777 and b == 888:
            solve2(board)
            print("You Win")
            print(answer)
            break
        if a == 4444 and b == 4444:
            sys.exit()
        minus(a, b)
        for i in board:
            if min(i) < 0:
                survive = False
                print("Game Over")
                break
            elif max(i) == 0:
                survive = False
                print("You Win")
                break