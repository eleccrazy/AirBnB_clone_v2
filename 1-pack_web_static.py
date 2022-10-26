#!/usr/bin/python3
"""This python script uses flask and geneates a .tgz file file."""
from datetime import datetime
from os.path import exists
from fabric.api import local


def do_pack():
    """A method that acomplishes the above objective"""
    now = datetime.now()
    appended_name = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + appended_name + ".tgz"

    if not exists("versions"):
        if local("mkdir -p versions").succeeded is False:
            return None
    if local("tar -cvzf {} web_static".format(archive_name)).failed is True:
        return None

    return archive_name
