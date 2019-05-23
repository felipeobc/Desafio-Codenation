import json, requests

response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=099bb428faac4b5fa39b8514f789502a1a779258")
print(response.status_code)
print(response.content)

# comments = json.loads(response.content)

# print(comments['numero_casas'])


# response = requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=099bb428faac4b5fa39b8514f789502a1a779258", data=answer, handler=)

# answer={
#     "numero_casas": 3,
#     "token": "099bb428faac4b5fa39b8514f789502a1a779258",
#     "cifrado": "wkh ehvw zdb wr pdnh brxu guhdpv frph wuxh lv wr zdnh xs. pxulho vlhehuw",
#     "decifrado": "the best way to make your dreams come true is to wake up. muriel siebert",
#     "resumo_criptografico": "4b649e40a0a1f2e6776c1291a0c81452dd697fb7",
#      "file": "answer"
#  }

# url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=099bb428faac4b5fa39b8514f789502a1a779258'
# # payload = {'some': 'data'}
# headers = {'Content-Type':'multipart/form-data'}

# r = requests.post(url, files=answer)

# print(r.content)
