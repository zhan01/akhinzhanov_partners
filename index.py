from flask import Flask
from flask import render_template
import os
app=Flask(__name__)


    
@app.route("/")
def law():
    return render_template('index.html', title='Law')



if __name__ == '__main__':
    app.run(debug=True)