# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1280901786.5808091
_template_filename='/home/rafaeldleon/Dropbox/workspace/AlephMathDB/alephmathdbserver/alephmathdbserver/templates/uploadobject.mako'
_template_uri='/uploadobject.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/basedesign.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<h1>Enter Object description</h1> <br/> <br/>\n    ')
        # SOURCE LINE 3
        __M_writer(escape(h.form('submit_object_info', method='post')))
        __M_writer(u'\n<!-- Accordion -->\n\t\t<h2 class="Headers">DAS</h2>\n\t\t<div id="accordion">\n\t\t\t<div>\n\t\t\t\t<h3><a href="#">Information about the submitter</a></h3>\n\t\t\t\t\n    \t\t\t\t<div> Author: <br/> ')
        # SOURCE LINE 10
        __M_writer(escape(h.text('author')))
        __M_writer(u' <br/>\n                                 Email Address:  <br/> ')
        # SOURCE LINE 11
        __M_writer(escape(h.text('email')))
        __M_writer(u' </div>\n\n\t\t\t</div>\n\t\t\t<div>\n\t\t\t\t<h3><a href="#">Basic information about the object</a></h3>\n\t\t\t\t<div>Phasellus mattis tincidunt nibh.\n    Name of Object:  <br/> ')
        # SOURCE LINE 17
        __M_writer(escape(h.text('name')))
        __M_writer(u' <br/>\n    Description:  <br/> ')
        # SOURCE LINE 18
        __M_writer(escape(h.textarea('description')))
        __M_writer(u' <br/>\n    Format:  <br/> ')
        # SOURCE LINE 19
        __M_writer(escape(h.select('format','',[('format 1','format 1'),('format 2','format 2')],class_='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only')))
        __M_writer(u' <br/>\n     \n    Object:  <br/> ')
        # SOURCE LINE 21
        __M_writer(escape(h.text('object')))
        __M_writer(u' <br/></div>\n\t\t\t</div>\n\t\t\t<div>\n\t\t\t\t<h3><a href="#">Additional Information</a></h3>\n\t\t\t\t<div>Keywords:  <br/> ')
        # SOURCE LINE 25
        __M_writer(escape(h.text('tags')))
        __M_writer(u' <br/></div>\n\t\t\t</div>\n\t\t</div>\n    \n\n\n   ')
        # SOURCE LINE 31
        __M_writer(escape(h.submit('submit','Submit Object',class_="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only")))
        __M_writer(u'\n   ')
        # SOURCE LINE 32
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


