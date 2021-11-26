# coding:utf-8

class Qta:
    def __init__(self,number,sentence):
        self.sentence = sentence
        self.number = number
    #出題を行う
    def info (self):
        print(str(self.number)+"問目、"+self.sentence)
    
 #計算時の逆転項目（５ー自分の点数）   
class Qtotal:
    def get_score(number,score):
        rev = ["2q","5q","6q","11q","12q","14q","16q","17q","18q","20q"]
        for x in rev:
            if x == number:
                s = 5- score
                return s
        return score
    
        
        
