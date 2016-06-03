#!/usr/bin/python
#coding: UTF-8
urlStr = "http://blog.csdn.net/"
import requests,threading,re,Queue
class MyClass(threading.Thread):
	def __init__(self,queue,lock):
		threading.Thread.__init__(self)
		self.queue = queue
		self.lock = lock

	def run(self):
	  try:	
	    while 1:	
		if self.queue.qsize()>0:
			if self.lock.acquire(1):
				print "加锁1"
				if self.queue.qsize()==0:
					print "解锁1"
					self.lock.release()	
				url = self.queue.get()
				print self.name + " get url from queue"
				self.lock.release()	
				print "解锁1"
				print url
				req = requests.get(url,timeout = 10)
				data = req.text
				print self.name + " is running"
				self.findUrl(url,data)
  	  except :
	  	  pass
	  finally:
		  print "ok"

	def findUrl(self,url,html):
		print "find url start..."
		siteList = []
		global mutex
		try:
			host = url.split("/")[2]
			reStr1 = r'"(/[^\s<>/]+?/[^\s<>]+?)"'
			reStr2 = r'"(http.+?)(!.js)"'
			comp1 = re.compile(reStr1)
			comp2 = re.compile(reStr2)
			list1 = re.findall(comp1,html)
			list2 = re.findall(comp2,html)
			list3 = []
			for s in list1:
				list3.append(host+s)
			siteList = list2 + list3		
			print  self.lock
			if self.lock.acquire(1):
				print "加锁2"
				for i in siteList:
					self.queue.put(i)
				self.lock.release()	
				print "解锁2"
			print self.queue.qsize()
		finally:
			print
		
def main():			
	global siteList,mutex
	mutex = threading.Lock()
	queue = Queue.Queue()
	urlSite = raw_input("设置入口网址\n")
	queue.put(urlSite)
	threads = [MyClass(queue,mutex) for x in xrange(10)]
	for t in threads:
		t.start()
if __name__ == '__main__':
	main()
