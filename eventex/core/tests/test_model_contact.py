from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
	def setUp(self):
		self.speaker = Speaker.objects.create(
			name='Henrique Bastos',
			slug='henrique-bastos',
			photo='http://hbn.link/hb-pic'
		)

	def test_email(self):
		contact = Contact.objects.create(speaker=self.speaker, kind='E',
										 value='henrique@bastos.net')

		self.assertTrue(Contact.objects.exists())

	def test_phone(self):
		contact = Contact.objects.create(speaker=self.speaker, kind='P',
										 value='21-996186180')

		self.assertTrue(Contact.objects.exists())