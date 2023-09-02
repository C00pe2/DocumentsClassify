import os

#信用证类
class Credit:
    def __init__(self) -> None:
        self.keywords_ls = self.build_keywords()
    def build_keywords(self):
        keywords_ls = []
        with open('rules_classify/rules_txt_file/credit.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                keywords_ls.append(line.strip())
        return keywords_ls
    def classify(self, text):
        for keyword in self.keywords_ls:
            if keyword in text:
                return True
        return False