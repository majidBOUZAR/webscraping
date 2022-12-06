######################################### beautiful soup ##############################################
import requests
from bs4 import BeautifulSoup
url = "https://uqo.ca/"
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

#find = soup.findAll("div")
#print(find)

#find_id = soup.find("div",id="nom_of_id")
#print(find_id)

#find_id = soup.findAll("div",id="nom_of_id")
#print(find_id)
###########f = open("demofile.html", "w")
###########f.write(page)
###########f.close()

find_classe = soup.find("a",class_="btn btn-sm btn-transparent width-150")
print(find_classe)



######################################### REGEX regulare expression ##############################################



import re
string = """ this is my email : test@test.com 
             this is my email : test1.22@test.com 
             this is my email : test12_22@test.com 
             this is my phine number : +213 333333333
             this is my ip : 123.321.123.321 
               """
regex = re.findall("\S{1,}\@\S{1,}.\S{1,}",string) #return all object
regex1 = re.search("\S{1,}\@\S{1,}.\S{1,}",string) #return first object
print(regex)
print(regex1)
###################\+\d{1,}\s{1,}\d{1,} number pattern
###################\S{1,}\@\S{1,}.\S{1,} email pattern
###################\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} id pattern
### or with link
import re
import requests
url = "http://url.com/"
page = requests.get( url,'html.parser').text
regex1 = re.search("\S{1,}\@\S{1,}.\S{1,}",page) #return first object
print(regex1)



######################################### MechanicalSoup hadi dirlak login automatiquement##############################################



import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "http://127.0.0.1:8000/accounts/login/"
t = browser.get(url)
jibli_page_html = t.soup
form = jibli_page_html.select("form")[1] #return the form number 2 in list contains all form of the page login 
#print(form_page) # hadi tjibli form numero 2 

username = form.select("input")[1]
password = form.select("input")[2]

username["value"] = 'majid' #insert the value of usernname
password["value"] = '1232' #insert the value of password

sub = browser.submit(form,url)
print(sub.url) # here will write the current url 

######### TEST 1
if sub.url == 'http://127.0.0.1:8000/' : #check if we are in the page wich mean login is succesful
  print('login succesful')
else : 
  print('login error')

######### TEST 2
try : 
   htmll=sub.soup
   a = htmll.select('a')[3]
   if '<a href="/profile/"> <i class="fa fa-user" style="font-size:20px"></i> Profile : majid</a>' == str(a) :
    print('sucess')
   else : 
    print('non')  
except  :
   print('you are note login')



######################################## GoogleSearche ##############################################



from googlesearch import search
print('Enter your search:')
x = input()
r = search(x, stop = 10 )#, num=2 , pause = 3
for i in r :
   print("your search is " ,i)


######################################## Selenium ##############################################
