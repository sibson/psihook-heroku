from __future__ import absolute_import

from django.http import HttpResponse

from .signals import psihook_heroku, HerokuSender


def heroku(request):
    psihook_heroku.send_robust(HerokuSender, path=request.path, **dict(request.POST.iteritems()))

    return HttpResponse()
