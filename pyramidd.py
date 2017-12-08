from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

assets = [
'app.js',
'react.js',
'leaflet.js',
'D3.js',
'moment.js',
'math.js',
'main.css',
'bootstrap.css',
'normalize.css',
]

css = []
js = []

for element in assets:
  element_split = element.split('.')
  if element_split[1] == 'js':
    js.append(element)
  elif element_split[1] == 'css':
    css.append(element)

def index(request):
  env = Environment(loader=FileSystemLoader('.'))
  template = env.get_template('index.html').render(javascripts=js, styles=css)
  return Response(template)

def about(request):
  env = Environment(loader=FileSystemLoader('.'))
  template = env.get_template('about/about.html').render(javascripts=js, styles=css)
  return Response(template)

if __name__ == '__main__':
  config = Configurator()
  configure.add_route('index', '/index.html')
  config.add_view(index, route_name="index")
  configure.add_route('about', '/about/about.html')
  config.add_view(about, route_name="about")
  app = config.make_wsgi_app()
  make_server('0.0.0.0', 8000, app).serve_forever()