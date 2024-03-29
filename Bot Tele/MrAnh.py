import requests
import os
from datetime import datetime
from tkinter.filedialog import askopenfilename
import base64, lzma


blue_back = '\033[46m'
red = '\033[31m'
purple = '\033[35m'
cyan ='\033[36m'
reset_color = '\033[0m'

def isAdmin(API):
    boss = os.getlogin()
    if(boss == "apt3233"):
        return("%sCode by APT3233%s" % (red, reset_color))
    else:
        return ""

def clear():
    if os.name == "nt": os.system("cls")
    else:   os.system("clear")

def banner(API):
    clear()
    print(f"""\033[1m\033[94m
 ____             _      ____                       
|  _ \  __ _ _ __| | __ |  _ \ __ ___   _____ _ __  
| | | |/ _` | '__| |/ / | |_) / _` \ \ / / _ \ '_ \ 
| |_| | (_| | |  |   <  |  _ < (_| |\ V /  __/ | | |
|____/ \__,_|_|  |_|\_\ |_| \_\__,_| \_/ \___|_| |_|                                                
          
                                        {isAdmin(API)}
\033[0m""")


def send_message(TOKEN, ID):
    message = input("Message: %s" % reset_color)
    now = datetime.now()
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        params = {'chat_id': ID, 
                  'text':message}
        response = requests.post(url, params=params)

        with open('status_code.txt', 'a') as file:
            file.write(f'{now} - Status code: {response.status_code} - {message}\n')

        if response.status_code != 200:
            print("%sStatus code: %s %s" % (red, response.status_code, reset_color))
        else:
            print("%sMessage sent successfully..%s" % (cyan, reset_color))
    except Exception as e:
        print(e)
    input("Press Enter to continue..")
    

def send_Document(TOKEN, ID):
    caption = input("Caption: %s" % reset_color)
    now = datetime.now()
    path = askopenfilename()
    path_file = os.path.abspath(path)
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
        params = {'chat_id': ID, 'caption':caption}
        file = {'document': open(path, 'rb')}
        print("%s[+] Uploading...%s" % (cyan, reset_color))
        response = requests.post(url, params=params, files=file)

        with open('status_code.txt', 'a') as file:
            file.write(f'{now} - Status code: {response.status_code} - {path_file}\n')

        if response.status_code != 200: print("%sStatus code: %s %s" % (red, response.status_code, reset_color))
        else:   print("%sDocument sent successfully..%s" % (cyan, reset_color))

    except Exception as e:
        print(e)
    
    input("Press Enter to continue..")

def read_api_info():
    API_TOKEN = ""
    CHAT_ID = ""
    if os.path.exists('api.txt'):
        with open('api.txt', 'r') as f:
            content = f.readline().strip()
            parts = content.split('$')
            if len(parts) == 2:
                API_TOKEN, CHAT_ID = parts
    else:
        API_TOKEN = input("Your_API: ")
        CHAT_ID = input("YOUR_CHAT_ID: ")
        with open('api.txt', 'w') as f:
            f.write(f"{API_TOKEN}${CHAT_ID}")
        print("%s[+] API, CHAT_ID saved successfully - api.txt.%s" % (cyan, reset_color))
        input("Press any Key to continue.")
    return API_TOKEN, CHAT_ID

def main():
    API_TOKEN, CHAT_ID = read_api_info()
    
    while 1:
        banner(API_TOKEN)
        print("%s1. Send Message\t\t 2. Send Document \n3. Exit \t\t 4. Remove Config\n5. ReadMe" % (purple))
        select = int(input("\nEnter your choice: "))
        if select == 1:
            send_message(API_TOKEN, CHAT_ID)
            continue
        elif select == 2:
            send_Document(API_TOKEN, CHAT_ID)
            continue
        elif select == 3:   exit(0)
        elif select == 4:
            if os.path.exists('api.txt'):
                os.remove('api.txt')
            print('[+] Remove Successfully..')
            break 
        elif select == 5:
            banner(API_TOKEN)
            print(f"{purple}[+] How to use: ")
            print("1. Creat Bot to get API")
            print("2. Creat new group")
            print(f"3. Add @chatIDrobot to get CHAT_ID{reset_color}")
            input("Press any Key to continue.")
        else:
            break

if __name__ == "__main__":
    main()
