import requests


class QuestionData:

    def __init__(self):
        self.data = ""

    def video_games(self):
        response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=boolean')
        self.data = response.json()

    def music(self):
        response = requests.get('https://opentdb.com/api.php?amount=10&category=12&type=boolean')
        self.data = response.json()

    def science_nature(self):
        response = requests.get('https://opentdb.com/api.php?amount=10&category=17&type=boolean')
        self.data = response.json()

    def computer_science(self):
        response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
        self.data = response.json()
