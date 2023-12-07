#!/usr/bin/python3
"""
This is a script that generates a .tgz archive
from the contents of the web_static folder
"""


import os
from datetime import datetime
from fabric.api import *

env.hosts = ["100.25.222.245", "100.25.0.44"]
env.user = "ubuntu"


def do_pack():
    """Function that packs web_static to .tgz archive"""
    date = datetime.now()
    dest = "versions/web_static{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day,
        date.hour, date.minute, date.second
    )

    try:
        local("mkdir -p versions")
        print("Packing web_static to {}".format(dest))
        local("tar -czvf {} web_static/".format(dest))
        print("web_static packed: {} -> {}Bytes".format(dest,
                                                        os.stat(dest).st_size))
    except Exception as e:
        dest = None
    return dest


def do_deploy(archive_path):
    """Function to deploy archive to web servers"""
    if not archive_path:
        return False

    compressed = archive_path[9:]  # eg. web_static_20170315003959.tgz
    unpacked = "/data/web_static/releases/" + compressed[:-4]
    # eg. /data/web_static/releases/web_static_20170315003959/

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(unpacked))
        run("tar -xzf {} -C {}".format("/tmp/" + compressed, unpacked))
        run("rm {}".format("/tmp/" + compressed))
        run("mv {} {}".format(unpacked + "/web_static/*", unpacked))
        run("rm -rf {}".format(unpacked + "/web_static"))
        run("rm -rf {}".format("/data/web_static/current"))
        run("ln -s {} /data/web_static/current".format(unpacked))
        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
