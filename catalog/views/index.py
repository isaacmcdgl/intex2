from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod

@view_function
def process_request(request, category:cmod.Category=None, page:int=1):
    context = {
       
    }
    return request.dmp.render('index.html', context)