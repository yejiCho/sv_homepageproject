from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

informations = []
privacys = []

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/login/admin')
def admin():
   return render_template('admin.html')


@app.route('/push', methods=['POST'])
def push():
   global privacys

   id_receive = request.form['id_give']
   pwd_receive =  request.form['pwd_give']

   privacy = {'id':id_receive, 'pwd':pwd_receive}

   privacys.append(privacy)

   return jsonify({'result':'success'})

@app.route('/push', methods=['GET'])
def pop():
   global privacys
   return jsonify({'result':'success', 'privacys':privacys})


@app.route('/post', methods=['POST'])
def post():
   global informations        # information 

   title_receive = request.form['title_give']
   img_receive = request.form['img_give']
   comment_receive = request.form['comment_give']
   local_receive = request.form['local_give']
   age_receive = request.form['age_give']
   latitude_receive = request.form['latitude_give']
   longitude_receive = request.form['longitude_give']

   information = {'title':title_receive, 'img':img_receive,
      'comment': comment_receive, 'local':local_receive, 'age': age_receive,
      'latitude': latitude_receive, 'longitude': longitude_receive
   }

   informations.append(information)

   return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def view():
   global informations
   return jsonify({'result':'success', 'informations':informations})


@app.route('/local')
def local():
   return render_template('local.html')

@app.route('/theme')
def theme():
   return render_template('theme.html')

@app.route('/age')
def age():
   return render_template('age.html')

if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)