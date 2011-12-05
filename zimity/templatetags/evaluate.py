# Written by Conan Albrecht <conan@warp.byu.edu>
# Released into the public domain, June 2011
# This file has no warranty, express or implied.  
# Use at your own risk.

from django import template
register = template.Library()
import logging; log = logging.getLogger('django')

__doc__ = '''
   An arbitrary method caller for the Django template system
   This possibly breaks logic/presentation separation Django
   works so hard to keep, but it can be incredibly useful
   when done correctly.

   EXAMPLE (the following goes in an html template file):

   <html><body>
   Hello world.
   {% load evaluate %}
   {% import random math %}
   Your random number is: {% eval random.randint(1, 100) %}
   Another number is: {% eval math.floor(somefloatvariable) # assuming this float came from views.py %}
   </body></html>

   INSTALLATION: 

   Place this file in your {app}/templatetags directory (create
   it if necessary).  Then add the location of the evaluate.py
   file to your global settings.py file (in the string below,
   {app}.templatetags.evaluate refers to evaluate.py, 
   .context_processor refers to a function within evaluate.py):

   TEMPLATE_CONTEXT_PROCESSORS = (
     "{app}.templatetags.evaluate.context_processor",
   )

   Note that other context processors must also be included in the
   the tuple.  As of Django 1.3, the following is the full tuple:

   TEMPLATE_CONTEXT_PROCESSORS = (
     "django.core.context_processors.request",
     "django.contrib.auth.context_processors.auth",
     "django.core.context_processors.debug",
     "django.core.context_processors.i18n",
     "django.core.context_processors.media",
     "django.core.context_processors.static",
     "django.contrib.messages.context_processors.messages",
     "{app}.templatetags.evaluate.context_processor",
   )
'''

def context_processor(request):
  '''Adds our __evaluate_tag_modules variable to the request context'''
  return { '__evaluate_tag_modules': {} }
  

@register.tag(name="eval")
def do_evaluate(parser, token):
  '''Calls an arbitrary method on an object.'''
  code = token.contents
  firstspace = code.find(' ')
  if firstspace >= 0:
    code = code[firstspace+1:]
  return Evaluator(code)

class Evaluator(template.Node):
  '''Calls an arbitrary method of an object'''
  def __init__(self, code):
    self.code = code
    
  def render(self, context):
    '''Evaluates the code in the page and returns the result'''
    return str(eval(self.code, context['__evaluate_tag_modules'], context))
  

@register.tag(name="import")
def do_import(parser, token):
  '''Imports a module into the evaluate context'''
  return ImportRenderer(token.split_contents()[1:])
  
class ImportRenderer(template.Node):
  '''Imports a module into the evaluate context'''
  def __init__(self, modulenames):
    self.modulenames = modulenames
    
  def render(self, context):
    '''Adds the module to the current request context'''
    assert '__evaluate_tag_modules' in context, 'Invalid configuration for evaluate template tag: you need to add "{app}.templatetags.evaluate.context_processor" to TEMPLATE_CONTEXT_PROCESSORS in settings.py.  See the Django docs for TEMPLATE_CONTEXT_PROCESSORS for more information.'
    for modulename in self.modulenames:
      if not modulename in context['__evaluate_tag_modules']:
        module = __import__(modulename)
        context['__evaluate_tag_modules'][modulename] = module
    return ''

    
    
    
    
    
    