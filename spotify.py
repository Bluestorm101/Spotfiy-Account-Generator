import requests
import colorama
from colorama import *
import random
from art import *
import datetime
from datetime import datetime
import base64
import json

tprint("Bluestorm")
print("----------------------------------------------------------------------------------------------------")

while True:
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    date_time = datetime.fromtimestamp(ts)
    time = date_time.strftime("%H:%M:%S")

    print(Fore.RESET,"[",time,"]",Fore.MAGENTA,"{!} Creating Account")

    ln = "ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghijklmnopqrstuvwxyz0123456789"
    mail  = ''.join((random.choice(ln) for i in range(6,10)))
    email = mail + "@xitroo.com"
    name = ''.join((random.choice(ln) for i in range(7)))
    password = ''.join((random.choice(ln) for i in range(14)))

    headers = {
    'authority': 'spclient.wg.spotify.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'origin': 'https://www.spotify.com',
    'referer': 'https://www.spotify.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36',
    }

    json_data = {
    'account_details': {
        'birthdate': '2000-02-08',
        'consent_flags': {
            'eula_agreed': True,
            'send_email': False,
            'third_party_email': True,
        },
        'display_name': name,
        'email_and_password_identifier': {
            'email': email,
            'password': password,
        },
        'gender': 1,
    },
    'callback_uri': 'https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=uk',
    'client_info': {
        'api_key': 'a1e486e2729f46d6bb368d6b2bcda326',
        'app_version': 'v2',
        'capabilities': [
            1,
        ],
        'installation_id': 'a82b20169f2850b8ea1b80be87d28449',
        'platform': 'www',
    },
    'tracking': {
        'creation_flow': '',
        'creation_point': 'https://open.spotify.com/?sp_cid=a82b20169f2850b8ea1b80be87d28449&device=desktop',
        'referrer': '',
    },
    }

    x = requests.post('https://spclient.wg.spotify.com/signup/public/v2/account/create', headers=headers, json=json_data)

    if x.status_code == 200:
        print(Fore.RESET,"[",time,"]",Fore.GREEN,"{+} Account Created > ",email,":",password,":",name)
        cred = email,":",password,":",name
        with open("data/accounts.txt" ,"a",) as file:
                    file.write(f"{cred}\n")
 
    else:
        print("[",time,"]",Fore.RED,"{!} Error Could not Create Account")