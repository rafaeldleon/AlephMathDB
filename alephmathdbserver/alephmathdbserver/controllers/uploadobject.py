import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from alephmathdbserver.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UploadobjectController(BaseController):

    def index(self):
        # Return a rendered template
        return render('/uploadobject.mako')
        # or, return a string
        #return 'Hello World'

    def email(self):
        return 'Your email is: %s' % request.params['email']
