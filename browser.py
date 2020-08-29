
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

dire=sys.argv[1]

try:
    os.mkdir(dire)
except OSError:
    print ("Creation of the directory %s failed" % dire)
else:
    print ("Successfully created the directory %s " % dire)
existing_file=[]
url_stack=[]

while True:
    url=input()
    if url=='exit':
        break
    if url=='back':
        url_stack.pop()
        url=url_stack.pop()
    if url.count('.')<1:
        print('There is an error reading website!')
    elif url in existing_file:
        url_stack.append(url)
        readfilepath=os.path.join(dire,url)
        with open(readfilepath,'r') as rd:
            print(rd.read())
    else:
        fullurl='https://'+url
        r=requests.get(fullurl)
        soup = BeautifulSoup(r.text, 'lxml')
        fulltext=""
        headings=soup.find_all(["p","a", "ul","ol","li","h1", "h2", "h3", "h4", "h5", "h6"])
        for heading in headings:
            fulltext+=heading.get_text()
            if heading.name in ["ul","ol","li"]:
                print(Fore.BLUE+heading.get_text())
            else:
                print(Fore.WHITE+heading.get_text())

        url_stack.append(url)
        urll=url.rsplit('.',1)
        filename=urll[0]
        existing_file.append(filename)
        filepath=os.path.join(dire,filename)
        with open(filepath,'w+',encoding="utf-8") as f:
            f.write(fulltext)



