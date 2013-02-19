S2-006 example

Affected Struts 2.2.1 and below

Solved with Struts 2.2.3

http://localhost:8080/s2-006/example/HelloWorld.action

Show vulnerability:
- change Struts2 version to 2.2.1
- copy application to Weblogic specific folder
- start Weblogic
- open browser
- paste url: http://localhost:7001/s2-006-1.0-SNAPSHOT/example/HelloWorld.action?action%3Alogin!login%3AcantLogin%3Cscript%3Ealert%28window.location%29%3C%2Fscript%3E%3Dsome_value=Submit
- stop Weblogic

The same example with Jetty works properly
