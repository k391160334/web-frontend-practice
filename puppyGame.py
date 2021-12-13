
import random


class Dog:
    def __init__(self,name):
        l1 = ['E', 'I']
        l2 = ['S', 'N']
        l3 = ['T', 'F']
        l4 = ['P', 'J']
        self.mbti = random.choice(l1) + random.choice(l2) + random.choice(l3) + random.choice(l4)
        self.dog_name=name
    def getname(self):
        return self.dog_name
    def getmbti(self):
        return self.mbti

class Main_story:
    def __init__(self):
        print("Game start!!")
        self.player_name=input("플레이어 이름을 입력하세요: ")
        dog_name=input("강아지 이름을 입력하세요: ")
        self.dog=Dog(dog_name)
        self.intro()
    def intro(self):    #menu_table에 포함
        print("\n당신과 오늘 함께할 강아지 {}입니다.".format(self.dog.getname()))
        print("나이: {}".format(3))
        print("좋아하는 간식: {}".format("뼈다귀"))
        print("성별: {}\n".format("여"))
        print("오늘 일정이 모두 끝나면 {}(을)를 입양해가시기 위한 간단한 테스트가 있으니 {}(이)의 성향을 잘 파악해 보시길 바랍니다.".format(self.dog.getname(),self.dog.getname()))
        print("그럼 {}(이)와 오늘 하루 즐거운 시간 보내시기를 바랍니다.".format(self.dog.getname()))
        self.menu_table()
    def menu_table(self):
        print("\n1. 밥 주기")
        print("2. 산책하기")
        print("3. 간식주기")
        print("0. 종료하기")
        index=int(input("{}(이)와 함께할 활동을 고르세요: ".format(self.dog.getname())))
        if index==1:
            self.Meal()
        elif index==2:
            self.Go_walk()
        elif index==3:
            self.Snack()
        elif index==0:
            self.Ending()
        else:
            print("\nindex를 잘못 입력하셨습니다.")
            self.menu_table()

    def Meal(self):
        # 밥 주는 그림 그려주기.
        print("\n{}(이)에게 밥을 줍니다.".format(self.dog.getname()))   #meal.html
        print("\n{}: ".format(self.dog.getname()),end="")
        meal=feed(self.dog.getmbti())
        meal.feedstart()                                               #feedStart.html, js
        print("\n{}(이)가 밥을 먹기 시작합니다.".format(self.dog.getname()))
        print("1. 계속 서서 강아지가 밥 먹는 모습을 바라본다.")
        print("2. {}(이)가 편하게 밥먹을 수 있도록 다른 일을 한다.".format(self.dog.getname()))
        a=int(input("Enter: "))
        if a==1:
            print("\n{}: ".format(self.dog.getname()),end="")
            meal.act()
        print("\n{}(이)가 밥을 다 먹었습니다.".format(self.dog.getname()))
        self.menu_table()
    def Go_walk(self):
        print("\n{}: ".format(self.dog.getname()),end="")
        gowalk=walk(self.dog.getmbti())
        gowalk.walkstart()
        print("\n{}(이)가 빨리 가기 시작합니다. 당신의 행동을 선택하세요.".format(self.dog.getname()))
        print("1. {}(이)에게 말걸기".format(self.dog.getname()))
        print("2. 목줄 당기기")
        print("3. 그냥 가기")
        a=int(input("Enter: "))
        if a==1:
            print("\n{}: ".format(self.dog.getname()),end="")
            gowalk.say()
        if a==2:
            print("\n{}: ".format(self.dog.getname()),end="")
            gowalk.rope()
        print("\n{}(이)와 산책을 하던 도중 예쁜 공원이 나왔습니다.".format(self.dog.getname()))
        print("1. 사진찍기")
        print("2. 그냥 가기")
        b=int(input("Enter: "))
        if b==1:
            print("\n{}: ".format(self.dog.getname()),end="")
            gowalk.photo()
        print("\n공원을 거닐다 다른 강아지를 만났습니다.")
        print("다른 강아지의 주인이 {}(을)를 칭찬합니다. 당신의 반응을 고르세요".format(self.dog.getname()))
        print("1. 맞아요~~ 하면서 동의한다.")
        print("2. 에이~ 그정도는 아니에요. 하면서 부정한다.")
        c=int(input("Enter: "))
        if c==1:
            print("\n{}: ".format(self.dog.getname()),end="")
            gowalk.agree()
        if c==2:
            print("\n{}: ".format(self.dog.getname()),end="")
            gowalk.disagree()
        print("\n다른 강아지의 주인이 함께 산책하는 것이 어떻냐고 묻습니다.")
        print("1. 함께 산책하기")
        print("2. 거절하기")
        d=int(input("Enter: "))
        if d==1:
            print("\n{}: ".format(self.dog.getname()),end="")
            gowalk.friend()
        elif d==2:
            print("\n{}: ".format(self.dog.getname()),end="")
            gowalk.alone()
        print("\n저녁 시간이 다가옵니다. {}(을)를 데리고 집으로 돌아갑니다.".format(self.dog.getname()))
        print("\n{}: ".format(self.dog.getname()),end="")
        gowalk.home()
        self.menu_table()

    def Snack(self):
        print("\n{}(이)에게 간식을 줍니다.".format(self.dog.getname()))
        print("\n{}: ".format(self.dog.getname()),end="")
        feed_snack=feed(self.dog.getmbti())
        feed_snack.snack()
        self.menu_table()
    def Ending(self):
        print("\n오늘 하루는 즐거우셨나요?")
        print("{}(이)를 데려가기 위한 마지막 절차가 남았습니다.".format(self.dog.getname()))
        print("정답을 맞추실 경우에만 {}(을)를 입양해 가실 수 있습니다.".format(self.dog.getname()))
        print("퀴즈를 시작합니다.")
        print("\n{}(이)의 성격을 맞추세요!".format(self.dog.getname()))
        print("{}(이)는 외향형 일까요 내향형 일까요? (내향형: I, 외향형: E)".format(self.dog.getname()))
        a=input("Enter: ")
        print("{}(이)는 현실적 일까요 상상력이 풍부할까요? (현실적: S, 상상력: N)".format(self.dog.getname()))
        b=input("Enter: ")
        print("{}(이)는 이성적 일까요 감성적 일까요? (이성적: T, 감성적: F)".format(self.dog.getname()))
        c=input("Enter: ")
        print("{}(이)는 계획적 일까요 즉흥적 일까요? (계획적: J, 즉흥적: P)".format(self.dog.getname()))
        d=input("Enter: ")
        answer=a+b+c+d
        if self.dog.getmbti()==answer:
            self.Correct()
        else:
            self.Wrong()
    def Correct(self):
        print("\n정답입니다!!!")
        print("{}(이)를 데려가실 수 있습니다. 축하드립니다!!".format(self.dog.getname()))
        # 특별 보너스컷 출력
        self.Quit()
    def Wrong(self):
        print("\n오답입니다..")
        print("아쉽게도 {}이를 데려가실 수 없습니다. 다른 인연을 찾으시길 바랍니다.".format(self.dog.getname()))
        self.Quit()
    def Quit(self):
        print("\n1. 재시작하기.")
        print("2. 게임 종료하기.")
        index=int(input("Enter: "))
        if index==1:
            Main_story()

