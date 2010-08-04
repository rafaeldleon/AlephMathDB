import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from alephmathdbserver.lib.base import BaseController, render

from pymongo import Connection
from datetime import datetime
log = logging.getLogger(__name__)

from formencode import Schema, validators, Invalid

class UploadForm(Schema):
    allow_extra_fields = True
    #filter_extra_fields = True
    email = validators.Email(not_empty=True)


class UploadobjectController(BaseController):

    def index(self):
        # Return a rendered template
        return render('/uploadobject.mako')

    def submit_object_info(self):
        schema = UploadForm()
        try:
            form_result = schema.to_python(dict(request.params))
        except Invalid, error:
            response.content_type = 'text/plain'
            return 'Invalid: '+unicode(error)
        else:
            #return 'Your email is: %s'%form_result.get('email')

            posts=dict(request.params);
            posts['date_of_creation']=datetime.utcnow()
            con = Connection('flame.mongohq.com', 27080)
            db = con.alephmathdb
            db.authenticate('aleph','Aiphootah3')
            collection = db.test_collection
            collection.insert(posts)
            redirect(url(controller='uploadobject', action='submit_obj_result'))

    def submit_obj_result(self):
        return 'Added in DB'
