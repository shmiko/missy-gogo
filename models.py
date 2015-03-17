#from dist import google.appengine.ext 
from google.appengine.ext import db

class PythonTerm(db.Model):
	"""Models a term from the Python glossary."""
	term = db.StringProperty()
	definition = db.TextProperty()

def store_pythonterm(query, result):
		pythonterm = PythonTerm(term=query, definition=result)
		pythonterm.put()


#!/usr/bin/python2.5
# Copyright 2009 Google Inc.
#

"""Sample Datastore models."""

import datetime

from google.appengine.ext import db
from google.appengine.ext.db import polymodel

# Models

class Customer(db.Model):
  """Very simple Customer class.

  Uses named keys.
  """
  name = db.StringProperty()
  phone = db.PhoneNumberProperty()
  created = db.DateTimeProperty()


class Visit(db.Model):
  """Very simple customer visit class."""
  customer = db.ReferenceProperty(Customer)
  visit_date = db.DateTimeProperty()
  score = db.FloatProperty()
  activities = db.ListProperty(str)


class VisitActivity(db.Model):
  """An alternate way to represent activites.

  This uses a child entity instead of listproperty. You probably
  shouldn't do this for such a simple case, it's far less efficient.
  
  This exists as a demo for how you might handle a more complex entity group.

  Key is ('Visit', visit id, 'VisitActivity', activity). We'll duplicate
  activity as a property too even though that's unnecessary.
  """
  actvity = db.StringProperty()


class CustomerCall(db.Model):
  """Another very simple example class."""
  customer = db.ReferenceProperty(Customer)
  call_date = db.DateTimeProperty()
  answered = db.BooleanProperty()


class Attachment(db.Model):
  filename = db.StringProperty()
  filecontents = db.BlobProperty()

# Polymodel
# http://groups.google.com/group/google-appengine-python/browse_thread/thread/d92179c712bda721

class Badge(db.Model):
  name = db.StringProperty()
  level = db.IntegerProperty()

class Person(polymodel.PolyModel):
  first_name = db.StringProperty()
  last_name = db.StringProperty()

class Adult(Person):
  interests = db.StringListProperty()