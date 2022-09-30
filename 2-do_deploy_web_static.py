#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""

from fabric.api import *
from datetime import datetime
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['3.239.86.158', '34.239.166.29']


def do_pack():
    """ Generate a .tgz archive from the contents of the web_static folder """
    time = datetime.now()
    name = 'web_static_' + str(time.year) + str(time.month) + str(time.day)
    name = name + str(time.hour) + str(time.minute) + str(time.second) + '.tgz'
    local('mkdir -p versions')
    archive = local('tar -cvzf versions/{} web_static'.format(name))
    if archive.failed:
        return None
    return 'versions/{}'.format(name)


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy
    """
    file_path = exists(archive_path)
    if not file_path:
        return file_path
    put('{}'.format(archive_path), '/tmp/')
    archive__ = archive_path.split('.')
    archive_ = archive__[0].split("/")
    archive = archive_[1]
    run("mkdir -p /data/web_static/releases/{}/".format(archive))
    run("tar -xzf /tmp/{}.tgz -c /data/web_static/releases/{}/".format(
        archive, archive))
    run("rm /tmp/{}.tgz".format(archive))
    run('mv /data/web_static/releases/{}/web_static/* '.format(archive) +
        '/data/web_static/releases/{}/'.format(archive))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(archive))
    run('rm -rf /data/web_static/current')
    run("ls -s /data/web_static/releases/{}/ "
        "/data/web_static/current".format(archive))
    print("New version deployed!")
    return True
