

import sys
sys.path.append('../')


from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from breadcrumb import Breadcrumb,BreadcrumbOl,BreadcrumbLi


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    bread= BreadcrumbLi("Home",_class="breadcrumb-item")
    bread2 =BreadcrumbLi("About",_class="breadcrumb-item active",aria_current="page")

    breadol = BreadcrumbOl(str(bread.render()) + str(bread2.render()), _class="breadcrumb")
    bread_ = Breadcrumb(str(breadol.render()),_class="")

    return render_template("main.html",alert=bread_)

if __name__ == "__main__":
    app.run(debug=True)







