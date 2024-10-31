from Masker import Masker
import unittest

class NumberMasker(Masker):
    
    def __init__(self, symbol: str = 'x', digits: int = 3) -> None:
        super().__init__(symbol)
        self._digits = digits
    
    def mask(self, inp: str) -> str:
        parsed = inp.split()
        remaining_digits = self._digits
        
        for i in range(len(parsed) - 1, 0, -1):
            length_of_step = len(parsed[i])
            if remaining_digits > 0:
                if remaining_digits >= length_of_step:
                    parsed[i] = self.symbol * length_of_step
                else:
                    parsed[i] = parsed[i][:-(remaining_digits)] + self.symbol * remaining_digits   
                remaining_digits = remaining_digits - length_of_step
            else:
                break
                
        return ' '.join(parsed)
    


class TestNumberMasker(unittest.TestCase):
    def setUp(self):
        self.masker = NumberMasker()

    def test_mask_phone_basic(self):
        self.assertEqual(self.masker.mask("+7 666 777 888"), "+7 666 777 xxx")

    def test_mask_phone_with_multiple_spaces(self):
        self.assertEqual(self.masker.mask("+7 666 777       888"), "+7 666 777 xxx")

    def test_mask_phone_with_custom_symbol(self):
        self.masker = NumberMasker(symbol="*")
        self.assertEqual(self.masker.mask("+7 666 777 888"), "+7 666 777 ***")

    def test_mask_phone_custom_length(self):
        self.masker = NumberMasker(digits=5)
        self.assertEqual(self.masker.mask("+7 666 777 888"), "+7 666 7xx xxx")

if __name__ == '__main__':
    unittest.main()