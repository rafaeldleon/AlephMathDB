# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1280869811.866761
_template_filename=u'/home/rafaeldleon/Dropbox/workspace/AlephMathDB/alephmathdbserver/alephmathdbserver/templates/basedesign.mako'
_template_uri=u'/basedesign.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!doctype html>\n\n\n<html>\n  <head>\n    <script type="text/javascript" src="jquery.js"></script>\n\n    <script type="text/javascript">\n    $(document).ready(function(){\n   $("a").click(function(event){\n     alert("Thanks for visiting!");\n   });\n });  \n    </script>\n    <title>\n      AlephMathDB\n    </title>\n  </head>\n\n\n\n  <body>\n    ')
        # SOURCE LINE 23
        __M_writer(escape(next.body()))
        __M_writer(u'\n  </body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


