import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from alephmathdbserver.lib.base import BaseController, render

from pymongo import Connection
from datetime import datetime
log = logging.getLogger(__name__)

class UploadobjectController(BaseController):

    def index(self):
        # Return a rendered template
        return render('/uploadobject.mako')

    def email(self):
        posts={};
        for key in request.params:
            posts[key]=request.params[key]
        posts['date_of_creation']=datetime.utcnow()
        con = Connection('localhost', 27017)
        db = con.testdb
        collection = db.test_collection
        collection.insert(posts)
        #return 'Your email is: %s' % request.params['email']
        return 'Added in DB'
