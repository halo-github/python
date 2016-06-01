#!/usr/bin/python
#coding: UTF-8
urlStr = "http://blog.csdn.net/"
import requests,threading,re,Queue
class MyClass(threading.Thread):
	def __init__(self,url,queue):
		threading.Thread.__init__(self)
		self.url = url
		self.queue = queue

	def run(self):
		global mutex
		file = open("csdn.rtf","wb")
		try:	
			siteList = file.read()
			if siteList:
				global x,mutex
			#	mutex.acquire()
				print siteList[x]
				x = x+1
				print x
			#	mutex.release()
				
			else :
				req = requests.get(self.url,timeout = 1)
				data = req.text
				self.findUrl(data,0)
				file.write(siteList)
				
		except :
			print "type error"
		finally:
			file.close()	
	def findUrl(self,html,depth):
		global siteList	
		host = self.url.split("/")[2]
		print host
		reStr1 = r'"(/[^\s<>/]+?/[^\s<>]+?)"'
		reStr2 = r'"(http.+?)"'
		comp1 = re.compile(reStr1)
		comp2 = re.compile(reStr2)
		list1 = re.findall(comp1,html)
		list2 = re.findall(comp2,html)
		list3 = []
		for s in list1:
			list3.append(host+s)
		siteList = list2 + list3
def main():			
	global siteList
	mutex = threading.Lock()
	queue = Queue.Queue()	
	siteList = []
	urlSite = raw_input("设置入口网址\n")
	id = MyClass(urlSite,queue)
	id.start()		
	id.join()
	
	for i in siteList:
		id = MyClass(i,queue)
		id.start()	
		id.join()
x = 0
if __name__ == '__main__':
	main()
