#!/usr/bin/python3
"""
This is a script that generates a .tgz archive
from the contents of the web_static folder
"""


import os
import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    if os.path.isdir("versions"):
        os.mkdir("versions")

    date = datetime.now()
    dest = "versions/web_static{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day,
        date.hour, date.minute, date.second
    )

    try:
        print("Packing web_static to {}".format(dest))
        local("tar -czvf {} web_static".format(dest))
        print("web_static packed: {} -> {}Bytes".format(dest,
                                                        os.stat(dest).st_size))
    except Exception as e:
        dest = None
    return dest
