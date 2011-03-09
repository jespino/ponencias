from fabric.api import run, put, env, local

env.hosts = [ "www.myserver.com"]

def deploy():
    local("tar -zcf webapp.tar.gz webapp")
    local("tar -zcf static_files.tar.gz static_files")
    put("static_files.tar.gz","/tmp/static_files.tar.gz")
    put("webapp.tar.gz","/tmp/webapp.tar.gz")
    put("ws.war","/tmp/ws.war")
    sudo("tar -zxf /tmp/webapp.tar.gz -C /var/www")
    sudo("tar -zxf /tmp/static_files.tar.gz -C /var/static-www/")
    sudo("mv /tmp/ws.war /opt/tomcat/webapps/ws.war")
