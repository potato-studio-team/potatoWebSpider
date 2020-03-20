import requests
import re
import json
from bs4 import BeautifulSoup
import datetime

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
	fileData = readFileLine("test.posp")

	saveFileName = "none"
	html = "none"
	url = "none"
	result = "none"

	err = [0,]

	for root in fileData:
		key = re.search(r"^[a-z,A-z]+",root).group(0)
		root = root.strip(key)

# 标题----------------------------------------------------------------------

		if key == "title":
			root = root.strip("=").strip("\n")
			root = "\n" + root + "\n"
			print(root)

# 文件处理------------------------------------------------------------------

		elif key == "file":
			root = root.strip("&")
			key = re.search(r"^[a-z,A-z]+",root).group(0)
			root = root.strip(key).strip("\n").strip("=")

			if key == "new":
				writeFileN(root,"")
				saveFileName = root

			elif key == "writeWord":
				if saveFileName == "none":
					print("!!!编译错误：文件还未创建，不可写入!!!")
					err = []
				else:
					writeFileA(saveFileName,root)

			elif key == "writeValue":
				if root == "time":
					today = datetime.date.today()
					today = str(today)

					today = today + "\n"

# 爬虫核心处理---------------------------------------------------------------

		elif key == "url":
			root = root.strip("&")
			key = re.search(r"^[a-z,A-z]+",root).group(0)
			root = root.strip(key).strip("=").strip("\n")

			if key == "get":
				url = root
				
				print(url)

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
					html = r.text
					print("##已完成抓取##\n")
				except:
					print("##抓取错误##\n")
					html = "Error"

			# elif key == "save":

	input("\n回车退出")
		
main()