class walk():
    def __init__(self,mbti):
        self.mbti = mbti

    def walkstart(self):
        if self.mbti[0] == 'E':
            print('산책 너무 좋아~\n빨리 밖에 나가고 싶었어!!')
        else:
            print('음. 집에서 쉬고 싶었는데...\n밖에 나가는 것도 괜찮지...ㅎㅎ')

    def say(self):
        if self.mbti[2] == 'T':
            print('뭐라는거야?\n간식 주려고?')
        else:
            print('내가 너무 빨리 가나?\n힘들었구나!')
    def rope(self):
        if self.mbti[2] == 'T':
            print('줄 땡기지 말고 늘려!\n힘드니?')
        else:
            print('아이고, 힘들었나보네!')

    def photo(self):
        if self.mbti[1] == 'S':
            print('인스타 올리려고?\n인스타 중독이다...')
        else:
            print('인스타 올리려고?\n이러다 인스타 스타 강아지 되는거 아님?\n막 간식 협찬도 들어오고, 방송출연도 하고,\n약간 피곤해지겠지만 좋을 것 같은데')

    def friend(self):
        if self.mbti[0] == 'E':
            print('오예! 친구랑 같이 산책한다~')
        else:
            print('부끄럽긴한데...\n같이 산책하지 뭐')
    def alone(self):
        if self.mbti[0] == 'E':
            print('같이 산책 하고 싶었는데...')
        else:
            print('혼자 산책이 편하지~')

    def agree(self):
        if self.mbti[1] == 'S':
            print('나 보고 하는 말 아닌 것 같은데?\n이 친구 현실 감각이 없구먼~')
        else:
            print('역시 난 인스타 스타가 될 강아지야~ 훗!')
    def disagree(self):
        if self.mbti[1] == 'S':
            print('그러게 현실적으로 보면\n나한테 하는 말이 아닐텐데~')
        else:
            print('당연히 나보고 하는 말이잖아!!\n인스타 스타가 될 강아지를 알아보시네~')

    def home(self):
        if self.mbti[3] == 'P':
            print('집에가면 뭐하지?\n무계획 인생~')
        else:
            print('짐에가서 저녁 먹으면\n딱이겠다!')

class feed():
    def __init__(self,mbti):
        self.mbti = mbti

    def feedstart(self):
        if self.mbti[0] == 'E':
            print('좋아\n!!')
        else:
            print('부담스러워서 못 먹겠어ㅜㅜ')

    def act(self):
        if self.mbti[2] == 'F':
            print('주인이심심한가봐\n내가 놀아줘야징')
        else:
            print('밥 먹는데 걸리적거리게\n왜 서있는거야!')
    def snack(self):
        if self.mbti[2] == 'S':
            print('와 맛있는 냄새다!!')
        else:
            print('이거 하면 간식 더 주겠지?')


Main_story()
