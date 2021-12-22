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
@app.route("/",methods=['GET','POST'])
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
    return render_template('goWalk.html')

@app.route("/snack")
def enterSnack():
    return render_template('snack.html')

@app.route("/ending")
def enterEnding():
    return render_template('ending.html')


if __name__ == "__main__":
    app.run(debug=True)
