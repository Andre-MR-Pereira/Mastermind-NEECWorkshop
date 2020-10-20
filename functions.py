import random


def generateSecret():
    passlist = ()
    changer = list(passlist)
    numberlist = list(range(1, 9))
    for i in range(4):
        pick = random.randint(0, 7-i)
        changer.append(numberlist.pop(pick))
    passlist = tuple(changer)
    print(passlist)
    return passlist


def generateInput():
    answer = tuple()
    changer = list(answer)
    valid = False
    '''
    for i in range(4):
        repeat_flag=False
        entry=int(input('Please make your play:'))
        while True:
            repeat_flag=False
            for x in changer:
                if entry==x:
                    repeat_flag=True
            if repeat_flag==False:
                break
            entry=int(input('You cannot repeat numbers.Please make your play:'))
        changer.append(entry)
    '''
    while valid == False:
        valid = True
        changer = [int(entry)
                   for entry in input('Please make your play: ').split()]
        for i in range(4):
            if changer[i] > 8 or changer[i] < 1:
                valid = False
                print('Invalid entry. Numbers have to be between 1 and 8')

    answer = tuple(changer)
    print(answer)
    return answer


def match(t, k):
    placed_count = 0
    right_count = 0
    tchanger = list(t)
    kchanger = list(k)
    for i in range(4):
        if tchanger[i] == kchanger[i]:
            placed_count += 1
        for x in range(4):
            if tchanger[i] == kchanger[x]:
                right_count = right_count+1

    clue = {
        "placed": placed_count,
        "right": right_count
    }

    return clue
