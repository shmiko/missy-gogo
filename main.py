from framework import bottle
from framework.bottle import route, template, request, error, debug
from google.appengine.ext.webapp.util import run_wsgi_app


@route('/search')
def search_form():
    output = template('templates/search')
    return output

@route('/results', method='GET')
def process_search():
    search_query = request.GET.get('search_query', '').strip()
    return template('templates/results', search_query=search_query)

@route('/')
def DisplayForm():
    message = 'Hello World'
    output = template('templates/home', data = message)
    return output
 
def main():
    debug(True)
    run_wsgi_app(bottle.default_app())
 
@error(403)
def Error403(code):
    return 'Get your codes right dude, you caused some error!'
 
@error(404)
def Error404(code):
    return 'Stop cowboy, what are you trying to find?'
 
if __name__=="__main__":
    main()