#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""
import os.path
from fabric.api import local
from datetime import datetime


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
