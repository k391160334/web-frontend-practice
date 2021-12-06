from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)
userName=''
age=0
snack=''
gender=''
mbti=''

@app.route("/",methods=['GET','POST'])
def home():
    #return render_template('index.html', user="", data={'age':, 'snack':, 'gender':})
    if request.method=='GET':
        # 먼저 화면을 띄우고 user와 data를 입력받음
        return render_template('index.html')
    else:
        # 입력받은 데이터를 전역변수에 저장
        global userName,age,snack,gender
        userName=request.form['user']
        age=request.form['age']
        snack=request.form['snack']
        gender=request.form['gender']
        # startGame 페이지 띄우기
        return redirect(url_for('menu_table',_external=True))

@app.route("/menu_table")
def menu_table():
    return render_template('menu_table.html')

@app.route("/meal")
def enterMeal():
    return render_template('meal.html')

if __name__ == "__main__":
    app.run(debug=True)
