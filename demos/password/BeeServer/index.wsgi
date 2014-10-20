import sae
from BeeServer import wsgi

application = sae.create_wsgi_app(wsgi.application)
