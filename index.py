from flask import Flask
from flask import render_template
import os
app=Flask(__name__)


    
@app.route("/")
def law():
    return render_template('index.html', title='Law')

@app.route("/representation")
def second():
    return render_template('secondpage.html', title='Law')

@app.route("/outsourcing")
def third():
    return render_template('thirdpage.html', title='Law')

if __name__ == '__main__':
    app.run(debug=True)