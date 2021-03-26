from flask import Flask, render_template, redirect, request
from flask.globals import request
from forms import SignUpForm

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

################## NEW ########################
import algoImp as al
################## NEW ########################



app = Flask(__name__)
app.config['SECRET_KEY'] = 'guacbanana'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userEntry2.db'
db = SQLAlchemy(app)

#go back to here for for loops, to loop through the program and print it to the page https://www.youtube.com/watch?v=xh3mFxbnc4o&list=PLB5jA40tNf3vX6Ue_ud64DDRVSryHHr1h&index=4

@app.route('/')
def home():
    return (render_template('homepage.html'))

#@app.route('/about')
#def about():
#    return (render_template('about.html', author="Jerry", sunny=False))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form

        """
        try:
            #sqlExe = "INSERT INTO userInfo({},{},{},{});".format(result.get("first_name"), result.get("last_name"), result.get("email"),result.get("sport"))
            #print(sqlExe)
            sqlExe = 'INSERT INTO "main"."userInfo"("first_name","last_name","email","sport") VALUES ("{}","{}","{}","{}");'.format(result.get("first_name"), result.get("last_name"), result.get("email"),result.get("sport"))
            db.session.execute(sqlExe)
            db.session.commit()

            print("Your info was successfully added")

        except Exception as e:
            print("Your query couldn't be inserted into the databse because: {}".format(e))


        #print(result)
        return render_template('user.html', result=result)

        """
        wk = al.workoutGen()
        wkls = None
        while(True):
            try:
                wkls = wk.generator(result.get("sport").lower())
                break
            except:
                pass

        wk1,wk2 = wk.formatter(wkls.wk)

        #print(wk1,wk2)
        
        return render_template('display.html', wk1=wk1, wk2=wk2, fName = result.get("first_name"), lName = result.get("last_name"), email = result.get("email"))


    return render_template('signup.html', form=form)

    #pass the arrays into the html page as variables as jinja. Reference the about page

@app.route('/retrieve')
def retrieve():
    return (render_template('retrieve.html'))

if __name__ == '__main__':
    app.run()

