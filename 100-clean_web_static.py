#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""
import os.path
from fabric.api import *

env.hosts = ["100.25.36.59", "100.24.255.151"]


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    number = 1 if int(number) == 0 else int(number)

    with lcd("versions"):
        # Local cleanup
        local("ls -t | tail -n +{} | xargs -I {{}} rm {{}}".format(number + 1))

    with cd("/data/web_static/releases"):
        # Remote cleanup
        archives = run("ls -tr | grep 'web_static_'").split()
        archives = archives[:-number]
        [run("rm -rf ./{}".format(a)) for a in archives]
