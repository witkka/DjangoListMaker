from django.urls import reverse, resolve


class TestURLs:

    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'
