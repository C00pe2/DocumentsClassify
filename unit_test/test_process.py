#unit test for process CleanText
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rules_classify.utils.process import CleanText, TextCorrect


#unit test for process CleanText
class TestCleanText(unittest.TestCase):
    def setUp(self):
        self.clean_text = CleanText()
        self.text = '   你好，我是一个测试文本，我有很多的标点符号，我还有很多的数字，我还有很多的空格，我还有很多的大写字母，我还有很多的特殊符号，我还有很多的换行符号�'
        self.cleaned_text = '你好 我是一个测试文本 我有很多的标点符号 我还有很多的数字 我还有很多的空格 我还有很多的大写字母 我还有很多的特殊符号 我还有很多的换行符号'
        self.cleaned_text_special = '你好我是一个测试文本我有很多的标点符号我还有很多的数字我还有很多的空格我还有很多的大写字母我还有很多的特殊符号我还有很多的换行符号'
        self.cleaned_text_number = '你好 我是一个测试文本 我有很多的标点符号 我还有很多的数字 我还有很多的空格 我还有很多的大写字母 我还有很多的特殊符号 我还有很多的换行符号'
        self.cleaned_text_lower = '   你好，我是一个测试文本，我有很多的标点符号，我还有很多的数字，我还有很多的空格，我还有很多的大写字母，我还有很多的特殊符号，我还有很多的换行符号�'
    
    def test_clean_space(self):
        self.assertEqual(self.clean_text.clean_space(self.text), self.cleaned_text)
    
    def test_clean_special(self):
        self.assertEqual(self.clean_text.clean_special(self.text), self.cleaned_text_special)
    
    def test_clean_number(self):
        self.assertEqual(self.clean_text.clean_number(self.text), self.cleaned_text_number)
    
    def test_char_lower(self):
        self.assertEqual(self.clean_text.char_lower(self.text), self.cleaned_text_lower)

#unit test for process TextCorrect
class TestTextCorrect(unittest.TestCase):
    def setUp(self):
        self.text_correct = TextCorrect()
        self.text_ch = '我是一个测试文本，我有恨多的标点符号，我还有很多的数字，我还有很多的空格，我还有很多的大写字母，我还有很多的特殊符号，我还有很多的换行符号�'
        self.text_en = 'I am a test text, I hvae a lot of punctuation, I have a lot of numbers, I have a lot of spaces, I have a lot of capital letters, I have a lot of special symbols, I have a lot of line breaks'
        self.text_ch_corrected = '我是一个测试文本，我有很多的标点符号，我还有很多的数字，我还有很多的空格，我还有很多的大写字母，我还有很多的特殊符号，我还有很多的换行符号'
        self.text_en_corrected = 'I am a test text, I have a lot of punctuation, I have a lot of numbers, I have a lot of spaces, I have a lot of capital letters, I have a lot of special symbols, I have a lot of line breaks'
        self.text_ch_en = '我是一个测试文本，我有很多的彪点符号，我还有lots of nummmbber，我还有很多的space，我还有很多的大写字母，我还有很多的特殊符号，我还有很多的换行符号�'
        self.text_ch_en_corrected = '我是一个测试文本，我有很多的标点符号，我还有lots of number，我还有很多的space，我还有很多的大写字母，我还有很多的特殊符号，我还有很多的换行符号'
    def test_ch_or_en(self):
        self.assertEqual(self.text_correct.ch_or_en(self.text_ch), self.text_ch_corrected)
        self.assertEqual(self.text_correct.ch_or_en(self.text_en), self.text_en_corrected)
        self.assertEqual(self.text_correct.ch_or_en(self.text_ch_en_corrected), self.text_ch_en_corrected)
    
    def test_correct_ch(self):
        self.assertEqual(self.text_correct.correct_ch(self.text_ch), self.text_ch_corrected)
    
    def test_correct_en(self):
        self.assertEqual(self.text_correct.correct_en(self.text_en), self.text_en_corrected)


if __name__ == '__main__':
    unittest.main()
