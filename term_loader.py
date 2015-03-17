from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.tools import bulkloader
#from models import PythonTerm

class PythonTerm(db.Model):
	"""Models a term from the Python glossary."""
	term = db.StringProperty()
	definition = db.TextProperty()

def store_pythonterm(query, result):
		pythonterm = PythonTerm(term=query, definition=result)
		pythonterm.put()

class PythonTermLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self, 'PythonTerm',
			[('term', str),
			('definition', str)
			])
loaders = [PythonTermLoader]


appcfg.py upload_data --config_file="bulkloader.yaml" --filename="function_dict.csv" --url=http://missy-go.appspot.com/remote_api --application=missy-go --kind=PythonTerm --email=shmiko@gmail.com --passin

#appcfg.py upload_data --url=http://127.0.0.1:8088/remote_api --filename=function_dict.csv --has_header --application=dev~missy-go --kind=PythonTerm
appcfg.py upload_data --config_file="bulkloader.yaml" --filename="function_dict.csv" --url=http://missy-go.appspot.com:8088/remote_api --application=missy-go --kind=PythonTerm --email=shmiko@gmail.com --passin
appcfg.py upload_data --application=missy-go --config_file="bulkloaderb.yaml" --filename="customer.csv" --kind=Customer --url=http://missy-go.appspot.com:8080/remote_api