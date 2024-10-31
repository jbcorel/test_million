from Masker import Masker
import unittest
import re


class SkypeMasker(Masker):
    def __init__(self, symbol: str = 'x') -> None:
        super().__init__(symbol)
        self._pattern_href = r'(skype:)[^?]+(((\?call|chat|voicemail|add)?)">)'
        self._pattern_str = r'(skype:)[^?]+(\?call|chat|voicemail|add)?'
        self._replace = fr'\1{self.symbol*3}\2' 
    
    def mask(self, inp: str) -> str:
        if 'href' in inp:
            return re.sub(self._pattern_href, self._replace, inp)
        else:
            return re.sub(self._pattern_str, self._replace, inp)
            
    

class TestSkypeMasker(unittest.TestCase):
    def setUp(self):
        self.masker = SkypeMasker()

    def test_mask_skype_string(self):
        self.assertEqual(self.masker.mask("skype:alex.max"), "skype:xxx")

    def test_mask_skype_link(self):
        self.assertEqual(self.masker.mask('<a href="skype:alex.max?call">skype</a>'), '<a href="skype:xxx?call">skype</a>')

    def test_mask_skype_link_without_action(self):
        self.assertEqual(self.masker.mask('<a href="skype:alex.max">skype</a>'), '<a href="skype:xxx">skype</a>')
    
    def test_mask_skype_string_with_query(self):
        self.masker = SkypeMasker()
        self.assertEqual(self.masker.mask("skype:alex.max?call"), "skype:xxx?call")
    
    def test_mask_skype_link_with_custom_symbol(self):
        self.masker = SkypeMasker(symbol='$')
        self.assertEqual(self.masker.mask('<a href="skype:alex.max">skype</a>'), '<a href="skype:$$$">skype</a>')
    
    def test_mask_skype_string_with_custom_symbol(self):
        self.masker = SkypeMasker(symbol='$')
        self.assertEqual(self.masker.mask("skype:alex.max"), "skype:$$$")



if __name__ == "__main__":
    unittest.main()
    
    