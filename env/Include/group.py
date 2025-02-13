from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'



@app.route("/<dob>")
def generation(dob):
    age=int(dob)
    if 1981<age<1996:
        return {'Generation':'Gen Y',
                'Age':age
        }
    elif 1997<age<2012:
        return {'Generation':'Gen Z',
                'Age':age
        }
    else:
        return {'Generation':'Aplha',
                'Age':age
        }

