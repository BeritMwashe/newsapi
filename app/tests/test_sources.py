# # from .models.sources import Sources
# from app.models.sources import Sources
from app.models import Sources

import unittest






class Test_Source(unittest.TestCase):
    ''''Define setup method'''
    def setUp(self):
       self.new_article=Sources(
            "abc-news",
            "ABC News",
            "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
            "https://abcnews.go.com",
            "en",
            "us")
        

    def test_instance(self):
        '''When the app starts test if its inititalized properly'''
        self.assertTrue(isinstance(self.new_article,Sources))








