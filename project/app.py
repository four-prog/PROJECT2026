import mysql.connector
from flask import Flask,render_template,request,redirect
import requests



app=Flask(__name__)

#SQL CONNECTION
db=mysql.connector.connect(
     host="mysql-2b94466e-project-eaec.d.aivencloud.com",
    user="avnadmin",
    password="AVNS_vKXV37n4YtvusG8hhfQ",
    database="project",
    port="27573"
    
)
if db.is_connected:
        print("success")
else:
        print("wrong")


#MSG CONNECTION

#REGISTER PAGE
@app.route('/')
def index():
    return render_template('register.html')



#LOGIN PAGE
@app.route('/login')
def login():
    return render_template('login.html')




@app.route('/success',methods=['POST'])
def success():
    try:
        email=request.form['email']
        password=request.form['password']
        print(email,password)
        cursor=db.cursor()
        sql="INSERT INTO auth VALUES(%s,%s)"
        values=(email,password)
        cursor.execute(sql,values)
        db.commit()
        cursor.close
    except:
         return render_template('already.html')
    return render_template('success.html')


#STUDENTS INFORMATION
@app.route('/table')
def table():
    cursor=db.cursor()
    
    cursor.execute("SELECT REG_NO,NAME,CLASS FROM students ORDER BY REG_NO")
    results=cursor.fetchall()
    
    return render_template('table.html',results=results)


@app.route('/added',methods=['POST'])
def added():
   name=request.form['uname'].upper()
   try:
    reg=int(request.form['unumber'])
   except ValueError:
        return "</h2>check your register number</h2>"
   phone=request.form['phone']
   clas=request.form.get('class')
   #print(name,reg,phone,clas)

    

   try:
#mysql connection:
       cursor=db.cursor()
       SQL=("INSERT INTO students VALUE(%s,%s,%s,%s)")
       values=(reg,name,clas,phone)

       cursor.execute(SQL,values)
       db.commit()
       cursor.close()
 
       return redirect('/add')
   except mysql.connector.errors.IntegrityError:
        return "this register id alreay registered!"
   except ValueError:
        return "check your register number"
       

         
#ADD STUDENTS
@app.route('/add')
def add():
   return render_template('add.html')


#DELETE STUDENTS
@app.route('/deleted',methods=['POST'])
def deleted():
    reg=request.form['regno']
    print(reg)
    cursor=db.cursor()

    sql=("DELETE FROM students WHERE REG_NO = %s")
    values=(reg,)

    cursor.execute(sql,values)
    db.commit()
    cursor.close()

    return redirect('/delete')



@app.route('/delete')
def delete():
    return render_template('delete.html')




@app.route('/show')
def show():

    cursor=db.cursor()

    cursor.execute("SELECT*FROM auth")

    result=cursor.fetchall()

    
    print(result)
    
    return render_template('index.html',result=result)



@app.route('/logined',methods=['POST'])
def logined():
    id=request.form['email']
    password=request.form['password']
    result1=(id,password)
    cursor=db.cursor()

    sql="SELECT*FROM auth WHERE EMAIL=%s"
    value=(id,)
    
    cursor.execute(sql,value)
   
    result=cursor.fetchone()

    cursor.close()

    print(result)
    if result==result1:
           return redirect('/home')
    elif result is None:
         return "not registered"
    else:
        return render_template('failed.html')


@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/soon')
def soon():
    return "<h2>Comming Soon</h2>"

    
    
@app.route('/msg',methods=['POST'])
def msg():
    result=request.form.getlist('checkbox')

    cursor=db.cursor()

    sql="SELECT PHONE_NO FROM students WHERE REG_NO=%s"

    for i in result:
        value=(i,)
        cursor.execute(sql,value)
        final=cursor.fetchone()

        print(final)
       
   
    
        

        data = {
            "channel": "sms",
            "e164From": "+919865987602",
            "to": str(final) ,
            "message": "hi."
        }

        response = requests.post(
            url,
        headers=headers,
         json=data
        )
        print(response.status_code)
    return render_template('msgsuccess.html')


if __name__=="__main__":
       # app.run(debug="true")
       app.run(host="0.0.0.0",port=5000,debug="true")



db.close()
