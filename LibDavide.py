#usr/bin/env python3
#coded by t0rt3ll1n0 under GPL 3.0
#camhunter use insecam.org site
#inspired by cam-hackers 
import sys
import os
from time import sleep
import requests
import re

def keyboard():
	print("\n\033[31mUser interrupt, exiting.\033[0m")
	exit(0)
def menu():

	print("""
\033[31m  ____               \033[94m _   _             _            
\033[31m / ___|__ _ _ __ ___ \033[94m| | | |_   _ _ __ | |_ ___ _ __ 
\033[31m| |   / _` | '_ ` _ |\033[94m| |_| | | | | '_ \| __/ _ \ '__|
\033[31m| |__| (_| | | | | | \033[94m|  _  | |_| | | | | ||  __/ |   
\033[31m \____\__,_|_| |_| |_\033[94m|_| |_|\__,_|_| |_|\__\___|_|   
\033[0m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
\033[92m[1]\033[0m Italy      | \033[92m[11]\033[0m Vietnam   | \033[92m[21]\033[0m Austria       
\033[92m[2]\033[0m U.S.A.     | \033[92m[12]\033[0m Croatia   | \033[92m[22]\033[0m Egypt         
\033[92m[3]\033[0m France     | \033[92m[13]\033[0m Serbia    | \033[92m[23]\033[0m Greece                                                
\033[92m[4]\033[0m Spain      | \033[92m[14]\033[0m Turkey    | \033[92m[24]\033[0m Argentina     
\033[92m[5]\033[0m Korea      | \033[92m[15]\033[0m Japan     | \033[92m[25]\033[0m Peru          
\033[92m[6]\033[0m India      | \033[92m[16]\033[0m Russia    | \033[92m[26]\033[0m Netherlands     
\033[92m[7]\033[0m Brazil     | \033[92m[17]\033[0m Albania   | \033[92m[27]\033[0m Germany   
\033[92m[8]\033[0m Belgium    | \033[92m[18]\033[0m Cyprus    | \033[92m[28]\033[0m Poland        
\033[92m[9]\033[0m Romania    | \033[92m[19]\033[0m Finland   | \033[92m[29]\033[0m China          
\033[92m[10]\033[0m Canada    | \033[92m[20]\033[0m Mexico    | \033[92m[30]\033[0m Israel        
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
	
	scelta = int(input("\nroot@CamHunter:~# "))
	if(scelta == 1):
		print("\033[94m[*]\033[0m Loading Italy cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/IT/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")
			

	elif(scelta == 2):
		print("\033[94m[*]\033[0m Loading U.S.A. cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")
	elif(scelta == 3):
		print("\033[94m[*]\033[0m Loading France cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/FR/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")
	elif(scelta == 4):
		print("\033[94m[*]\033[0m Loading Spain cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/ES/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")
	
	elif(scelta == 5):
		print("\033[94m[*]\033[0m Loading Korea cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/KR/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 6):
		print("\033[94m[*]\033[0m Loading India cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/IN/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 7):
		print("\033[94m[*]\033[0m Loading Brazil cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/BR/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 8):
		print("\033[94m[*]\033[0m Loading Belgium cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/BE/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 9):
		print("\033[94m[*]\033[0m Loading Romania cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/RO/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 10):
		print("\033[94m[*]\033[0m Loading Canada cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/CA/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 11):
		print("\033[94m[*]\033[0m Loading Vietnam cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/VN/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 12):
		print("\033[94m[*]\033[0m Loading Croatia cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/HR/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 13):
		print("\033[94m[*]\033[0m Loading Serbia cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/RS/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 14):
		print("\033[94m[*]\033[0m Loading Turkey cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 15):
		print("\033[94m[*]\033[0m Loading Japan cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/JP/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 16):
		print("\033[94m[*]\033[0m Loading Russia cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/RU/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 17):
		print("\033[94m[*]\033[0m Loading Albania cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/AL/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 18):
		print("\033[94m[*]\033[0m Loading Cyprus cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/CY/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 19):
		print("\033[94m[*]\033[0m Loading Finland cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/FI/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 20):
		print("\033[94m[*]\033[0m Loading Mexico cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/MX/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 21):
		print("\033[94m[*]\033[0m Loading Austria cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/AT/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 22):
		print("\033[94m[*]\033[0m Loading Egypt cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/EG/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 23):
		print("\033[94m[*]\033[0m Loading Greece cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/GR/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 24):
		print("\033[94m[*]\033[0m Loading Argentina cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/AR/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 25):
		print("\033[94m[*]\033[0m Loading Peru cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/PE/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 26):
		print("\033[94m[*]\033[0m Loading Netherlands cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/NL/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 27):
		print("\033[94m[*]\033[0m Loading Germany cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 28):
		print("\033[94m[*]\033[0m Loading Poland cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/PL/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 29):
		print("\033[94m[*]\033[0m Loading China cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/CN/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")

	elif(scelta == 30):
		print("\033[94m[*]\033[0m Loading Israel cams...")
		sleep(2)
		try:
            		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            		for page in range (0,159):
		
                		url = ("https://www.insecam.org/en/bycountry/IL/?page="+str(page))
            
                		res = requests.get(url, headers=headers)
                		findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                		count = 0
                                
               			for _ in findip:
                			link = findip[count]

                			print (link)
                 
                			count += 1
		except:
            		print ("\033[41m\nUser interruption or server error, anyway exiting\033[0m\n")
	else:
		print("\n\033[41mINPUT ERROR!! TIPE A NUMBER FROM 1 TO 30\033[0m")
		sleep(2)
		menu()

try:
	menu()
except KeyboardInterrupt:
	keyboard()
			

			

			

			

			

			

			

			

			

			

			

			

			

			

			

			

			

			

			

			

			

			


 
			

			

			
			

			

			

	
