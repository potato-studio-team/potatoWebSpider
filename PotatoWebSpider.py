import requests
import re
import json
from bs4 import BeautifulSoup
import os

def readFileLine(place):
	with open(place, encoding="utf-8") as f:
		content = f.readlines()
	return content

def writeFileN(place,data):
	data = str(data)
	filehandle = open(place,'w', encoding="utf-8")
	filehandle.write(data)
	filehandle.close()

def writeFileA(place,data):
	data = str(data)
	filehandle = open(place,'a', encoding="utf-8")
	filehandle.write(data)
	filehandle.close()

def main():
	fileData = readFileLine("a.posp")

	saveFileName = "none"
	html = "none"
	url = "none"
	result = "none"

	for root in fileData:
		key = re.search(r"^[a-z,A-z]+",root).group(0)
		root = root.strip(key)

		if key == "title":
			data = root.strip("=")
			print(data)

		elif key == "file":
			root = .strip("&")
			key = re.search(r"^[a-z,A-z]+",root).group(0)
			root = key.strip(key)

			if key == "new":
				writeFileN(root,"")
				saveFileName = root

			elif key == "writeWorld":
				if save == "none":
					print("!!!文件还未创建，不可写入!!!")

				else:
					writeFileA(saveFileName,root)

			elif key == "value":
				if root == "time":



		elif key == "url":
			root = .strip("&")
			key = re.search(r"^[a-z,A-z]+",root).group(0)
			root = key.strip(key)

			if key = "get":
				url = root.strip("=")
				
				try:		
					send_headers = {
					"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
					"Connection": "keep-alive",
					"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
					"Accept-Language": "zh-CN,zh;q=0.8"
					}#伪装成浏		
					r = requests.get(url,send_headers)
					r.raise_for_status()
					r.encoding = r.apparent_encoding
					r = r.text
					print("##已完成抓取##\n")
    			except:
					print("##抓取错误##\n")
					r = "Error"

			elif key == "save":


	
main()