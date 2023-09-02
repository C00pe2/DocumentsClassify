import os

#发票类
class Invoice:
    def __init__(self) -> None:
        self.keywords_ls = self.build_keywords()
    def build_keywords(self):
        keywords_ls = []
        with open(os.path.join(os.path.dirname(__file__), 'rules_txt_file/invoice.txt'), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                keywords_ls.append(line.strip())
        return keywords_ls
    def classify(self, text):
        for keyword in self.keywords_ls:
            if keyword in text:
                return True
        return False