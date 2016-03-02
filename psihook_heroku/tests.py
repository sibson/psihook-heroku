from __future__ import absolute_import

from unittest import TestCase
from django.test import RequestFactory
from mock import patch

from . import views, signals


class HerokuHookTestCase(TestCase):
    def setUp(self):
        super(HerokuHookTestCase, self).setUp()
        self.factory = RequestFactory()

    @patch('psihook_heroku.signals.psihook_heroku.send_robust')
    def test_sends_signal(self, signal):
        params = {
            'app': 'testapp',
            'user': 'testuser@example.com',
            'url': 'https://testapp.example.com',
            'head': '12345',
            'head_long': '1234567890abcdef',
            'git_log': 'test changes',
            'release': '11',
        }
        req = self.factory.post('/heroku/webhook', params)

        resp = views.heroku(req)
        self.assertEqual(resp.status_code, 200)

        signal.assert_called_once_with(signals.HerokuSender, path='/heroku/webhook', **params)
