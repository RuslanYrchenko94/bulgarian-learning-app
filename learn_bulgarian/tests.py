# from django.test import TestCase
# from django.urls import reverse
# from .models import Word
#
# class WordTests(TestCase):
#     def setUp(self):
#         Word.objects.create(bulgarian="здравей", translation="привіт")
#
#     def test_word_creation(self):
#         word = Word.objects.get(bulgarian="здравей")
#         self.assertEqual(word.translation, "привіт")
#
#     def test_dictionary_view(self):
#         response = self.client.get(reverse('learn_bulgarian:dictionary'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "здравей")
#
# # Create your tests here.
