import sys, os
INTERP = "/usr/bin/python2.4"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

os.environ['NORC_ENVIRONMENT'] = 'YOUR_NORC_ENVINROMENT'
os.environ['DJANGO_SETTINGS_MODULE'] = "norc.settings"
os.environ['PATH'] += ':' + os.getcwd() + '/norc/bin'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
