#!/usr/bin/python
#coding: UTF-8
urlStr = "http://blog.csdn.net/"
import requests,threading,re
class MyClass(threading.Thread):
	def __init__(self,thread_name,url):
		threading.Thread.__init__(self)
		self.setName(thread_name)
		self.url = url

	def run(self):
		try:
			req = requests.get(self.url,timeout = 1)
			data = req.text
		#	print data
			self.findUrl(data,0)
			#fileHandle = open("csdnBlog.rtf","w")
			#fileHandle.write(data)
		except :
			print "type error"
		finally:
			print "ok"
		
	def findUrl(self,html,depth):	
		if (depth == 0):
			reStr1 = r'"http.+?"'
			reStr2 = r'"(/?[^\s<>]+?/[^\s<>]+?)"'

#			comp1 = re.compile(reStr1)
#			list1 = re.findall(comp1,html)

			comp2 = re.compile(reStr2)
			list2 = re.findall(comp2,html)
			list2.sort()
			for s2 in list2:
				print s2
			#	r = requests.get(s,timeout=1)

			
if __name__ == '__main__':
	urlSite = raw_input("设置入口网址\n")
	id = MyClass("hello",urlSite)
	id.start()		
	
