from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import sys
import time

rollnumber = input("Enter your roll number -> ")
passwd = input("Enter your password -> ")
dss = webdriver.Chrome()
dss.get('http://www.dss.nitc.ac.in/nitcreg/reglogin.aspx')

username = dss.find_element_by_name('user')
username.send_keys(rollnumber)
password = dss.find_element_by_name('passwd')
password.send_keys(passwd)
dss.find_element_by_name('Submit1').click()
dss.get('http://www.dss.nitc.ac.in/nitcreg/tlogin.aspx?regno='+rollnumber)

def evaluate():
	select = Select(dss.find_element_by_name('ddlcourse'))
	select.select_by_index(0)

	dss.find_element_by_name('Button3').click()

	alert = dss.switch_to.alert.accept()

	select = Select(dss.find_element_by_name('ddlteacher'))
	select.select_by_index(0)

	dss.find_element_by_name('Button1').click()
	for i in range(11, 16):
		select = Select(dss.find_element_by_name('ddl'+str(i)))
		select.select_by_index(4)

	for i in range(21, 26):
		select = Select(dss.find_element_by_name('ddl'+str(i)))
		select.select_by_index(4)

	for i in range(31, 36):
		select = Select(dss.find_element_by_name('ddl'+str(i)))
		select.select_by_index(4)

	for i in range(41, 46):
		select = Select(dss.find_element_by_name('ddl'+str(i)))
		select.select_by_index(4)

	for i in range(51, 54):
		select = Select(dss.find_element_by_name('ddl'+str(i)))
		if i is 53:
			select.select_by_index(6)
		else:
			select.select_by_index(1)
	time.sleep(3)
	dss.find_element_by_name('Button1').click()
	

for i in range(0,6):
	time.sleep(4)
	evaluate()





