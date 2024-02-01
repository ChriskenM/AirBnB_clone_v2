#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
creates & distributes an archive to web servers, uses the function deploy
"""
import os.path
from datetime import datetime
from fabric.api import put, run, env, local

env.hosts = ["100.25.36.59", "100.24.255.151"]


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    date_str = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_str.year,
                                                         date_str.month,
                                                         date_str.day,
                                                         date_str.hour,
                                                         date_str.minute,
                                                         date_str.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/"
            .format(name)).failed is True:
        return False

    if run("mkdir -p /data/web_static/releases/{}/"
            .format(name)).failed is True:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False

    return True


def deploy():
    """
    Calls do_pack() and do_deploy() functions.
    to Create and distribute an archive to a web server.
    """
    file = do_pack()
    if file is None:
        return False

    return do_deploy(file)
