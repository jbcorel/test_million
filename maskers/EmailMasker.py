from Masker import Masker
import unittest

   
class EmailMasker(Masker):
    
    def __init__(self, symbol: str = 'x') -> None:
        super().__init__(symbol)
    
    def mask(self, inp: str) -> str:
        name, domain = inp.split('@')
        name = self.symbol * len(name)
        return name + '@' + domain


class TestEmailMasker(unittest.TestCase):
    def setUp(self):
        self.masker = EmailMasker()

    def test_mask_email_basic(self):
        self.assertEqual(self.masker.mask("aaa@aaa.com"), "xxx@aaa.com")

    def test_mask_email_multiple_characters(self):
        self.masker = EmailMasker("x")
        self.assertEqual(self.masker.mask("aaaa@aaa.com"), "xxxx@aaa.com")

    def test_mask_email_with_custom_symbol(self):
        self.masker = EmailMasker("*")
        self.assertEqual(self.masker.mask("user123@domain.com"), "*******@domain.com")


if __name__ == '__main__':
    unittest.main()