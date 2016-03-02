PsiHook Heroku
===============

PsiHook Heroku is a simple [PsiHook](https://github.com/sibson/psihook) plugin that can be used to intergrate with [Heroku Deployhooks](https://devcenter.heroku.com/articles/deploy-hooks#http-post-hook) .

Quick start
-----------

1. Add "psihook_heroku" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'psihook_heroku',
    ]

2. Include the heroku URLconf in your project urls.py like this::

    url(r'^heroku/', include('psihook_heroku.urls')),

3. Add your hook to Heroku

    heroku addons:create deployhooks:http --url=https://exmaple.com/heroku
