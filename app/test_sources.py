# # from .models.sources import Sources
# from app.models.sources import Sources
from models import sources

import unittest
Source=sources.Sources
# from .sources import Source
class Test_Source(unittest.TestCase):
    '''tests if source is working fine'''
    def setUp(self):
        '''Runs before any test'''
        self.new_source=Source(
            "abc-news",
            "ABC News",
            "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
            "https://abcnews.go.com",
            "en",
            "us")

    def test__init__(self):
        '''asstets if values equals'''
        self.assertEqual(self.new_source.id,"abc-news")
        self.assertEqual(self.new_source.name,"ABC-news")
        self.assertEqual(self.new_source.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        self.assertEqual(self.new_source.url,"https://abcnews.go.com")



if __name__=='__main__':
    unittest.main()