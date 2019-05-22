import urllib

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=099bb428faac4b5fa39b8514f789502a1a779258"
f = urllib.urlopen(url)
contents = f.read()
f.close()
print (contents)