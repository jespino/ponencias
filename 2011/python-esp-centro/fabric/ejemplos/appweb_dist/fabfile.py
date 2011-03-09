from fabric.api import run, put, env, local

env.hosts = [ "www1.myserver.com", "www2.myserver.com", "www3.myserver.com" ]

def deploy():
    local("tar -zcf webapp.tar.gz webapp")
    put("webapp.tar.gz","/tmp/webapp.tar.gz")
    sudo("tar -zxf /tmp/webapp.tar.gz -C /var/www")
    run("php /var/www/webapp/scripts/update_db.php")
