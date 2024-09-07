import unittest
from functions import isAInt, isValidChoice, isValidName, isValidPosition, isValidInputNumber

class unittestFunctions(unittest.TestCase):
    def test_isAInt(self):
        self.assertFalse(isAInt("twelve"))
        self.assertFalse(isAInt("Josh"))
        self.assertFalse(isAInt("Guard"))
        self.assertTrue(isAInt("27"))
        self.assertTrue(isAInt("1"))
        self.assertTrue(isAInt("0"))
        self.assertFalse(isAInt("34%"))
        self.assertFalse(isAInt("3.14"))
        self.assertFalse(isAInt(""))
    def test_isValidChoice(self):
        self.assertFalse(isValidChoice(""))
        self.assertFalse(isValidChoice("0"))
        self.assertFalse(isValidChoice("7"))
        self.assertTrue(isValidChoice("1"))
        self.assertTrue(isValidChoice("2"))
        self.assertTrue(isValidChoice("3"))
        self.assertTrue(isValidChoice("4"))
        self.assertTrue(isValidChoice("5"))
        self.assertTrue(isValidChoice("6"))
    def test_isValidName(self):
        self.assertFalse(isValidName(""))
        self.assertTrue(isValidName("Jay Kim"))
        self.assertTrue(isValidName("kimj196"))
        self.assertTrue(isValidName("K"))
        self.assertTrue(isValidName("qwerqwerqwerqwerqwerqwerqwerqw"))
        self.assertFalse(isValidName("qwerqwerqwerqwerqwerqwerqwerqwe"))
    def test_isValidPosition(self):
        self.assertTrue(isValidPosition("Guard"))
        self.assertTrue(isValidPosition("Forward"))
        self.assertTrue(isValidPosition("Centre"))
        self.assertFalse(isValidPosition(""))
        self.assertFalse(isValidPosition("G"))
        self.assertFalse(isValidPosition("F"))
        self.assertFalse(isValidPosition("C"))
        self.assertFalse(isValidPosition("123"))
        self.assertFalse(isValidPosition("John"))
    def test_isValidInputNumber(self):
        self.assertTrue(isValidInputNumber(5, 1, 10))
        self.assertFalse(isValidInputNumber(1, 5, 10))
        self.assertTrue(isValidInputNumber(0, 0, 200))
        self.assertTrue(isValidInputNumber(1, 0, 200))
        self.assertTrue(isValidInputNumber(137, 0, 200))
        self.assertTrue(isValidInputNumber(200, 0, 200))
        self.assertFalse(isValidInputNumber(201, 0, 200))
        self.assertTrue(isValidInputNumber(0, 0, 2000))
        self.assertTrue(isValidInputNumber(1, 0, 2000))
        self.assertTrue(isValidInputNumber(41, 0, 2000))
        self.assertTrue(isValidInputNumber(729, 0, 2000))
        self.assertTrue(isValidInputNumber(2000, 0, 2000))
        self.assertFalse(isValidInputNumber(2001, 0, 2000))
        self.assertFalse(isValidInputNumber(2024, 0, 2000))

if __name__ == '__main__':
    unittest.main()