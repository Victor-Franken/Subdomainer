#!/usr/bin/python3
from argparse import ArgumentParser,FileType
from threading import Thread
from requests import get,exceptions
from time import time

subdomains = []
def prepare_args():
    """Prepare Arguments
            return:
            args(argparse.Namespace)
    """
    print("""
 _______  __   __  _______  ______   _______  __   __  _______  ___   __    _  _______  ______   
|       ||  | |  ||  _    ||      | |       ||  |_|  ||   _   ||   | |  |  | ||       ||    _ |  
|  _____||  | |  || |_|   ||  _    ||   _   ||       ||  |_|  ||   | |   |_| ||    ___||   | ||  
| |_____ |  |_|  ||       || | |   ||  | |  ||       ||       ||   | |       ||   |___ |   |_||_ 
|_____  ||       ||  _   | | |_|   ||  |_|  ||       ||       ||   | |  _    ||    ___||    __  |
 _____| ||       || |_|   ||       ||       || ||_|| ||   _   ||   | | | |   ||   |___ |   |  | |
|_______||_______||_______||______| |_______||_|   |_||__| |__||___| |_|  |__||_______||___|  |_|
""")
    print("✩░▒▓▆▅▃▂▁𝐜𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 : 𝐕𝐢𝐜𝐭𝐨𝐫-𝐅𝐫𝐚𝐧𝐤𝐞𝐧▁▂▃▅▆▓▒░✩\n")
    parser = ArgumentParser(description="̲F̲a̲̲s̲̲t̲̲e̲̲r̲ ̲s̲̲u̲̲b̲̲d̲̲o̲̲m̲a̲̲i̲̲n̲̲e̲̲r̲ ̲e̲̲n̲̲u̲̲m̲̲e̲̲r̲a̲̲t̲̲i̲̲o̲̲n̲ ̲t̲̲o̲̲o̲̲l̲ ",usage="%(prog)s example.com",epilog="Example =%(prog)s -w /usr/bin/share/wordlist/wordlist.txt -t 500 -V google.com")
    parser.add_argument(metavar="Domain",dest="domain",help="Domain Name")
    parser.add_argument("-w","--wordlist",dest="wordlist",metavar="",type=FileType("r"),help="Wordlist of subdomains",default="wordlist.txt")
    parser.add_argument("-t","--threads",dest="threads",metavar="",type=int,help="Number of threads to use",default=200)
    parser.add_argument("-V","--verbose",action="store_true",help="verbose output")
    parser.add_argument("-v","--version",action="version",help="print version",version="%(prog)s 1.0")
    args = parser.parse_args()
    return args

def prepare_words():
    """generator functions for words
    """
    words = arguments.wordlist.read().split()
    for word in words:
        yield word

def check_subdomain():
    """check subdomain for 200 status code
    """
    while True:
        try:
            word=next(words)
            url=f"https://{word}.{arguments.domain}"
            request=get(url,timeout=5)
            if request.status_code==200:
                subdomains.append(url)
                if arguments.verbose:
                    print(url)
        except(exceptions.ConnectionError,exceptions.ReadTimeout):
            continue
        except StopIteration:
            break

def prepare_threads():
    """create, start , join threads
    """
    thread_list=[]
    for _ in range(arguments.threads):
        thread_list.append(Thread(target=check_subdomain))
    
    for thread in thread_list:
        thread.start()
    
    for thread in thread_list:
        thread.join()

if __name__=="__main__":
    arguments = prepare_args()
    words=prepare_words()
    start_time=time()
    prepare_threads()
    end_time = time()
    print("Subdomains Found are :-\n"+"\n".join(i for i in subdomains))
    print(f"Time Taken - {round(end_time-start_time,2)}")