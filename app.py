# don't allow the same word to be counted twice

from boggle import Boggle
from flask import Flask, session, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

import app.js 

boggle_game = Boggle()


app=Flask(__name__)
app.config['SECRET_KEY']='secret'

debug=DebugToolbarExtension(app)

# add debugger


# use session throughout routes

# start new game, make board
@app.route('/')
def generate_board():
    board = boggle_game.make_board()
    session['board']=board

    # import pdb
    # pdb.set_trace()

    # loop through board
    # better to loop through in python or html

    # breakpoint or debug with VScode

    return render_template('boardDisplay.html', board=board)


@app.route('/')
def display_board():
    return


@app.route('/guess', methods=['POST'])
def make_guess():
    # send guess as text to the server?  
    # add form for user to make guess
    # send guess to server
    # use AJAX. Cannot refresh page
    # update session

    return redirect


@app.route('/evaluatedval')
def get_form_value():
    # confirm word is valid
    # give feedback to user
    # respond with jsonify

    # how to receive the form request from js

    

    return render_template('evaluateVal.html')

@app.route('/')
def send_result():
    # send OK/NG message to front-end
    # may combine with update_score
    return

@app.route('/')
def update_score():
    # send score to front-end
    return

