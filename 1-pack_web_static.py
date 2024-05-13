#!/home/caitlyn/venvs/alxstatic/bin/python3

"""Generates a .tgz archive from the contents of the web_static folder
of the AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local('mkdir -p versions')
    # year,month,day,hour,minute,second
    time = datetime.now().strftime('%y%m%d%I%M%S')
    local(f'tar -cvf versions/web_static_{time}.tgz web_static')
