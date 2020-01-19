

import sys
sys.path.append('../')


from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from alert import Alert
from button import Button


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
 
    button = Button("click me !",_class="btn btn-primary").render()    
    alert = Alert("successfull login! ",_class ="alert alert-danger")


    

    return render_template("main.html",alert=alert)

if __name__ == "__main__":
    app.run(debug=True)







