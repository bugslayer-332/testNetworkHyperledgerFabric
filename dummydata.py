import requests 

url = 'http://localhost:4000/channels/mychannel/chaincodes/fabcar'

authToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNhdHlhaml0IFNpciIsIm9yZ05hbWUiOiJPcmcyIiwiaWF0IjoxNjc5NDc1MDI1LCJleHAiOjMzNTkzMTAwNTB9.hOxj24A2FPb9K6R6utX2aWL91W0WNncX1NEgTIco6Rc'
headers = {
    'Authorization' : 'Bearer ' + authToken,
            'Content-Type': 'application/json'
}
print('Bearer' + authToken)
jsonObj = {
    "fcn": "createCar",
    "peers": ["peer0.org1.example.com","peer0.org2.example.com"],
    "chaincodeName":"fabcar",
    "channelName": "mychannel",
   "args": ["4","Mango","Fruit","Yellow","Satyajit Sir"]
}

x = requests.post(url, json = jsonObj,headers=headers)

print(x.text) 