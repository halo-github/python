#!/usr/bin/python
#coding: UTF-8
urlStr = "http://blog.csdn.net/"
import urllib2,threading
class MyClass(threading.Thread):
	def __init__(self,thread_name,url):
		threading.Thread.__init__(self)
		self.setName(thread_name)
		self.url = url

	def run(self):
		req = urllib2.Request(self.url)
		response = urllib2.urlopen(req)
		data = response.read()
		fileHandle = open("csdnBlog.rtf","w")
		fileHandle.write(data)


if __name__ == '__main__':
	urlSite = raw_input("设置入口网址\n")
	id = MyClass("hello",urlSite)
	id.start()		
	
