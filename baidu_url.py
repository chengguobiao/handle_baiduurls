# !/usr/bin/python
#-*-coding:utf-8-*-


import os

def extract_url():
	myurl = open('myurl.txt', 'wb')
	file_list = os.listdir('Baidu_url2')
	print file_list
	#for file in file_list:
	for i in range(len(file_list)):
		print file_list[i]
		txt_list = os.listdir('Baidu_url2' + '/' + file_list[i])
		for txt in txt_list:
			myfile = open('Baidu_url2' + '/' + file_list[i] + '/' + txt)
			myfile_list = myfile.readlines()
			for line in myfile_list:
				url = line.strip().split('!')
				myurl.write(url[1])
				myurl.write('\n')



extract_url()