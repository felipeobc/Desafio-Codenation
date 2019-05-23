
import hashlib

import requests
import string
import json

ACCESS_TOKEN = input('099bb428faac4b5fa39b8514f789502a1a779258')

CHALLENGE_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}'.format(ACCESS_TOKEN)
SUBMIT_CHALLENGE_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={}'.format(ACCESS_TOKEN)

response = requests.get(CHALLENGE_URL)
response = response.json()

steps = response['numero_casas']
text = response['cifrado']

class ExerciseSolver:

    def __init__(self, steps, text):
        self.steps = steps
        self.text = text
        self.deciphered_text = self.decipher_text()

    def decipher_text(self):        
        response = ''
        for token in self.text.lower():
            if token in string.ascii_letters:
                response += string.ascii_letters[
                    (string.ascii_letters.index(token) - self.steps) % len(string.ascii_letters)
                ]
            else:
                response += token
        return response.lower()

    def get_text_hash(self):
        return hashlib.sha1(self.deciphered_text.encode()).hexdigest()

    def solve(self):
        return {
            'numero_casas': self.steps,
            'token': ACCESS_TOKEN,
            'cifrado': self.text,
            'decifrado': self.deciphered_text,
            'resumo_criptografico': self.get_text_hash()
        }

solution = ExerciseSolver(steps, text).solve()

print(json.dumps(solution, indent=2))

with open('answer.json', 'w') as f:
    json.dump(solution, f)

user_response = input('Deseja realmente enviar a solução ? (s/n)')
if user_response == 's':
    response = requests.post(SUBMIT_CHALLENGE_URL, files={
        'answer': open('answer.json', 'r')
    })
    print(response.json())