import unittest
from models import article
Article = article.Article
class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article=Article('P. H. Madore','Crypto Market Round-Up: Another Bitcoin Break Near $4000 or Are The Bulls Rushing the Gate?','Bitcoin is over $3900 globally, though many exchanges still have it trading closer to $3850. Ethereum’s broken beyond $140, might take $150 before the day is through. Bitcoin Cash is right behind it. It’s green everywhere you look. Even Bitcoin SV is on the r…','https://www.ccn.com/crypto-market-round-up-another-bitcoin-break-near-4000-or-are-the-bulls-rushing-the-gate','https://www.ccn.com/wp-content/uploads/2019/02/Crowd-chart-Shutterstock.jpg','2019-02-18T23:35:55Z','Bitcoin is over $3900 globally, though many exchanges still have it trading closer to $3850. Ethereums broken beyond $140, might take $150 before the day is through. Bitcoin Cash is right behind it. Its green everywhere you look. Even Bitcoin SV is on the reb… [+3568 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()