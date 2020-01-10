from login import *
from learn import *
from event2_Lunch import *
from homework_event import *

boss, students = login()
avg_ability = make_avgdict(students)
finish = True



print('\n\n------안녕하세요. {0}의 피로 키우기에 오신것을 환영합니다.------' .format(boss.b_name))
while finish:
    select = 0

    print('(1) 강의하기    (2) 밥먹이기    (3) test3    (4) test4    (0) 종료')
    select = input('입력: ')
    if select == '0':
        break
    elif select == '1':
        learn(boss, students)
    elif select == '2':
        lunch(boss, students)
    elif select == '3':
        homework(students)
    elif select == '4':
        pass
    else:
        print('ERROR: 잘못된 번호를 선택하였습니다.')



