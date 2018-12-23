import config
import requests
import json

token = config.token

URL = "https://api.telegram.org/bot" + token + '/'






#https://api.telegram.org/bot713670283:AAFpUNdODrvWvkrWvECAyIqfuNAeVH425Do/sendmessage?chat_id=441814052&text=саси
def get_updates():

	url = URL + 'getupdates' 

	req = requests.get(url)

	return req.json()




def main():


 	d = get_updates()

	with open('updates.json', 'w') as file:

		json.dump(d, file, indent = 2, ensure_ascii = False )



if __name__ == '__main__':
	main()
