from django.urls import reverse, resolve


class TestURLs:

    def test_word_list_page_url(self):
        path = reverse('list')
        assert resolve(path).view_name == 'list'

    def test_check_word_form_url(self):
        path = reverse('check')
        assert resolve(path).view_name == 'check'