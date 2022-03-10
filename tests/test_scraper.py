from django.urls import reverse, resolve


class TestURLs:

    def test_context_url(self):
        path = reverse('context')
        assert resolve(path).view_name == 'context'
