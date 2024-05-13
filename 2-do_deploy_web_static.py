#!/usr/bin/python3

"""Generates a .tgz archive from the contents of the web_static folder
of the AirBnB Clone repo, using the function do_pack.
"""

from pathlib import Path
from fabric.api import *
from datetime import datetime

env.hosts = ['54.160.122.175', '54.208.168.38']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

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


def do_deploy(archive_path):
    """Distributes an archive to a set of web servers"""

    archive_path = Path(archive_path)
    if not Path.exists(Path(archive_path)):
        return False

    put(archive_path, '/tmp/')

    # decompress the archive to a specified location, and delete the archive
    archive_name = archive_path.name
    untar_dest = f'/data/web_static/releases/{archive_path.stem}'
    run(f'mkdir -p {untar_dest}')
    run(f'tar -xf /tmp/{archive_name} -C {untar_dest}')
    run(f'rm /tmp/{archive_name}')

    # move contents of web_static one level outwards
    run(f'mv {untar_dest}/web_static/* {untar_dest}')
    run(f'rm -rf {untar_dest}/web_static/')

    # update symbolic link to the new codebase
    sym_link = '/data/web_static/current'
    run(f'rm {sym_link}')
    run(f'ln -s {untar_dest}/ {sym_link}')
