#!/usr/bin/python3
"""
Fabric script for deploying an archive to web servers
"""
import os.path
from fabric.api import env, run, put

env.hosts = ["100.25.36.59", "100.24.255.151"]


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
