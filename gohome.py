import random
import time

def gohome(boss, students, avg_passion):
  print('귀가를 선택했습니다.')

  while True:
    # 커멘드 선택
    print('1. 일찍 보내기')
    print('2. 정시에 보내기')
    print('3. 늦게 보내기')
    command = input()

    ran = random.randint(1, 10)
    # 일찍 보내기
    if command == '1':
      print('회장님 : 여러분들 일찍 가세요!!')
      time.sleep(1)

      # 거절 상황1
      if avg_passion >= 80:
        print('학생들 : 싫습니다!! 아직 6시 아닌데요!!')
        time.sleep(1)
        print('회장님 : 히잉..')
        boss.b_leadership -= 3
        print('회장님의 리더십이 3 감소했습니다\n')
        time.sleep(1)
        if len(students) >= 5:
          idx_list = random.sample(range(len(students)), 5)
          for idx in idx_list:
            print('%s : (속닥속닥)아니.. 난 집에 가고 싶은데..' % students[idx].st_name)
            students[idx].st_fatigue += 10
            print('%s의 피로도가 10 증가했습니다\n' % students[idx].st_name)
        print('(공부중....)\n')
        time.sleep(5)
        for i in range(len(students)):
          students[i].st_coding += 5
        print('모든 학생들의 코딩 능력이 5 증가했습니다')
        print('\n회장님 : 이제 6시입니다..! 가세요 이제..제발..')
        time.sleep(1)

      # 거절 상황2
      elif boss.b_anger <= 10 * ran:
        print('회장님 : 뻥이지롱~ 아직 6시 아닙니다ㅎㅎ 6시까지 듣던 강의 들으시면 됩니다!')
        time.sleep(1)
        print('학생들 : (깊은 한숨)^^;')
        time.sleep(1)
        print('(공부중...)')
        time.sleep(5)
        boss.b_passion += 5
        print('회장님의 열정이 5 증가했지만...........!')
        time.sleep(1)
        dec = random.randint(1, 2)
        for i in len(students):
          students[i].st_humanity -= 5 * dec
          students[i].st_fatigue += 5 * dec
          students[i].st_passion -= 5 * dec
          students[i].st_coding += 3 * dec
        print('모든 학생들의 인류애가 %d 감소하고 열정이 %d 감소하고 피로도가 %d 증가했습니다' % (5 * dec, 5 * dec, 5 * dec))
        print('그러나 모든 학생들의 코딩능력이 %d 증가했습니다' % (3 * dec))
        time.sleep(1)
        print('회장님 : 이제 가셔도 좋습니다!!')
        time.sleep(1)

      # 바로 귀가
      else:
        print('학생들 : 수고하셨습니다!! ^ㅁ^')
        time.sleep(1)

      # 공통 귀가
      for i in range(len(students)):
        students[i].st_fatigue -= 5
      print('학생들은 귀가를 해서 피로도가 5 감소했습니다')

    # 정시에 보내기
    elif command == '2':
      print('회장님 : 여러분들 6시입니다!! 집에 가세요!!')
      time.sleep(1)

      # 거절 상황1
      if avg_passion >= 80:
        print('학생들 : 싫은데요!! 더 공부할건데요!!')
        time.sleep(1)
        print('회장님 : 히잉...')
        time.sleep(1)
        dec = random.randint(1, 2)
        boss.b_leadership -= 3 * dec
        boss.b_anger -= 4 * dec
        print("\n회장님의 리더십이 %d 감소하고 분노조절능력이 %d 감소했습니다." % (3 * dec, 4 * dec))
        if len(students) >= 5:
          idx_list = random.sample(range(len(students)), 5)
          for idx in idx_list:
            print('%s : (속닥속닥)아니.. 난 집에 가고 싶은데..' % students[idx].st_name)
            students[idx].st_fatigue += 10
            print('%s의 피로도가 10 증가했습니다\n' % students[idx].st_name)
        print('(공부중....)\n')
        time.sleep(3)
        for i in range(len(students)):
          students[i].st_coding += 3
        print('모든 학생들의 코딩능력이 3 증가했습니다')

      # 거절 상황2
      elif boss.b_anger <= 10 * ran:
        print('회장님 : 사실 여러분들에게 해드릴 얘기가 있습니다.. 제가 LA에 있었을 때...')
        print('(이야기중...)')
        time.sleep(5)
        boss.b_passion += 10
        print('회장님의 열정이 10 증가했습니다')
        dec = random.randint(1, 2)
        for i in range(len(students)):
          students[i].st_humanity -= 5 * dec
          students[i].st_fatigue += 5 * dec
          students[i].st_passion -= 5 * dec
        print('모든 학생들의 인류애가 %s 감소하고 열정이 %s 감소하고 피로도가 %s 증가했습니다' % (5 * dec, 5 * dec, 5 * dec))
        time.sleep(1)
        print('회장님 : 이제 가셔도 좋습니다!!\n')
        time.sleep(1)

      # 바로 귀가
      else:
        print('학생들 : 수고하셨습니다!! ^ㅁ^\n')
        time.sleep(1)

      # 공통 귀가
      for i in range(len(students)):
        students[i].st_fatigue -= 5
      print('학생들은 귀가를 해서 피로도가 5 감소했습니다\n')
      return avg_passion

    # 커맨드 3
    elif command == '3':
      print("회장님 : 여러분 제가 재밌는 얘기를 해드리겠습니다!! 제가 LA에 있었을 때...")
      print('(이야기중...)')
      time.sleep(3)
      boss.b_passion += 10
      print('회장님의 열정이 10 증가했습니다')
      for i in range(len(students)):
        students[i].st_humanity -= 10
        students[i].st_fatigue += 10
        students[i].st_passion -= 10
      print('모든 학생들의 인류애, 열정이 10 감소하고 피로도가 10 증가했습니다')
      time.sleep(1)
      print('회장님 : 이제 가셔도 좋습니다!!\n')
      time.sleep(1)

      for i in range(len(students)):
        students[i].st_fatigue -= 5
      print('학생들은 귀가를 해서 피로도가 5 감소했습니다')
      return avg_passion

    # 늦게 보내기
    else:
      print('삐빅!! 정신차리세요!! 다시 입력하세요!!')
      return avg_passion