#!/usr/bin/env python3
import os
import requests
import re
from time import sleep
import argparse
import sys

#import LibDavide
#CamHunter cli library#
#i will import it later

#basic version info
__version_info__ = ('2020','12','9')
__version__ = '-'.join(__version_info__)

#create parser
parser = argparse.ArgumentParser()
parser.add_argument('--nation', help='Nation to select')
parser.add_argument('--version', help="Show version info", action="store_true")
parser.add_argument('--show', help='Show list of nations', action="store_true")
parser.add_argument('--old', help='Use old interface', action="store_true")
parser.add_argument('--output', help='Save output in a file')
parser.add_argument('--update', help="Update CamHunter to the latest version", action="store_true")
#add help
args = parser.parse_args()

def banner():
	print("""

░█████╗░░█████╗░███╗░░░███╗██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝███████║██╔████╔██║███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██║░░██╗██╔══██║██║╚██╔╝██║██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
{ v2 coded by t0rt3ll1n0 ~ Breaking in cams may be illegal in some nations!! } \n
""")
#Best lamer banner#

nation_short = ""
page = ""
NationList = ["Italy", "USA", "France", "Spain", "India", "Korea", "Brazil", "Belgium", "Romania", "Canada", "Vietnam", "Croatia", "Serbia", "Turkey", "Japan", "Russia", "Albania", "Cyprus", "Finland", "Mexico", "Austria", "Egypt", "Greece", "Argentina", "Peru", "Netherlands", "Germany", "Poland", "China", "Israel"]
url = ("https://www.insecam.org/en/bycountry/"+ nation_short +"/?page="+str(page))

def MakeRequests(url, nation_short, NationList, nation):
	try:
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
		for page in range(0, 159):
			url = ("https://www.insecam.org/en/bycountry/"+ nation_short +"/?page="+str(page))
			req = requests.get(url, headers=headers)
			ip = re.findall('http://\d+.\d+.\d+.\d+:\d+', req.text)
			num = 0
			for _ in ip:
				link = ip[num]
				print(link)
				num += 1
	except KeyboardInterrupt:
		print("SIGTERM detected - aborting")

if args.nation:
	nation = args.nation
	NationList = ["Italy", "USA", "France", "Spain", "India", "Korea", "Brazil", "Belgium", "Romania", "Canada", "Vietnam", "Croatia", "Serbia", "Turkey", "Japan", "Russia", "Albania", "Cyprus", "Finland", "Mexico", "Austria", "Egypt", "Greece", "Argentina", "Peru", "Netherlands", "Germany", "Poland", "China", "Israel"]
	if nation in NationList:
		banner()
		if nation == "Italy":
			nation_short = "IT"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "USA":
			nation_short = "US"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "France":
			nation_short = "FR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Spain":
			nation_short = "ES"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Korea":
			nation_short = "KR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "India":
			nation_short = "IN"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Brazil":
			nation_short = "BR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Belgium":
			nation_short = "BE"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Romania":
			nation_short = "RO"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Canada":
			nation_short = "CA"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Vietnam":
			nation_short = "VN"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Croatia":
			nation_short = "HR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Serbia":
			nation_short = "SR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Turkey":
			nation_short = "TR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Japan":
			nation_short = "JP"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Russia":
			nation_short = "RU"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Albania":
			nation_short = "AL"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Cyprus":
			nation_short = "CY"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Finland":
			nation_short = "FI"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Mexico":
			nation_short = "MX"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Austria":
			nation_short = "AT"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Egypt":
			nation_short = "EG"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Greece":
			nation_short = "GR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Argentina":
			nation_short = "AR"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Peru":
			nation_short = "PE"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Netherlands":
			nation_short = "NL"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Germany":
			nation_short = "DE"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Poland":
			nation_short = "PL"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "China":
			nation_short = "CN"
			MakeRequests(url, nation_short, NationList, nation)
		elif nation == "Israel":
			nation_short = "IL"
			MakeRequests(url, nation_short, NationList, nation)
	else:
		print("\nError, use a valid nation, use --show to show that")


if args.show:
	for nation in NationList:
		print(nation)
	exit(0)

if args.old:
	try:
		import LibDavide
		menu()
	except NameError:
		pass
			
if args.output:
	file = args.output
	os.system("python3 CamHunter_V2.py --nation " + nation + " > " + file)

if args.version:
	print("""
CamHunter v2.1 by t0rt3ll1n0
-This script is only for fun-
Current version: 2.1 - 11/12/2020
First release: 1.0 - 20/07/2020
""")

if args.update:
	#check if root
	if os.geteuid() != 0:
		print("For update you need to run it as root")
		exit(0)
	print("Starting update...")
	os.chdir("../")
	os.system("sudo rm -rf CamHunterV2")
	os.system("git clone https://github.com/t0rt3ll1n0/CamHunterV2.git")
	os.chdir("CamHunterV2")
	print("\nCamHunter was successfully updated")