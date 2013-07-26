import os
import time

from fabric.api import *
from fabric.utils import puts
from fabric.contrib.project import rsync_project


local_dir = '~/dev/projects/koken_template/'
remote_dir = '/var/www/romanaverin.com/'


#If no local_settings.py then settings.py
try:
    from pelicanconf_local import OUTPUT_PATH
    SETTINGS_FILE = "pelicanconf_local.py"
except ImportError:
    from pelicanconf import OUTPUT_PATH
    SETTINGS_FILE = "pelicanconf.py"

# Get directories
ABS_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ABS_SETTINGS_FILE = os.path.join(ABS_ROOT_DIR, SETTINGS_FILE)
ABS_OUTPUT_PATH = os.path.join(ABS_ROOT_DIR, OUTPUT_PATH)


#Commands

@hosts('root@webserver01.rastler.ru')
def sync():
	"""Push data to remote host"""
	local("make html")
	rsync_project(remote_dir, local_dir, delete=True)
	with cd(remote_dir):
		run('chown -R www-data:www-data *')
