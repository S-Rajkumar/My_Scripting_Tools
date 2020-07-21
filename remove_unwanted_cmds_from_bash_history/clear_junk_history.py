#!/usr/bin/env python3

'''
@author = udmnxpdu
date = July 2020
'''

#change to your username to read your .bash_history
f = open('/home/smiley/.bash_history','r').readlines()
nf = open('/home/smiley/.bash_history','w')
for line in f :
	line = line.strip()
	#Here all junks for mine you can edit by yourself for what you want
	if 'ls' in line[:3] or 'cd' in line[:3] or 'mv' in line[:3] or 'mkdir ' in line[:6] or 'cat' in line[:4] or 'history' in line[:8] or 'rm' in line[:3] or 'strings ' in line[:8] or 'python3' in line[:8] or 'python' in line[:7] or 'exiftool ' in line[:9] or 'nano ' in line[:5] or 'echo' in line[:4] or 'locate' in line[:7] or 'pluma' in line[:6] or 'vi' in line[:3] or 'pwd' in line[:4] or 'cp' in line[:3] or 'bye' in line[:4] or 'file' in line[:5] or 'display' in line[:8] or 'gdp' in line[:4] or 'wget' in line[:5] or 'tree' in line[:5] or 'firefox' in line[:8] or 'clear' in line[:6] or 'ifconfig' in line[:9] or 'chmod' in line[:6] or 'gdb' in line[:4] or 'nc' in line[:3] or 'vlc' in line[:4] or 'java' in line[:5] or 'ftp' in line[:4] or 'nmap' in line[:5] or 'wc' in line[:3] or 'exit' in line[:5] or 'service' in line[:8] or './' in line[:3] or 'git' in line[:4] or 'zsteg' in line[:6] or 'ping' in line[:5] or 'zip' in line[:4] or 'unzip' in line[:6] or 'sudo openvpn' in line or 'steghide' in line[:9] or 'stegosuite' in line[:11] or 'stegsnow' in line[:9] or 'binwalk' in line[:8] or 'curl' in line[:5] or 'find' in line[:5] or 'pip' in line[:4] or 'pip3' in line[:5] or 'sudo nano' in line or 'sudo rm ' in line or 'go' in line[:3] or 'ngrok' in line[:6] or 'sudo python3' in line or 'sudo python' in line or 'sudo -s' in line or 'sudo -l' in line or 'sudo service' in line or 'gcc' in line[:4] or 'g++' in line[:4] :
		continue
	nf.write(line+'\n')
