import os
import urllib.request
import re
import time

if not os.path.exists('C:\\1\\Ust-Katav'):
  os.makedirs('C:\\1\\Ust-Katav')

if not os.path.exists('C:\\1\\Ust-Katav\\plain'):
    os.makedirs('C:\\1\\Ust-Katav\\plain')

if not os.path.exists('C:\\1\\Ust-Katav\\mystem-xml'):
    os.makedirs('C:\\1\\Ust-Katav\\mystem-xml')

if not os.path.exists('C:\\1\\Ust-Katav\\mystem-plain'):
    os.makedirs('C:\\1\\Ust-Katav\\mystem-plain')

dau='@au '
dti='@ti '
dda='@da '
durl='@url '
art_num=0 

prog="C:\\mystem.exe"
filein="C:\\1\\Ust-Katav\\plain\\"
fileout="C:\\1\\Ust-Katav\\mystem-xml\\"

start_url='http://tramuk.ru/novosti/'
for i in range(1650, 2000):
    time.sleep(1)
    try:
        page_url=start_url+str(i)
        url_open=urllib.request.urlopen(page_url)
        html_text=url_open.read().decode('utf-8')

        res=re.search('<meta name="title" content="(.*?)" />', html_text)
        if res!=None:
            
            title=res.group(1)
        res=re.search('<a rel="author".*>(.*)</a>', html_text)
        autor='NoName'
        if res!=None:
            author=res.group(1)
        res=re.search('Published: *([\d]{1,2}?) *([А-Яёа-я]*) *([\d]{1,4})([\d]*?)[\\t]*</div>', html_text)
        numm='undef'
        if res!=None:
            m = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
            n = 1
            for t in m:
                if t == res.group(2):
                    numm = str(n)
                n=n+1
            data=res.group(1)+"-"+numm+"-"+res.group(3)
        res=re.compile('<div class="itemFullText">(.*?)</div>', flags=re.U | re.DOTALL)
        resul=res.findall(html_text)
        if resul!=None:
            text=''
            text=resul

        clear_text = []
        regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
        regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
        for t in text:
            clean_t = regSpace.sub("", t)
            clean_t = regTag.sub("", clean_t)
            clear_text .append(clean_t)
        clear_text=''.join(clear_text)

        art_num+=1
        name='article'+str(art_num)
        p=[]
        p=data[-4:]
        if not os.path.exists('C:\\1\\Ust-Katav\\plain\\'+p+'\\'+numm):
                os.makedirs('C:\\1\\Ust-Katav\\plain\\'+p+'\\'+numm)
        file=open('C:\\1\\Ust-Katav\\plain\\'+p+'\\'+numm+'\\'+name+'.txt', 'w')
        file.write(dti+title)
        file.write('\n')
        file.write(dau+author)
        file.write('\n')
        file.write(dda+data)
        file.write('\n')
        file.write(durl+page_url)
        file.write('\n'+'\n')
        file.write(clear_text)
        file.close()

        inp = "C:\\1\\Ust-Katav\\plain"
        lst = os.listdir(inp)
        for fl1 in lst:
            lst2 = os.listdir(inp+os.sep+fl1)
            for fl2 in lst2:
              lst3 = os.listdir(inp+os.sep+fl1+os.sep+fl2)
              for fl3 in lst3:
                os.system("C:\mystem.exe -i -d -e windows-1251 --format xml " + inp + os.sep + fl1 + os.sep + fl2 + os.sep + fl3 + " C:\\1\\Ust-Katav\\mystem-xml" + os.sep + fl3+".xml")
                os.system("C:\mystem.exe -i -d -e windows-1251 " + inp + os.sep + fl1 + os.sep + fl2 + os.sep + fl3 + " C:\\1\\Ust-Katav\\mystem-plain" + os.sep + fl3+".txt")


    except:
        print('Error')
