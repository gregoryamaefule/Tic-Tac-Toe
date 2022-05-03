from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None],[None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])

def condition():
    if session["board"][0][0] == session["board"][0][1] == session["board"][0][2] == "X" or session["board"][0][0] == session["board"][0][1] == session["board"][0][2] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))

    elif session["board"][1][0] == session["board"][1][1] == session["board"][1][2] == "X" or session["board"][1][0] == session["board"][1][1] == session["board"][1][2] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))
    
    elif session["board"][2][0] == session["board"][2][1] == session["board"][2][2] == "X" or session["board"][2][0] == session["board"][2][1] == session["board"][2][2] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))

    elif session["board"][0][0] == session["board"][1][0] == session["board"][2][0] == "X" or session["board"][0][0] == session["board"][1][0] == session["board"][2][0] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))

    elif session["board"][0][1] == session["board"][1][1] == session["board"][2][1] == "X" or session["board"][0][1] == session["board"][1][1] == session["board"][2][1] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))
    
    elif session["board"][0][2] == session["board"][1][2] == session["board"][2][2] == "X" or session["board"][0][2] == session["board"][1][2] == session["board"][2][2] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))

    elif session["board"][0][0] == session["board"][1][1] == session["board"][2][2] == "X" or session["board"][0][0] == session["board"][1][1] == session["board"][2][2] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))
    
    elif session["board"][0][2] == session["board"][1][1] == session["board"][2][0] == "X" or session["board"][0][2] == session["board"][1][1] == session["board"][2][0] == "Y":
        for i in session["board"]:
            for j in range(3):
                if i[j] == None:
                    i[j] = ' '
                else:
                    continue

        return redirect(url_for("index"))

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    if session["turn"] == "X":
        session["board"][row][col] = "X"
        session["turn"] = "Y"
        condition()
    else:
        session["board"][row][col] = "Y"
        session["turn"] = "X"
        condition()
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    session["board"] = [[None, None, None],[None, None, None], [None, None, None]]
    session["turn"] = "X"
    return render_template("game.html", game=session["board"], turn=session["turn"])
