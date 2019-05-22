#https://www.codenation.dev/acceleration/aceleradev-python-2/challenge/dev-ps
import requests, json
import hashlib

response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=099bb428faac4b5fa39b8514f789502a1a779258')

print(response.content)


#i = hashlib.sha1(b'the best way to make your dreams come true is to wake up. muriel siebert')
#e = i.hexdigest()

#print(e)
