import unittest
import model_ex
class TestModelEx(unittest.TestCase):

    def test_predict_stock_news(self):
        str = 'Kickers on my watchlist XIDE TIT SOQ PNK CPW BPZ AJ  trade method 1 or method 2, see prev posts'
        modelEx = model_ex.ModelEx()
        self.assertEqual(modelEx.predict_stock_with_news(str),("postive") )

if __name__ == '__main__':
    unittest.main()