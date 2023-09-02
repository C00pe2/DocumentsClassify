import os
import re
import pycorrector

class CleanText:
    def __init__(self) -> None:
        self.keywords_ls = self.build_keywords()
    def build_keywords(self):
        keywords_ls = []
        with open(os.path.join(os.path.dirname(__file__), 'rules_txt_file/clean_text.txt'), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                keywords_ls.append(line.strip())
        return keywords_ls
    
    def clean_space(self, text):
        cleaned_text = ' '.join(text.split())
        return cleaned_text
    
    def clean_special(self, text): 
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text

    def clean_number(self, text):
        cleaned_text = re.sub(r'[^A-Za-z\s]', '', text)
        return cleaned_text
    
    def char_lower(self, text):
        cleaned_text = text.lower()
        return cleaned_text 
        
#文本纠错
class TextCorrect:
    def __init__(self):
        pass
    def ch_or_en(self, text):
        #判断是中文
        if re.search(r'[\u4e00-\u9fa5]', text):
            return self.correct_ch(text)
        #还是英文
        elif re.search(r'[A-Za-z]', text):
            return self.correct_en(text)
        #还是中英混合
        else:
            return self.correct_ch(self.correct_en(text))
    #对中文进行文本纠错
    def correct_ch(self, text):
        corrected_text, _ = pycorrector.correct(text)
        return corrected_text
    #对英文进行文本纠错
    def correct_en(self, text):
        corrected_text, _ = pycorrector.en_correct(text)
        return corrected_text