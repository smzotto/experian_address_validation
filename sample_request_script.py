import requests

url = 'https://www.api.experianaperture.io/address/search/vi'
myobj = {
  "country_iso": "GBR",
  "components": {
    "unspecified": [
      "79 Station road, kelty"
    ]
  },
  "dataset": [
    "MRF"
  ]
}

x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

print(x.text)
