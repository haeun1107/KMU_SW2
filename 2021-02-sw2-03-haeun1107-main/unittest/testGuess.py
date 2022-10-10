import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #중복
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #숫자
        self.g1.guess('1')
        self.assertEqual(self.g1.displayGuessed(), ' 1 a e n t u ')
        #특수문자
        self.g1.guess('?')
        self.assertEqual(self.g1.displayGuessed(), ' 1 ? a e n t u ')

    def testGuess(self):
        self.assertTrue(self.g1.guess('a'))
        self.assertFalse(self.g1.guess('b'))
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        #중복
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        #대문자
        self.g1.guess('A')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        #숫자
        self.g1.guess('1')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        #특수문자
        self.g1.guess('?')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        #두글자이상
        self.g1.guess('ab')
        self.assertEqual(self.g1.currentStatus, '_e_a___')

    def testFinished(self):
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertTrue(self.g1.finished())


if __name__ == '__main__':
    unittest.main()

