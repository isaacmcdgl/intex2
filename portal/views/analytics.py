from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    if request.user.has_perm('account.analytics'):
        return request.dmp.render('analytics.html')
    else:
        return request.dmp.render('error.html')