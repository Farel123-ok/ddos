import os
import sys
import httpx
from colorama import Fore, init
init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN
fy = Fore.YELLOW
fw = Fore.WHITE
fre = Fore.RESET

list = [
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
'https://api.openproxylist.xyz/http.txt',
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'http://worm.rip/http.txt',
'https://proxyspace.pro/http.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
'https://www.us-proxy.org',
    'https://www.socks-proxy.net',
    'https://proxyscrape.com/free-proxy-list',
    'https://www.proxynova.com/proxy-server-list/',
    'https://proxybros.com/free-proxy-list/',
    'https://proxydb.net/',
    'https://spys.one/en/free-proxy-list/',
    'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=100',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=110',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=96',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=88',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=5',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=6',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=7',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=8',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=9',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=10',
  ' https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=70',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=30',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=85',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=91',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=52',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=77',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=78',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=89',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=99',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=23',
  ' https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=34',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=45',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=55',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=76',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=91',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=93',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=93',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=94',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=95',
  'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=97',
  'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
  'https://api.good-proxies.ru/getfree.php?count=1000&key=freeproxy',
]  
         

if __name__ == "__main__":
    file = "proxy.txt"
    
    try:
        if os.path.isfile(file):
            os.system('cls' if os.name == 'nt' else 'clear')
            os.remove(file)
            print("{}File {} Sudah Ada!\n{}Memulai Mengunduh {} Yang Baru!\n".format(fr, file, fy, file))
            with open(file, 'a') as data:
                for proxy in list:
                    data.write(httpx.get(proxy).text)
                    print(" -| mengambil {}{}".format(fg, proxy))
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            with open(file, 'a') as data:
                for proxy in list:
                    data.write(httpx.get(proxy).text)
                    print(" -| mengambil {}{}".format(fg, proxy))
    
        with open(file, 'r') as count:
            total = sum(1 for line in count)
        print("\n{}( {}{} {}) {}Proxy Berhasil Di Unduh.". format(fw, fy, total, fw, fg))
    
    except IndexError:
        sys.exit(1)
        