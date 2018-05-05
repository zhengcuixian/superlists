from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
import re

# Create your tests here.
#class SmokeTest(TestCase):
#	def test_bad_maths(self):
#		self.assertEqual(1+1,3)

class HomePageTest(TestCase):
	@staticmethod
	def remove_csrf(html_code):
		csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
		return re.sub(csrf_regex, '', html_code)
	
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
		
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))
		
	def test_home_page_returns_correct_html2(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html', request = request)
		self.assertEqual(self.remove_csrf(response.content.decode()), self.remove_csrf(expected_html))
		
	def test_home_page_can_save_a_post_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'
		
		response = home_page(request)
		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_item_text': 'A new list item'}
		)
		self.assertEqual(self.remove_csrf(response.content.decode()), self.remove_csrf(expected_html))
		
	
		
		
		
		