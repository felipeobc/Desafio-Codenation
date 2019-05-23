import requests

info = {
    'var1' : 'this',
    'var2'  : 'that',
}

data = {
    "numero_casas": 3,
    "token": "099bb428faac4b5fa39b8514f789502a1a779258",
    "cifrado": "wkh ehvw zdb wr pdnh brxu guhdpv frph wuxh lv wr zdnh xs. pxulho vlhehuw",
    "decifrado": "",
    "resumo_criptografico": ""
 }

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=099bb428faac4b5fa39b8514f789502a1a779258'

headers = {'Content-type': 'multipart/form-data'}

answer = {'answer': open('answer.json', 'rb')}

r = requests.post(url, files=answer, data=data, headers=headers)

print(r.content)