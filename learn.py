from random import sample
from random import randint

teacher = ['장용석', '늘한', '몰랑이는 귀여워']

def learn(boss, students):
    num = randint(0, 2)
    d_teacher = teacher[num]
    print("\n흠..어떤 걸 시키지??")
    print("(1) 인강 듣기    (2) '{0}'의 강의 듣기    (3) '정성모' 따라하기")  # teacher 변수 필요

    num = input('입력: ')  # input 예외처리 필요

    # 어떤걸 시킬지에 따라 학생들의 능력치 변화
    if num == '1':
        online_lec(students)
    elif num == '2':
        offline_lec(students, d_teacher)
    elif num == '3':
        follow_boss(students)


# learn의 datail action
def online_lec(students):
    print("\n회장님: 인강 듣자")
    print('''
       ■■■■■■■■■■■■■■
       ■    코딩     ■
       ■    도장     ■
       ■■■■■■■■■■■■■■
           /    \\
    ''')
    index = sample(list(range(len(students))), randint(1, len(students)))
    for i in index:
        students[i].st_coding += 10
        students[i].st_fatigue += 3
        students[i].st_humanity -= 2
        students[i].st_passion -= 3



def offline_lec(students, d_teacher):# 누구의 강의인지에 따라 학생들의 능력치 변화
    if d_teacher == '장용석':
        print('\n학생들: (웅성웅성){} 강사님 잘생겼다~~'.format(d_teacher))
        index = sample(list(range(len(students))), randint(1, len(students)))
        for i in index:
            students[i].st_coding += 8
            students[i].st_fatigue += 3
            students[i].st_humanity -= 1
            students[i].st_passion += 3
    elif d_teacher == '늘한':
        print('\n질문방 네임드 {} 등장!! '.format(d_teacher))
        index = sample(list(range(len(students))), randint(1, len(students)))
        for i in index:
            students[i].st_coding += 5
            students[i].st_fatigue += 2
            students[i].st_humanity -= 2
            students[i].st_passion += 4
    elif d_teacher == '몰랑이는 귀여워':
        print('\n학생들: 앗, 저분은 질문방의 몰랑이...귀여워')
        index = sample(list(range(len(students))), randint(1, len(students)))
        for i in index:
            students[i].st_coding += 20
            students[i].st_fatigue -= 3
            students[i].st_humanity += 4
            students[i].st_passion += 3


def follow_boss(students):
    print("\n회장님: 저를 따라해보세요~여기보세요~")
    index = sample(list(range(len(students))), randint(1, len(students)))
    for i in index:
        students[i].st_coding += 5
        students[i].st_fatigue += 1
        students[i].st_humanity += 3
        students[i].st_passion -= 4
