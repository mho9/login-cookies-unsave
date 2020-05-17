import requests,json,time,re
import random 
from time import sleep


with open('config.json') as file_js:
    file_js = json.load(file_js)## josn to json :)

user_ag_list= file_js['User_agent'] #list of User agents
User_agent = random.choice(user_ag_list)

cookies = file_js['Cookies']## your  cookies 
csrf_token =cookies['csrftoken']
sessionid = cookies['sessionid']


user = input('Username : ')



def login():
    s = requests.Session()

    s.headers = { #header
        'User-Agent':User_agent,
        'Connection': 'Keep-Alive',
        "X-CSRFToken": csrf_token
    }
    #

    s.cookies.update({
        'sessionid':sessionid,
    })

    r = s.get('https://www.instagram.com/')
    # token
    

 
    find = r.text.find(user)
    if find != -1:
        
        user_json = s.get(f'https://instagram.com/{user}/?__a=1')
        print(user_json)

        if user_json.status_code ==200:

            user_json =user_json.json()

            info = user_json['graphql']['user']['edge_saved_media']['edges']
            
            for i in info:


                i_d = i['node']['id']#  get  id the  Post
               
              
                sleep(6)

                unsave =s.post(f'https://www.instagram.com/web/save/{i_d}/unsave/')

               
                print('Done')
                print('Erorr')
                if unsave.ok ==True:
                    count +=1
                else:
                    Erorr +=1
        else:
            print('Something wrong')
                            
                        
                    
    else:
        print('Check your Cookies or Username ?~?')
        exit
    
login()
