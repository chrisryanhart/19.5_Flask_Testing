from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # docTests or Unittest

    def test_generate_board():
        # should confirm there are 5 rows and columns

    
    def test_dislay_board():
        # should confirm board sent to browser

    def test_make_guess():



    def get_form_value():
        # should verify value is obtained from form


    def send_result():
        # should verify if word exists
        # should send response to browser


    def update_score():
        # should handle score and player information from browser at end of game
















@app.route('/')
def generate_board():


@app.route('/')
def display_board():



@app.route('/')
def make_guess():
    # add form for user to make guess
    # send guess to server
    # use AJAX. Cannot refresh page


@app.route('/')
def get_form_value():
    # confirm word is valid

@app.route('/')
def send_result():
    # send OK/NG message to front-end
    # may combine with update_score

@app.route('/')
def update_score():
    # send score to front-end