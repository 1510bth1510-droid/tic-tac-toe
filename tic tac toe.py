import random

boa = ['_'] * 9

def board():

    choice = int(input('숫자로 입력(1~9): '))

    if choice == 1 and boa[0] == '_':
        boa[0] = 'O'
        return True
    elif choice == 2 and boa[1] == '_':
        boa[1] = 'O'
        return True
    elif choice == 3 and boa[2] == '_':
        boa[2] = 'O'
        return True
    elif choice == 4 and boa[3] == '_':
        boa[3] = 'O'
        return True
    elif choice == 5 and boa[4] == '_':
        boa[4] = 'O'
        return True
    elif choice == 6 and boa[5] == '_':
        boa[5] = 'O'
        return True
    elif choice == 7 and boa[6] == '_':
        boa[6] = 'O'
        return True
    elif choice == 8 and boa[7] == '_':
        boa[7] = 'O'
        return True
    elif choice == 9 and boa[8] == '_':
        boa[8] = 'O'
        return True
    else:
        print('잘못된 입력입니다.')
    return False


def winl():
    global winl1, winl2, winl3, winl4, winl5, winl6, winl7, winl8
    winl1 = boa[0] + boa[1] + boa[2]
    winl2 = boa[3] + boa[4] + boa[5]
    winl3 = boa[6] + boa[7] + boa[8]
    winl4 = boa[0] + boa[3] + boa[6]
    winl5 = boa[1] + boa[4] + boa[7]
    winl6 = boa[2] + boa[5] + boa[8]
    winl7 = boa[0] + boa[4] + boa[8]
    winl8 = boa[2] + boa[4] + boa[6]


def pcturn():
    winl()
    #공격
    if winl1.count('X') == 2:
        if boa[0] == '_':
            boa[0] = 'X'
            return
        elif boa[1] == '_':
            boa[1] = 'X'
            return
        elif boa[2] == '_':
            boa[2] = 'X'
            return
    if winl2.count('X') == 2:
        if boa[3] == '_':
            boa[3] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[5] == '_':
            boa[5] = 'X'
            return
    if winl3.count('X') == 2:
        if boa[6] == '_':
            boa[6] = 'X'
            return
        elif boa[7] == '_':
            boa[7] = 'X'
            return
        elif boa[8] == '_':
            boa[8] = 'X'
            return
    if winl4.count('X') == 2:
        if boa[0] == '_':
            boa[0] = 'X'
            return
        elif boa[3] == '_':
            boa[3] = 'X'
            return
        elif boa[6] == '_':
            boa[6] = 'X'
            return
    if winl5.count('X') == 2:
        if boa[1] == '_':
            boa[1] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[7] == '_':
            boa[7] = 'X'
            return
    if winl6.count('X') == 2:
        if boa[2] == '_':
            boa[2] = 'X'
            return
        elif boa[5] == '_':
            boa[5] = 'X'
            return
        elif boa[8] == '_':
            boa[8] = 'X'
            return
    if winl7.count('X') == 2:
        if boa[0] == '_':
            boa[0] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[8] == '_':
            boa[8] = 'X'
            return
    if winl8.count('X') == 2:
        if boa[2] == '_':
            boa[2] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[6] == '_':
            boa[6] = 'X'
            return

    #방어
    if winl1.count('O') == 2:
        if boa[0] == '_':
            boa[0] = 'X'
            return
        elif boa[1] == '_':
            boa[1] = 'X'
            return
        elif boa[2] == '_':
            boa[2] = 'X'
            return
    if winl2.count('O') == 2:
        if boa[3] == '_':
            boa[3] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[5] == '_':
            boa[5] = 'X'
            return
    if winl3.count('O') == 2:
        if boa[6] == '_':
            boa[6] = 'X'
            return
        elif boa[7] == '_':
            boa[7] = 'X'
            return
        elif boa[8] == '_':
            boa[8] = 'X'
            return
    if winl4.count('O') == 2:
        if boa[0] == '_':
            boa[0] = 'X'
            return
        elif boa[3] == '_':
            boa[3] = 'X'
            return
        elif boa[6] == '_':
            boa[6] = 'X'
            return
    if winl5.count('O') == 2:
        if boa[1] == '_':
            boa[1] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[7] == '_':
            boa[7] = 'X'
            return
    if winl6.count('O') == 2:
        if boa[2] == '_':
            boa[2] = 'X'
            return
        elif boa[5] == '_':
            boa[5] = 'X'
            return
        elif boa[8] == '_':
            boa[8] = 'X'
            return
    if winl7.count('O') == 2:
        if boa[0] == '_':
            boa[0] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[8] == '_':
            boa[8] = 'X'
            return
    if winl8.count('O') == 2:
        if boa[2] == '_':
            boa[2] = 'X'
            return
        elif boa[4] == '_':
            boa[4] = 'X'
            return
        elif boa[6] == '_':
            boa[6] = 'X'
            return

    #한칸
    empty = []
    for index, value in enumerate(boa):
        if value == '_':
            empty.append(index)
    if empty:
        boa[random.choice(empty)] = 'X'
    return

def wl():
    win_lines = [winl1, winl2, winl3, winl4, winl5, winl6, winl7, winl8]
    for line in win_lines:
        if line == 'OOO':
            print('승')
            return True
        elif line == 'XXX':
            print('패')
            return True
    if '_' not in boa:
        print('무승부')
        return True




# 게임 시작
while True:
    board()
    print('-' * 20)
    
    if not youturn():
        continue

    winl()
    if wl():
        board()
        print('-' * 20)
        b = int(input('다시 시작 = 1번\n종료 = 2번'))
        if b == 1:
            boa = ['_'] * 9
            continue
        elif b == 2:
            break
        else:
            print('잘못된 입력')
            break

    pcturn()
    winl()
    if wl():
        board()
        print('-' * 20)
        b = int(input('다시 시작 = 1번\n종료 = 2번'))
        if b == 1:
            boa = ['_'] * 9
            continue
        elif b == 2:
            break
        else:
            print('잘못된 입력')
            break
