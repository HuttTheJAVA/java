import sys
input = sys.stdin.readline

king,rock,n = input().split()
n = int(n)

col = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
alp = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
orders = []

king_col = col[king[0]]
king_row = 8-int(king[1])

rock_col = col[rock[0]]
rock_row = 8-int(rock[1])

for i in range(n):
    orders.append(input().strip())

king_x = {'R':0,'L':0,'B':1,'T':-1,'RT':-1,'LT':-1,'RB':1,'LB':1}
king_y = {'R':1,'L':-1,'B':0,'T':0,'RT':1,'LT':-1,'RB':1,'LB':-1}

for order in orders:
    new_king_row = king_row + king_x[order]
    new_king_col = king_col + king_y[order]
    if 0<=new_king_row<8 and 0<=new_king_col<8:
        if rock_row == new_king_row and rock_col == new_king_col:
            new_rock_row = rock_row + king_x[order]
            new_rock_col = rock_col + king_y[order]
        else:
            new_rock_row = rock_row
            new_rock_col = rock_col
        if 0<=new_rock_row<8 and 0<=new_rock_col<8:
            king_row = new_king_row
            king_col = new_king_col
            rock_row = new_rock_row
            rock_col = new_rock_col

print(alp[king_col]+str(8-king_row))
print(alp[rock_col]+str(8-rock_row))
