import requests


class QuestionData:

    def __init__(self, difficulty):

        if difficulty == "easy":
            response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')
        elif difficulty == "medium":
            response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean')
        elif difficulty == "hard":
            response = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=hard&type=boolean')
        else:
            response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=boolean')

        self.data = response.json()
        #response = html.unescape(response)
        #self.data = json.dumps(response)
