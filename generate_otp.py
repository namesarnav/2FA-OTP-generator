import os
import random
from twilio.rest import Client

account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'

authorized_users_with_passwords = { 'admin': '1234'}
client = Client(account_sid,auth_token)

def request_otp():
    def Authenticate():
        otp = random.randint(10000000,99999999)
        return otp
    
    global code_2fa 
    code_2fa = Authenticate()
request_otp()

attempts = 3
while attempts > 0:
  
    authenticate_2fa = int(input('Enter OTP: '))
    if authenticate_2fa == code_2fa:
        print('Success!!')
        break
    else:
        print('Authentication Failed')
        attempts -= 1
        print(f'Attempts remaining: {attempts}')
        
        if attempts == 0:
            print('Request another OTP?')
            ans = input('Y or N : ')
            if ans.lower() ==  'y':
                request_otp()
                attempts = 3

            elif ans.lower() == 'n':
                break
            else: 
                print('Not correct input, try again.')
                break

###--- If you want to spam a message to someone, uncomment this and comment the above code below client declaration ---##
# def send_text(msg):
#     message = client.messages.create(
#         body = i,
#         from_ = '+18445260912',
#         to='+14694653437'
#     )

# with open('song.txt','r') as spam:
#     content = spam.readlines()

# for i in content:
#     send_text(i)
