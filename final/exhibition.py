from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dblogin                  # 'dbsparta'라는 이름의 db를 만듭니다.


db.users.insert_one({'id':'mijung','password':8548})
user = db.users.find()
admin_id=user[0]['id']
admin_password = user[0]['password']

articles = []
informations = []
num=1

@app.route('/deletein')
def deletein():
   return render_template('delete.html')

@app.route('/login')
def mypage():
   return render_template('login.html')

@app.route('/click')
def click():
   return render_template('local-click.html')
   
@app.route('/click1')
def click1():
   return render_template('디뮤지엄.html')

@app.route('/login/admin')
def admin():
   return render_template('admin.html')

@app.route('/')
def local():
   return render_template('local.html')

## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def post():
   global articles               # 이 함수 안에서 나오는 articles 글로벌 변수를 가리킵니다.

   id_receive = request.form['id_give']          # 클라이언트로부터 url을 받는 부분
   password_receive = request.form['password_give']  # 클라이언트로부터 comment를 받는 부분

   article = {'id':id_receive,'password':password_receive} # 받은 걸 딕셔너리로 만들고,

   articles.append(article)   # 넣는다

   return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def view():
   return jsonify({'result':'success', 'id':admin_id, 'password':admin_password})


# # 데이터 입력
@app.route('/push', methods=['POST'])
def push():
   global informations        # information 
   global num
   x_receive = request.form['x_give']
   y_receive = request.form['y_give']
   name_receive = request.form['name_give']
   date_receive = request.form['date_give']
   explain_receive = request.form['explain_give']
   locate_receive = request.form['locate_give']
   age_receive = request.form ['age_give']
   theme_receive = request.form ['theme_give']
   link_receive = request.form ['link_give']   
   img_receive = request.form['img_give']
   information = {'x':x_receive, 'y':y_receive, 'img':img_receive,
   'num':num, 'name':name_receive, 'date':date_receive,
   'explain':explain_receive,'locate':locate_receive, 'age':age_receive,
    'theme':theme_receive, 'link':link_receive}
   num = num+1;
   
   db.informations.insert_one(information)

   
   return jsonify ({'result':'success'})
# def remove():
#    global informations
#    no_receive = request.form['no_give']
#    db.informations.remove({'num': no_receive})  
   # informations.append(information)

   

@app.route('/push', methods=['GET'])
def pop():
   global informations
   pops = db.informations.find({},{'_id':0})
   return jsonify({'result':'success', 'informations':list(pops)})


   
@app.route('/delete', methods = ['POST'])
def delete():
   global informations
   no_receive = request.form['no_give']

 
   result = db.informations.delete_one({'num':int(no_receive)})

   return jsonify({'result':'success'})



if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)