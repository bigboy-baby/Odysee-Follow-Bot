#Code and exploit by bigboybigboi#0001 skid if ur homosexual (ew)
import requests, random, string, threading, json

with open('config.json') as config_file:
  config = json.load(config_file)

def follow(user, prox):
  proxy = {
    "http":f"http://{prox}",
    "https":f"http://{prox}",
  }
  while True:
    try:
      claim = ('').join(random.choices(string.ascii_letters + string.digits, k=40))

      r = requests.get('https://api.odysee.com/user/new', proxies=proxy)
      dat = r.json()
      token1 = dat['data']
      token = token1['auth_token']
 
      d = {
        "auth_token": token,
        "channel_name": f"@{user}",
        "claim_id": "cdeda221af9a49e6d3421b587bc664f58ead8970",
        "notifications_disabled": "true"
      }

      r = requests.post('https://api.odysee.com/subscription/new', data=d, proxies=proxy)

      print(f"{token} | Followed {user}")
    except:
      pass

user = input("Channel: ")
am = int(input("Thread Amount: "))

prox = config["proxy"]
for n in range(am):
  x = threading.Thread(target=follow, args=(user,prox))
  x.start()