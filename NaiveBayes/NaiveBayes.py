import math
import re
from collections import defaultdict 

class Bayes_Classifier:

    def __init__(self):
        self.positive_words, self.negative_words = defaultdict(int), defaultdict(int)
        self.total_positive_words, self.total_negative_words = 0, 0
        self.unique_words = set()
        self.num_unique_words = 0
        self.total_words = 0 


    def train(self, lines):
        for line in lines: 
            all = line.strip().split('|')
            label, text = all[0], all[2]
            words = text.split()
            words = [word.lower() for word in words]
            words = [re.sub(r'[^\w\s]', '', word) for word in words]
            unique_words_in_review = set(words)
            if label == '5': 
                for word in words: 
                    self.positive_words[word]+=1 
                    self.total_positive_words+=1 
            else: 
                for word in words: 
                    self.negative_words[word]+=1 
                    self.total_negative_words+=1 
            self.unique_words.update(unique_words_in_review)  
            self.num_unique_words = len(self.unique_words)
            self.total_words = self.total_positive_words + self.total_negative_words



    def classify(self, lines):
        predictions = []
        for line in lines: 
            all = line.strip().split('|')
            text = all[2]
            words = text.split()
            words = [re.sub(r'[^\w\s]', '', word.lower()) for word in words]
            log_total_pos_prob, log_total_neg_prob = math.log(self.total_positive_words / self.total_words), math.log(self.total_negative_words / self.total_words)
            for word in words: 
                log_total_pos_prob += math.log((self.positive_words[word]+1) / (self.total_positive_words + self.num_unique_words))
                log_total_neg_prob += math.log((self.negative_words[word]+1) / (self.total_negative_words + self.num_unique_words))
            predictions.append("5" if log_total_pos_prob > log_total_neg_prob else "1")
        return predictions 
                
