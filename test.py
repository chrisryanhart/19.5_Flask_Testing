from unittest import TestCase
from app import app
from flask import session
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
            


    def test_evaluate_value(self):
        # should verify value is obtained from form
        # should return result if word was OK/NG
        with app.test_client as client:
            resp = client.post("http://127.0.0.1:5000/evaluatedValue", data = {"word": "word"})
            html = resp.get_data(as_text=True)

            import pdb
            pdb.set_trace()

            self.assertEqual(resp.status_code, 200)


    def test_update_score(self):
        with app.test_client as client:
            resp = client.post("http://127.0.0.1:5000/gameEnd", data={"score": 5})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
        # should handle score and player information from browser at end of game
        # should return string with high score






    
    # def test_dislay_board():
    #     # should confirm board sent to browser

    # def test_make_guess():



    # def get_form_value():
    #     # should verify value is obtained from form


    # def send_result():
    #     # should verify if word exists
    #     # should send response to browser


















