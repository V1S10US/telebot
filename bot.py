import config
import requests
import json

token = config.token

URL = "https://api.telegram.org/bot" + token + '/'


#https://api.telegram.org/bot713670283:AAFpUNdODrvWvkrWvECAyIqfuNAeVH425Do/sendmessage?chat_id=441814052&text



def get_updates():                                          # builds .json file with data from url request

	url = URL + 'getupdates' 

	req = requests.get(url)

	return req.json()

def get_message():

	data = get_updates()                                    # makes a dict from .json file from get_address

	chat_id = data['result'][-1]['chat']['id']              # 
                                                            # saves value from dict
	message_text = data['result'][-1]['message']['text']    #

	message = {'chat_id' : chat_id,
			   'text' : message_text}
	return message


def send_message(chat_id,text=''):
	
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)




def main():

 	#d = get_updates()

	#with open('updates.json', 'w') as file:

		#json.dump(d, file, indent = 2, ensure_ascii = False )
answer = get_message()

chat_id = answer['chat_id']
response = answer['text']
if response == 'Codename?':

	send_message(chat_id,'Test string')


if __name__ == '__main__':
	main()
