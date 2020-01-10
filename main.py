from login import *
from learn import *
from event2_Lunch import *
from homework_event import *
from gohome import *
from student import escape

boss, students = login()
avg_ability = make_avgdict(students)
finish = True
week = 1

print("\n\n------안녕하세요. '{0}'의 피로 키우기에 오신것을 환영합니다.------##\n" .format(boss.b_name))
print("##{0}님은 28명의 피로그래밍12기를 8주 동안 낙오자없이 데려가야합니다.##\n"
      "##학생들이 '{0}님을 잘 따를 수 있도록 리더십을 발휘하세요!\n".format(boss.b_name))
while finish:
    select = 0
    repeat = True
    print("                 Week {0} - P'rogramming 12th\n[12기의 평균 능력치] - 열정: {1}%, 피로감: {2}%, 코딩력: {3}%, 인류애: {4}%\n"
          .format(week, avg_ability['avg_passion'], avg_ability['avg_fatigue'], avg_ability['avg_coding'], avg_ability['avg_humanity']))
    while repeat:
        print('(1) 강의하기    (2) 밥먹이기    (3) 과제내기    (4) 집보내기    (0) 종료')
        select = input('입력: ')
        if select == '0':
            finish = False
            continue
        elif select == '1':
            learn(boss, students)
        elif select == '2':
            lunch(boss, students)
        elif select == '3':
            homework(students)
        elif select == '4':
            change = gohome(boss, students, avg_ability['avg_passion'])
            avg_ability['avg_passion'] = change
            repeat = False
        else:
            print('ERROR: 잘못된 번호를 선택하였습니다.\n\n')

    escape(students)
    week += 1
