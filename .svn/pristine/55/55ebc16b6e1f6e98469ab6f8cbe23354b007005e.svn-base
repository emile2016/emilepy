#coding:utf-8
import sae
import os
import sys
reload(sys)
#import djangoversion

#support django 1.8#################
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '.', 'site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "emilepy.settings")


from django.core.wsgi import get_wsgi_application  
application = get_wsgi_application() 
