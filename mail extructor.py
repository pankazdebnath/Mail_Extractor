from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?num=100&ei=HT8_WpOGKIrxvAT7naLACw&q=football+lovers+email+id+type%3D%27gmail%27+location%3D%27new+york%27+&oq=football+lovers+email+id+type%3D%27gmail%27+location%3D%27new+york%27+&gs_l=psy-ab.12..35i39k1.174271.174271.0.175917.1.1.0.0.0.0.403.403.4-1.1.0....0...1.1.64.psy-ab..0.1.401....0.YdKm6dT0MDM')

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

print('The emails are:')
for email in emails:
    print(email)