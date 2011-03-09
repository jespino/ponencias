from fabric.api import run, put, env, local, sudo
from fabric.decorators import roles

env.roledefs = {
    'db': [ "db1.myserver.com", "db2.myserver.com", "db3.myserver.com" ],
    'dns': [ "dns1.myserver.com", "dns2.myserver.com" ],
    'www': [ "www1.myserver.com", "www2.myserver.com", "www3.myserver.com" ]
}

@roles('db')
def deploy_db():
    put("database_dump.sql","/tmp/database_dump.sql")
    run("mysql -u root myserver_db < /tmp/database_dump.sql")
    run("rm /tmp/database_dump.sql")

@roles('dns')
def deploy_dns():
    #sudo("bash /usr/local/bin/update-dns.sh")
    sudo("true")

@roles('www')
def deploy_www():
    local("tar -zcf webapp.tar.gz webapp")
    put("/tmp/webapp.tar.gz","webapp.tar.gz")
    sudo("tar -zxf /tmp/webapp.tar.gz -C /var/www")
    run("php /var/www/webapp/scripts/update_db.php")
