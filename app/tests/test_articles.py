import unittest
from app.models import Articles





class Test_Article(unittest.TestCase):
    ''''Define setup method'''
    def setUp(self):
       self.new_article=Articles(
            {},
            "Jonathan Howcroft",
            "Bledisloe Cup 2021: New Zealand All Blacks v Australia Wallabies – live - The Guardian",
            "Minute-by-minute report: The Bledisloe Cup kicks off at Eden Park where the Wallabies have not won since 1986. Join Jonathan Howcroft for updates",
            "https://www.theguardian.com/sport/live/2021/aug/07/bledisloe-cup-2021-live-all-blacks-vs-australia-rugby-new-zealand-v-wallabies-union-test-match-updates-team-schedule-watch-eden-park-auckland",
            "https://i.guim.co.uk/img/media/a2a267c5e6b0d036ffb7130dfbed5ba6e1beaeb0/0_106_3888_2333/master/3888.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctbGl2ZS5wbmc&enable=upscale&s=52a8685196da5bd593ce9cbc92df0b99",
            "2021-08-07T08:30:51Z",
            "9.47am BST09:47 Full-time: New Zealand 33-25 Australia Bledisloe I to the All Blacks at Eden Park. 9.47am BST09:47 TRY! New Zealand 33-25 Australia (Uelese 80+3) 9.45am BST09:45 80+2 mins: Aust… [+11295 chars]"
                )
        

    def test_instance(self):
        '''When the app starts test if its inititalized properly'''
        self.assertTrue(isinstance(self.new_article,Articles))




