import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoApp.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def test():  
   print('test')   

if __name__ == '__main__':  
   test()