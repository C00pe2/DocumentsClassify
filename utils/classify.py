import os

from rules_classify.rules.packing_list import PackingList
from rules_classify.rules.credit import Credit
from rules_classify.rules.insurance import Insurance
from rules_classify.rules.invoice import Invoice 
from rules_classify.rules.bill_of_lading import BillOfLading

class RulesClassify:
    def __init__(self) -> None:
        self.packing_list = PackingList()
        self.credit = Credit()
        self.insurance = Insurance()
        self.invoice = Invoice()
        self.bill_of_lading = BillOfLading()
    def classify(self, text):
        if self.packing_list.classify(text):
            return '箱单'
        elif self.credit.classify(text):
            return '信用证'
        elif self.insurance.classify(text):
            return '保险单'
        elif self.invoice.classify(text):
            return '发票'
        elif self.bill_of_lading.classify(text):
            return '提单'
        else:
            return '未知'
