#!/usr/bin/python3
"""
This is a script that generates a .tgz archive from the contents of the web_static folder
"""


import os
import datetime
from fabric.operations import local

def do_pack():
    if os.path.isdir("versions"):
        os.mkdir("versions")

    date = datetime.now()
    dest = "versions/web_static{}{}{}{}{}{}.tgz".format(
        date.year,date.month,date.day,
        date.hour,date.minute,date.second
    )

    print("Packing web_static to {}".format(dest))
    local("tar -czvf {} web_static".format(dest))
    print("web_static packed: {} ->".format(dest))