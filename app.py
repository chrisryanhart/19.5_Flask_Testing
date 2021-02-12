# don't allow the same word to be counted twice

from boggle import Boggle
from flask import Flask, session, request, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension


boggle_game = Boggle()

app=Flask(__name__)
app.config['SECRET_KEY']='secret'
app.config['TESTING']=True
app.config['DEBUG_TB_HOSTS']=["dont-show-debug-toolbar"]

debug=DebugToolbarExtension(app)


# start new game, make board, retrieves high score/ games played
@app.route('/')
def start_game():
    board = boggle_game.make_board()
    session['board']=board

    keys = session.keys()


    if "gameCount" in keys:
        gameCount=session["gameCount"]
    else:
        session["gameCount"]=0

    if "score" in keys:
        score=session["gameCount"]
    else:
        session["score"]=0

    score=session["score"]
    gameCount=session["gameCount"]

    return render_template('boardDisplay.html', board=board, gameCount=gameCount, score=score)


# checks if word is valid and returns result
@app.route('/evaluatedValue', methods=['POST'])
def evaluate_value():
    
    board=session['board']
    word=request.json['word']

    word_result=boggle_game.check_valid_word(board, word)

    response = {"result": f"{word_result}"}

    return jsonify(result=word_result)
                    

# saves high score and game count to session.  Returns updated high score.
@app.route('/gameEnd', methods=["POST"])
def send_result():

    gameCount=session["gameCount"]+1
    session["gameCount"]=gameCount

    new_score = int(request.json["score"])
    old_score = session["score"]

    if new_score > old_score:
        session["score"] = new_score
        
    updated_score = session["score"]

    return f"High Score is {updated_score}"

