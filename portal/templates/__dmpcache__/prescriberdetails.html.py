# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554864319.972693
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/prescriberdetails.html'
_template_uri = 'prescriberdetails.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'left_content', 'site_content', 'right_content']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        fullname = context.get('fullname', UNDEFINED)
        state = context.get('state', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        specialty = context.get('specialty', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        gender = context.get('gender', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fullname = context.get('fullname', UNDEFINED)
        state = context.get('state', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        def site_content():
            return render_site_content(context)
        specialty = context.get('specialty', UNDEFINED)
        gender = context.get('gender', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n   <div class="content">\r\n      <table class="detstab">\r\n         <tr>\r\n            <td>\r\n                  <img src="/static/homepage/media/UserImages/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(gender))
        __M_writer('.png">\r\n            </td>\r\n            <td class="bio">\r\n                  <p class="name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(fullname))
        __M_writer('<span class="info" style="margin-left:40px; font-weight:100;">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(gender))
        __M_writer('</span></p>\r\n                  <p class="spec">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(specialty))
        __M_writer(' <span style="margin-left:40px; font-weight:100; font-weight: bold;">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(state))
        __M_writer('</span></p>\r\n                  <p class="info"><span class="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('red' if sellsOpiod else ''))
        __M_writer('">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Opiate Prescriber' if sellsOpiod else 'Non-Opiate Prescriber' ))
        __M_writer('</span></p>\r\n                  \r\n            </td>\r\n            <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n            <td style="vertical-align:middle; padding-left:40px;">\r\n               <p class="stat" style="font-size:60px;line-height: 30px;">\r\n                  567,600\r\n               </p>\r\n               <p style="font-size:20px;">\r\n                  deaths in ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(state))
        __M_writer('\r\n               </p>\r\n            </td>\r\n         </tr>\r\n      </table>\r\n      <table class="detstab" style="border-top-style:solid;border-color:rgb(189, 189, 189);border-width:1px;">\r\n         <tr>\r\n')
        if sellsOpiod:
            __M_writer('            <td class="botinfo">\r\n                 <p class="head">Opiates Prescribed</p>\r\n                 <p>Druggedy Drug</p>\r\n                 <p>Druggedy Drug</p>\r\n                 <p>Druggedy Drug</p>\r\n                 <p>Druggedy Drug</p>\r\n                 <p>Druggedy Drug</p>\r\n                 <p>Druggedy Drug</p>\r\n            </td>\r\n')
        else:
            __M_writer('            <td class="botinfo">\r\n                  <p class="head">Opiate-Related Rx</p>\r\n                  <p>Druggedy Drug</p>\r\n                  <p>Druggedy Drug</p>\r\n                  <p>Druggedy Drug</p>\r\n                  <p class="red" style="font-size:50px;">At Risk</p>\r\n             </td>\r\n')
        __M_writer('            <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n            <td class="botinfo">\r\n                  <p class="head">Similar Prescribers</p>\r\n                  <a href="/portal/details/1/" class="link2" ><p>Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" style="font-family:trebuchet MS"><p>Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" style="font-family:trebuchet MS"><p>Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" style="font-family:trebuchet MS"><p>Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" style="font-family:trebuchet MS"><p>Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" style="font-family:trebuchet MS"><p>Other Dude</p></a>\r\n\r\n            </td>\r\n         </tr>\r\n      </table>\r\n            \r\n         \r\n         \r\n   </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/intexsite/portal/templates/prescriberdetails.html", "uri": "prescriberdetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "48": 1, "53": 3, "58": 7, "63": 71, "73": 3, "79": 3, "85": 5, "91": 5, "97": 9, "109": 9, "110": 14, "111": 14, "112": 17, "113": 17, "114": 17, "115": 17, "116": 18, "117": 18, "118": 18, "119": 18, "120": 19, "121": 19, "122": 19, "123": 19, "124": 28, "125": 28, "126": 35, "127": 36, "128": 45, "129": 46, "130": 54, "136": 73, "142": 73, "148": 142}}
__M_END_METADATA
"""
