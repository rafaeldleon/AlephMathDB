# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1280902562.924154
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
        __M_writer(u'<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />\n\t\t<title>AlephMathDB</title>\n\t\t<link type="text/css" href="../css/custom-theme/jquery-ui-1.8.2.custom.css" rel="stylesheet" />\t\n\t\t<script type="text/javascript" src="../js/jquery-1.4.2.min.js"></script> \n\t\t<script type="text/javascript" src="../js/jquery-ui-1.8.2.custom.min.js"></script>\n\t\t<script type="text/javascript">\n\t\t\t$(function(){\n\n\t\t\t\t// Accordion\n\t\t\t\t$("#accordion").accordion({ header: "h3" });\n\t\n\t\t\t\t// Tabs\n\t\t\t\t$(\'#tabs\').tabs();\n\t\n\n\t\t\t\t// Dialog\t\t\t\n\t\t\t\t$(\'#dialog\').dialog({\n\t\t\t\t\tautoOpen: false,\n\t\t\t\t\twidth: 600,\n\t\t\t\t\tbuttons: {\n\t\t\t\t\t\t"Ok": function() { \n\t\t\t\t\t\t\t$(this).dialog("close"); \n\t\t\t\t\t\t}, \n\t\t\t\t\t\t"Cancel": function() { \n\t\t\t\t\t\t\t$(this).dialog("close"); \n\t\t\t\t\t\t} \n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t\t\n\t\t\t\t// Dialog Link\n\t\t\t\t$(\'#dialog_link\').click(function(){\n\t\t\t\t\t$(\'#dialog\').dialog(\'open\');\n\t\t\t\t\treturn false;\n\t\t\t\t});\n\n\t\t\t\t// Datepicker\n\t\t\t\t$(\'#datepicker\').datepicker({\n\t\t\t\t\tinline: true\n\t\t\t\t});\n\t\t\t\t\n\t\t\t\t// Slider\n\t\t\t\t$(\'#slider\').slider({\n\t\t\t\t\trange: true,\n\t\t\t\t\tvalues: [17, 67]\n\t\t\t\t});\n\t\t\t\t\n\t\t\t\t// Progressbar\n\t\t\t\t$("#progressbar").progressbar({\n\t\t\t\t\tvalue: 20 \n\t\t\t\t});\n\t\t\t\t\n\t\t\t\t//hover states on the static widgets\n\t\t\t\t$(\'#dialog_link, ul#icons li\').hover(\n\t\t\t\t\tfunction() { $(this).addClass(\'ui-state-hover\'); }, \n\t\t\t\t\tfunction() { $(this).removeClass(\'ui-state-hover\'); }\n\t\t\t\t);\n\t\t\t\t\n\t\t\t});\n\t\t</script>\n\t\t<style type="text/css">\n\t\t\t/*demo page css*/\n\t\t\tbody{ font: 62.5% "Trebuchet MS", sans-serif; margin: 50px;}\n\t\t\t.demoHeaders { margin-top: 2em; }\n\t\t\t#dialog_link {padding: .4em 1em .4em 20px;text-decoration: none;position: relative;}\n\t\t\t#dialog_link span.ui-icon {margin: 0 5px 0 0;position: absolute;left: .2em;top: 50%;margin-top: -8px;}\n\t\t\tul#icons {margin: 0; padding: 0;}\n\t\t\tul#icons li {margin: 2px; position: relative; padding: 4px 0; cursor: pointer; float: left;  list-style: none;}\n\t\t\tul#icons span.ui-icon {float: left; margin: 0 4px;}\n\t\t</style>\t\n\t</head>\n\n\n\n\t<body>\n\n    ')
        # SOURCE LINE 79
        __M_writer(escape(next.body()))
        __M_writer(u'\n  </body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


