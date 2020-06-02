
from itertools import tee
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import string

wordRegex = re.compile(r"[\w']+")

# MR Class for word probability
class MRWordProbability(MRJob):
    
    # Define MRJob steps
    def steps(self):
        return [
            MRStep(mapper=self.read_csv),
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer_counts),
            MRStep(reducer=self.reducer_percents)
        ]
    
    # Return a line from the CSV
    def read_csv(self, _, line):
        if(line[0] != '"'):
            yield (None, line[line.find(","):].lower())
    
    # Regex the line to build bigrams from the words
    def mapper(self, _, line):
        prevWord = ""
        
        # Remove non-alpha characters
        for inv in (list(string.punctuation) + list(string.digits)):
            line = line.replace(inv, "")
        
        # Find words and build bigrams
        for word in wordRegex.findall(line):
            if(prevWord != ""):
                yield ((prevWord, word), 1)
            prevWord = word
    
    def combiner(self, word, counts):
        yield (word, sum(counts))
    
    def reducer_counts(self, word, counts):
        first, second = word
        yield first, (sum(counts), second)
    
    # Calculate percent likelyhood of a word following another
    def reducer_percents(self, word, pairs):
        # Dupicate the data so that we can sort one set
        pairs, pairs2 = tee(pairs)
        
        # Count each bigram for the given word
        total = 0
        for pair in pairs:
            pairCount, _ = pair
            total = total + pairCount
        
        # Sort bigrams by word usage
        probabilityList = sorted(pairs2, key=self.getUsage, reverse = True)
        
        # Calculate output
        numPairs = len(probabilityList) - 1
        for i in range(numPairs):
            word_count, word_key = probabilityList[i]
            percent = (word_count / total) * 100
            yield str(i+1), ((word, word_key), percent, word_count)
        
    # Return the number a times a word is used
    def getUsage(self, x):
        num, _ = x
        return num
        
if __name__ == '__main__':
    MRWordProbability.run()
