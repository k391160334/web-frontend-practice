from flask import Flask, render_template,request,redirect,url_for
import random

app = Flask(__name__)

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
userName=''
'''age=0
snack=''
gender='''''
myDog=Dog('')
def dogToDict(d):
    return {'name':d.getname(),'mbti':d.getmbti()}

@app.route("/")
def intro():
    return render_template('intro.html')

@app.route("/home",methods=['GET','POST'])
def home():
    #return render_template('index.html', user="", data={'age':, 'snack':, 'gender':})
    if request.method=='GET':
        # 먼저 화면을 띄우고 user와 data를 입력받음
        return render_template('index.html')
    else:
        # 입력받은 데이터를 전역변수에 저장
        global userName,myDog
        userName=request.form['userName']
        myDog=Dog(request.form['dogName'])
        '''age=request.form['age']
        snack=request.form['snack']
        gender=request.form['gender']'''
        # startGame 페이지 띄우기
        return redirect(url_for('menu_table'))

@app.route("/menu_table")
def menu_table():
    print(myDog.getmbti())
    return render_template('menu_table.html',dogName=myDog.getname())

@app.route("/meal")
def enterMeal():
    choice=request.args.to_dict()
    if not choice:  #처음 밥먹일 때
        return render_template('meal.html',myDog=dogToDict(myDog))
    else:           #밥먹인 후 지켜볼지 다른거 할지 선택
        return render_template('afterMeal.html',choice=choice,myDog=dogToDict(myDog))


@app.route("/goWalk")
def enterGoWalk():
    choice=request.args.to_dict()
    if 'fastWalkBtn' in choice: #강아지가 빠르게 걸을 때
        return render_template('fastWalk.html',choice=choice,myDog=dogToDict(myDog))
    elif 'parkWalkBtn' in choice:   #공원이 나왔을 때
        return render_template('parkWalk.html',choice=choice,myDog=dogToDict(myDog))
    elif 'complimentWalkBtn' in choice:   #칭찬들었을 때
        return render_template('complimentWalk.html',choice=choice,myDog=dogToDict(myDog))
    elif 'walkTogetherBtn' in choice:   #함께 걷자고할 때
        return render_template('walkTogether.html',choice=choice,myDog=dogToDict(myDog))
    else:   #처음 산책할 때
        return render_template('goWalk.html',myDog=dogToDict(myDog))


@app.route("/snack")
def enterSnack():
    return render_template('snack.html',myDog=dogToDict(myDog))

@app.route("/ending",methods=['GET','POST'])
def enterEnding():
    if request.method=='GET':
        return render_template('ending.html',myDog=dogToDict(myDog))
    else:
        submittedRes=''
        submittedRes+='I' if 'focus' in str(request.form) else 'E'
        submittedRes+='N' if 'information' in str(request.form) else 'S'
        submittedRes+='F' if 'decision' in str(request.form) else 'T'
        submittedRes+='P' if 'live' in str(request.form) else 'J'
        if myDog.getmbti()==submittedRes:
            return render_template('correct.html',myDog=dogToDict(myDog))
        else:
            return render_template('wrong.html',myDog=dogToDict(myDog))

if __name__ == "__main__":
    app.run(debug=True)
