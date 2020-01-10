from login import *

boss, students = login()
avg_ability = make_avgdict(students)
finish = True

index = {
    '1': None,
    '2': None,
    '3': None,
    '4': None
}

print('------안녕하세요. {0}의 피로 키우기에 오신것을 환영합니다.------' .format(boss.b_name))
while finish:
    select = 0

    print('(1) 강의하기    (2) 밥먹이기    (3) test3    (4) test4    (0) 종료')
    select = input('입력: ')
    if select == '0':
        break
    index[select]




