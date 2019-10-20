from django.test import TestCase
import twitter
from decouple import config


# Create your views here.

class tweeterTestCase(TestCase):
    def setUp(self):
        self.api = twitter.Api(consumer_key=config('consumer_key'), consumer_secret=config('consumer_secret'),
                               access_token_key=config('access_token_key'),
                               access_token_secret=config('access_token_secret'))
        self.str1 = "Test content"
        self.str2 = "test test"

    def test(self):
        a = self.api.PostUpdate(self.str1)
        b = self.api.PostUpdate(self.str2)
        self.assertEqual(self.api.GetStatus(a.id).text, self.str1)
        self.assertEqual(self.api.GetStatus(b.id).text, self.str2)
        self.api.DestroyStatus(a.id)
        self.api.DestroyStatus(b.id)
        for tweet in self.api.GetUserTimeline():
            self.assertNotEqual(a.id, tweet.id)
            self.assertNotEqual(b.id, tweet.id)