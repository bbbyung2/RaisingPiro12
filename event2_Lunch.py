from boss import *
from student import *
import random

'''1. 학식 2. 배달음식 3. 굶기'''

def lunch(students):
    print('오늘 점심은 뭘 먹이지?...')
    while(True):
        choice = int(input('1. 학식  2. 배달  3. 굶자\n'))
        print('------------------------------------------------')
        if choice == 1 :
            lunch_cafeteria(students)
            break
        elif choice == 2:
            lunch_delivery(students)
            break
        elif choice == 3:
            lunch_no(students)
            break
        else:
            '다시 생각해보자 성모야'


def lunch_cafeteria(students) :
    print('여러분 오늘은 학식 드세요')
    index = random.sample(list(range(len(students))), random.randint(1, len(students)))
    count = 0
    for i in index:
        students[i].st_humanity += 5
        students[i].st_fatigue -= 5
        count += 1
    print('{0}명의 인류애가 +5, 피로가 -5 되었습니다'.format(count))
    return students

def lunch_delivery(students):
    print('여러분 오늘은 배달시켜서 드세요')
    index = random.sample(list(range(len(students))), random.randint(1, len(students)))
    count = 0
    for i in index:
        students[i].st_humanity += 5
        students[i].st_fatigue -= 10
        count += 1
    print('{0}명의 인류애가 +5, 피로가 -10 되었습니다'.format(count))
    return students

def lunch_no(students):
    print('여러분 모두 굶읍시다. 우린 배고픔도 잊고 코딩할 수 있어요')
    index = random.sample(list(range(len(students))), random.randint(1, len(students)))
    count = 0
    for i in index:
        students[i].st_humanity -= 10
        students[i].st_fatigue += 5
        count += 1
    print('{0}명의 인류애가 -10, 피로가 +5 되었습니다'.format(count))
    return students
