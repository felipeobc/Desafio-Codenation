# importing the requests library 
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=099bb428faac4b5fa39b8514f789502a1a779258"
  
  
# data to be sent to api 
data = {
    "numero_casas": 3,
    "token": "099bb428faac4b5fa39b8514f789502a1a779258",
    "cifrado": "wkh ehvw zdb wr pdnh brxu guhdpv frph wuxh lv wr zdnh xs. pxulho vlhehuw",
    "decifrado": "the best way to make your dreams come true is to wake up. muriel siebert",
    "resumo_criptografico": "4b649e40a0a1f2e6776c1291a0c81452dd697fb7"
 }
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print(pastebin_url) 