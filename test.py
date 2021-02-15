from unittest import TestCase
from app import app
from flask import session, Flask
from boggle import Boggle

app.config['DEBUG_TB_HOSTS']=["dont-show-debug-toolbar"]

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # docTests or Unittest
    def setUp(self):

        app.config["TESTING"] = True

    def test_start_game(self):
        # should confirm there are 5 rows and columns
        # should assign/share session values for record score and games played
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(b'<p>Current Score',resp.data)
            self.assertEqual(0,session.get('gameCount'))
            self.assertEqual(0,session.get('score'))

    def test_evaluate_value(self):
        # should verify value is obtained from form
        # should return result if word was OK/NG
        with app.test_client() as client:
            with client.session_transaction() as sess:
            
            # from solution
            # board = session['board']
                board=[['C','A','T','T','T'],
                ['C','A','T','T','T'],
                ['C','A','T','T','T'],
                ['C','A','T','T','T'],
                ['C','A','T','T','T'],
                ]
                sess['board']=board
            # sess['board']=board

            resp = client.post("/evaluatedValue", json={"word": 'cat'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json['result'],'ok')


    def test_update_score(self):
        with app.test_client() as client:
            
            # do I have a session value, if not then need to assign
            # use session.get
            # score = session.get('score')
            resp = client.post("/gameEnd", json={"score": 5})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("gameCount", session)
            self.assertIn(b'5',resp.data)

        # should handle score and player information from browser at end of game
        # should return string with high score

# import json
# from unittest.mock import patch




    
    # def test_dislay_board():
    #     # should confirm board sent to browser

    # def test_make_guess():



    # def get_form_value():
    #     # should verify value is obtained from form


    # def send_result():
    #     # should verify if word exists
    #     # should send response to browser


















