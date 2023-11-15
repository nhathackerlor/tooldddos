try:import requests
except:import os;os.system('pip install requests')
from datetime import datetime
import requests,random,os,sys
from time import sleep
session = requests.Session()
import threading
def logo():
    os.system("cls" if os.name == "nt" else "clear")


def ngttu(o):
    while(o>1):
        o=o-1
        print(f'[LNMTxTMN][.....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[LNMTxTMN][X....][{o}]','     ',end='\r');sleep(1/6)
        print(f'[LNMTxTMN][XX...][{o}]','     ',end='\r');sleep(1/6)
        print(f'[LNMTxTMN][XXX..][{o}]','     ',end='\r');sleep(1/6)
        print(f'[LNMTxTMN][XXXX.][{o}]','     ',end='\r');sleep(1/6)
        print(f'[LNMTxTMN][XXXXX][{o}]','     ',end='\r');sleep(1/6)

list_token_page=[]
list_id_page=[]
token_s=1
logo()
soluong=int(input("Nhập số luồng chạy: "))
cookie_fb=input(f'Nhập cookie Facebook {token_s} : ')


while(True):
    
  
    token_fb=requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token', headers={'cookie': cookie_fb}).url.split('&')[0].split('#access_token=')[1]
 
    id_page=input(f'Nhập id page mẹ {token_s} : ')
    if id_page=="":
        break
    listpage= session.get(f'https://graph.facebook.com/me/accounts?access_token={token_fb}&limit=100000000000000000000000000000000000000000000000000000000000000000', headers={'cookie': cookie_fb}).json()['data']
    get_token_page=requests.get(f'https://graph.facebook.com/{id_page}?fields=access_token&access_token={token_fb}').json()
    if 'access_token' in get_token_page:
        token_page=get_token_page['access_token']
        list_token_page.append(token_page)
        list_id_page.append(id_page)
        token_s=token_s+1
    elif 'error' in get_token_page:print(get_token_page['error']['message'])
    else:print(get_token_page)
logo()
choice=input('[ENTER - Tự tách][Nhập: no - Không tự tách]\nNHẬP LỰA CHỌN: ')
while(True):
    try:delay=int(input('Nhập delay: '));break
    except:print('[ngttu][?]');sleep(0.5)
s=0
logo()
def regpage():
    global list_token_page,list_id_page
    ngttu3=open("name.txt","r", encoding="utf8")
    ngttu9=ngttu3.read()
    ngttu9=ngttu9.split("\n")
    for x in range(len(list_token_page)):
        
            try:
                token_page=list_token_page[x]
                id_page=list_id_page[x]
                latitude=random.randrange(99999999)
                longitude=random.randrange(33333333)
                store_number=random.randrange(999999999)
                name=random.choice(ngttu9)
                register=requests.post(f'https://graph.facebook.com/v16.0/{id_page}/locations?access_token={token_page}',data={'_reqName': 'object:page/locations','_reqSrc': 'LocationManagerUtils','always_open': 'false','differently_open_offerings': '{}','id': id_page,'ignore_warnings': 'true','is_franchise': 'false','locale': 'vi_VN','location': '{"city_id":2599270,"latitude":"21.'+str(latitude)+'","longitude":"105.2'+str(longitude)+'","street":"'+name+'","zip":"10000"}','method': 'post','permanently_closed': 'false','phone': '+84987654321','pickup_options': '[]','place_topics': '["123377808095874","530553733821238"]','pretty': '0','price_range': 'Unspecified','store_name': name,'store_number': store_number,'suppress_http_code': '1'}).json()
                if 'id' in register:
                    s=s+1
                    id_register=register['id']
                    time=datetime.now().strftime("%H:%M:%S")
                    if choice=='':
                        print(f'[{s}][Tạo page thành công][{time}][{name.upper()}][{id_register}]',end='\r')
                        tach=requests.post(f'https://graph.facebook.com/v16.0/{id_page}/locations?access_token={token_page}',data={'_reqName': 'object:page/locations','_reqSrc': 'LocationManagerUtils','locale': 'vi_VN','location_page_id': id_register,'method': 'delete','pretty': '0','store_number': store_number,'suppress_http_code': '1'}).json()
                        if 'success' in tach:print(f'[{s}][Tạo và gỡ page thành công][{time}][{name.upper()}][{id_register}]')
                    else:print(f'[{s}][Tạo page thành công][{time}][{name.upper()}][{id_register}]')
                    ngttu(delay)
                elif 'error' in register:print(register['error']['message']);ngttu(20000)
                else:print(register);ngttu(5500)
            except:print('[NETWORK ERROR !]','          ',end='\r')
Threads=[]
for lam in range(soluong):
    Threads+=[threading.Thread(target=regpage)]
for t in Threads:
    t.start()
for t in Threads:
    t.join()
