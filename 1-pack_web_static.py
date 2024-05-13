#!/usr/bin/python3

"""Generates a .tgz archive from the contents of the web_static folder
of the AirBnB Clone repo, using the function do_pack.
"""

from pathlib import Path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    versions_dir = Path('versions/')
    if not Path.exists(versions_dir):
        Path.mkdir(versions_dir)
    # year,month,day,hour,minute,second
    time = datetime.now().strftime('%y%m%d%I%M%S')
    tar_path = Path(versions_dir, f'web_static_{time}.tgz')
    local(f'tar -cvf {tar_path} web_static')

    if Path.exists(tar_path):
        return tar_path
    return None
