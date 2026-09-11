import unittest
from p5_Fowler_Alejandra import caesar_cipher, caesar_decipher, letter_frequency



class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("Hello, FAU!", 3), "Khoor, IDX!")

    def test_caesar_decipher(self):
        self.assertEqual(caesar_decipher("Khoor, IDX!", 3), "Hello, FAU!")

    def test_letter_frequency(self):
        self.assertEqual(letter_frequency("Hello, FAU!"), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'f': 1, 'a': 1, 'u': 1})

class TestCaesarDecipher(unittest.TestCase):
    def test_caesar_decipher(self):
        self.assertEqual(caesar_decipher("Khoor, IDX!", 3), "Hello, FAU!")

class TestLetterFrequency(unittest.TestCase):
    def test_letter_frequency(self):
        self.assertEqual(letter_frequency("Hello, FAU!"), {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'f': 1, 'a': 1, 'u': 1})


if __name__ == '__main__':
    unittest.main()