from flask import *
import string

app = Flask(__name__)

@app.route('/')
def index():
    abort(401)

@app.route("/<path:name>")
def user(name):
    banChar = ["~", "//", ".."]
    ret = False
    for char in banChar:
        if char in name:
            ret = True

    if ret:
        abort(403)
    try:
        if name.endswith(".css"):
            return send_from_directory('static/css', name)
        return render_template(name), 200
    except:
        abort(404)   

@app.errorhandler(401)
def forbidden(e):
    return render_template("401.html"), 401

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')
