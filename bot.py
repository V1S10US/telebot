import config
import requests
import json
from time import sleep

token = config.token

URL = "https://api.telegram.org/bot" + token + '/'


#https://api.telegram.org/bot713670283:AAFpUNdODrvWvkrWvECAyIqfuNAeVH425Do/sendmessage?chat_id=441814052&text

global recent_update_id
recent_update_id = 0 

def get_updates():                                          # builds .json file with data from url request

	url = URL + 'getupdates' 

	req = requests.get(url)

	return req.json()

def get_message():

	data = get_updates()                                    # makes a dict from .json file from get_address

	last_item = data['result'][-1]

	update_id = last_item['update_id']

	global recent_update_id
	if recent_update_id != update_id:                       # takes the last update_id and checks for equality with current one

		recent_update_id = update_id

		chat_id = last_item['message']['chat']['id']        # 
	                                                        # saves value from dict
		message_text = last_item['message']['text']         #

		username = last_item['message']['from']['username']

		message = {'chat_id' : chat_id,
				   'text' : message_text,		
				    'username' : username}
		return message
		return None

def send_message(chat_id,text=''):
	
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)

def echo(chat_id,text):
	send_message(chat_id,text)

def main():
	'''d = get_updates()
	with open('updates.json', 'w') as file:

		json.dump(d, file, indent = 2, ensure_ascii = False )'''

	while True:		
		answer = get_message()

		if answer != None:                                                   # main body 


			chat_id = answer['chat_id']
			send_message(chat_id,'Здравствуйте ,{} !'.format(answer['username']))


		else:
			continue

		if answer['text'] == 'stop':
			break
		sleep(3)                                                             # saves for overloading



if __name__ == '__main__':
	main()