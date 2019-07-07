from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Eric Patrick', cpf='12345678901',
                    email='ericpatrick15@gmail.com', phone='62-99685-1234')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_form(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'ericpatrick15@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Eric Patrick',
            '12345678901',
            'ericpatrick15@gmail.com',
            '62-99685-1234',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)