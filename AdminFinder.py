import requests,os,sys,platform,time,threading,enquiries
from colorama import Fore

checked = 0
Founds = 0
Blocked = 0
Found_url = []

def  get_file():
    FILES = __file__.split('/')
    for FILE in FILES:
        if (".py" in FILE):
            return FILE

def clear():
    os.system("clear")

def OS_check():
    if (platform.system().lower() != "linux"):
        print("Only Linux OS!")
        time.sleep(0.50)
        exit(0)

def searcher(url,num,file_save):
    global checked,Founds,Found_url,Blocked
    if (file_save != False):
        with open(file_save,'w') as f:
            f.close()
    try:
        Response = requests.get(url)
        if (Response.status_code != 404):
            print(f"{Fore.GREEN}Found {Response.status_code}: {url}{Fore.RESET}")
            Found_url.append(f"{Fore.GREEN}Found {Response.status_code}: {url}{Fore.RESET}")
            Founds+=1
            if (file_save != False):
                with open(file_save,'a') as f:
                    f.write(f"Found {Response.status_code}: {url}{Fore.RESET}")
                    f.close()
        else:
            print(f"{Fore.RED}Not Found {Response.status_code}: {url}{Fore.RESET}")
    except:
        print(f"{Fore.RED}Connection Blocked!{Fore.RESET}")
        Blocked+=1

    checked += 1
    threading._shutdown()

     

def main():
    clear()
    print("By Hereioz, IG: https://instagram.com/hereioz/\n")
    time.sleep(1)
    try:
        if ('-u' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == "-u"):
                    i+=1
                    site = sys.argv[2]
                    break

        else:
            print(f" Usage:\n     -u [url]        [required!]\n     -o [file_save]  [optional]\n     -f [path_file]  [required!]\n     -t [time]       [optional]\n\n Ex: python3 {get_file()} -u https://google.com -o path.txt -f paths.txt -t 0.50")
            exit(0)

    except IndexError:
        print(f" Usage:\n     -u [url]        [required!]\n     -o [file_save]  [optional]\n     -f [path_file]  [required!]\n     -t [time]       [optional]\n\n Ex: python3 {get_file()} -u https://google.com -o path.txt -f paths.txt -t 0.50")

    try:
        for i in range(len(sys.argv)):
            if (sys.argv[i] == "-o"):
                i+=1
                file_save = sys.argv[i]
                break
            else:
                file_save = False
    except:
        file_save = False

    try:
        if ('-f' in sys.argv):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '-f'):
                    i+=1
                    path_file = sys.argv[i]
                    break
        else:
            print(f" Usage:\n     -u [url]        [required!]\n     -o [file_save]  [optional]\n     -f [path_file]  [required!]\n     -t [time]       [optional]\n\n Ex: python3 {get_file()} -u https://google.com -o path.txt -f paths.txt -t 0.50")
            exit(0)

    except IndexError:
        print(f" Usage:\n     -u [url]        [required!]\n     -o [file_save]  [optional]\n     -f [path_file]  [required!]\n     -t [time]       [optional]\n\n Ex: python3 {get_file()} -u https://google.com -o path.txt -f paths.txt -t 0.50")
    
    try:
        for i in range(len(sys.argv)):
            if (sys.argv[i] == "-t"):
                i+=1
                sleep = float(sys.argv[i])
                break
            else:
                sleep = (0.10)
    except:
        sleep = (0.10)


    with open(path_file,'r') as f:
        path = f.readlines()
        f.close()

    time.sleep(3)

    for i in range(len(path)):
        if (path[i].startswith('/')):
            url = site+path[i].strip()
        else:
            url = site+"/"+path[i].strip()
        time.sleep(sleep)
        threading.Thread(target=searcher,args=(url,i,file_save)).start()

    while True:
        time.sleep(1)
        if (threading.active_count() < 3):
            print(f"\n{Fore.RESET}url Checked : {checked}")
            print(f"url Found : {Founds}")
            print(f"url Blocked : {Blocked}\n")
            break

    if enquiries.confirm('Want print it?'):
        for i in range(len(Found_url)):
            time.sleep(0.05)
            print(Found_url[i])


OS_check()
main()