S2-011 example

Affected Struts 2.3.4 and below

Solved with Struts 2.3.4.1

http://localhost:8080/s2-011/example/HelloWorld.action

Show vulnerability:
- change Struts2 version to 2.3.4
- start application: `mvn jetty:run`
- start Activity Monitor to demonstrate CPU/memory consumption
- start `python dos.py` script
- stop Jetty and script

Show solution:
- change Struts2 version to 2.3.4.1
- start application: `mvn jetty:run`
- start Activity Monitor to demonstrate CPU/memory consumption
- start `python dos.py` script
- stop Jetty and script
