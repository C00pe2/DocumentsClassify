import os

#提单类
class BillOfLading:
    def __init__(self) -> None:
        self.keywords_ls = self.build_keywords()
    def build_keywords(self):
        keywords_ls = []
        with open(os.path.join(os.path.dirname(__file__), 'rules_txt_file/bill_of_lading.txt'), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                keywords_ls.append(line.strip())
        return keywords_ls
    def classify(self, text):
        for keyword in self.keywords_ls:
            if keyword in text:
                return True
        return False