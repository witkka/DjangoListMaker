from django.urls import reverse, resolve


class TestURLs:

    def test_new_url(self):
        path = reverse('new')
        assert resolve(path).view_name == 'new'