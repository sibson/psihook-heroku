import django.dispatch


class HerokuSender(object):
    """ A placeholder for sender in signals """


psihook_heroku = django.dispatch.Signal(
    providing_args=['path', 'app', 'user', 'url', 'head', 'head_long', 'git_log', 'release'])
