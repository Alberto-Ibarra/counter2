from flask import Flask, render_template, request,  redirect, session


app = Flask(__name__)
app.secret_key = "12345"

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    
    return render_template("index.html")




# @app.route('/counter')
# def counter():
#     session['counter'] += 1
#     return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)