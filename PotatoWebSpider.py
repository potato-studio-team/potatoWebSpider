import requests
import re
import json
from bs4 import BeautifulSoup
import datetime

def spiderRoot(url):
    try:
        send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
        }#伪装成浏览器

        r = requests.get(url,send_headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return "Error"

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
	fileData = readFileLine(input("请输入子雨爬虫配置文件XXX.posp位置\n>>>"))

	saveFileName = "none"
	textWeb = "none"
	url = "none"
	result = "none"
	htmlHeaders = "none"

	for root in fileData:
		key = re.search(r"^[a-z,A-z]+",root).group(0)
		root = root.strip(key)

# 标题----------------------------------------------------------------------

		if key == "title":
			root = root.strip("=").strip("\n")
			root = "\n" + root + "\n"

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
					break

				else:
					root = root + "\n"
					writeFileA(saveFileName,root)

			elif key == "writeValue":
				# 错误分析
				if root == "time":
					if saveFileName == "none":
						print("!!!编译错误：文件还未创建，不可写入!!!")
						break

					else:
						today = datetime.date.today()
						today = str(today)
	
						today = today + "\n"
						writeFileA("saveFileName",today)
						print("##时间信息已写入##")

				# 写入访问头部信息
				if root == "headers":
					# 错误分析
					if saveFileName == "none":
						print("!!!编译错误：文件还未创建，不可写入!!!")
						break

					elif htmlHeaders  == "none":
						print("!!!编译错误：没有抓取，无法返回请求头信息!!!")
						break

					else:
						headers = str(htmlHeaders) + "\n"
						writeFileA(saveFileName,headers)
						print("##头部信息已写入##")

				# 直接写入html
				if root == "textWeb":
					# 错误分析
					if saveFileName == "none":
						print("!!!编译错误：文件还未创建，不可写入!!!")
						break

					elif textWeb == "none":
						print("!!!编译错误：没有抓取，不可写入!!!")
						break

					else:
						html = "\n本次爬取的网站内容如下\n" + str(textWeb) + "\n"
						writeFileA(saveFileName,textWeb)
						print("##网站抓取内容信息已写入##")

				# 写入处理结果
				if root == "result":
					if saveFileName == "none":
						print("!!!编译错误：文件还未创建，不可写入!!!")
						break

					elif result == "none":
						print("!!!编译错误：没有信息被处理，不可写入!!!")
						break

					else:
						writeFileA("saveFileName",result)

# 爬虫核心处理---------------------------------------------------------------

		elif key == "url":
			root = root.strip("&")
			key = re.search(r"^[a-z,A-z]+",root).group(0)
			root = root.strip(key).strip("=").strip("\n")

			if key == "get":
				url = root

				pti = "正在抓取" + url + "......\n"
				print(pti)

				spiderResult = spiderRoot(url)
				if spiderResult == "Error":
					print("##抓取错误##\n")

				else:
					print("##抓取成功##\n")
					htmlHeaders = spiderResult.headers
					textWeb = spiderResult.text


	input("\n回车退出")
		
main()