import math
from collections import defaultdict, Counter


class NGramModel:
    def __init__(self, n, alpha=0.1):
        self.n = n
        self.alpha = alpha
        
        self.vocab = set()
        self.vocab_size = 0
        
        self.ngram_counts = defaultdict(int)
        self.context_counts = defaultdict(int)

    def build_vocab(self, data):
        counts = Counter()
        for method in data:
            for token in method:
                counts[token] += 1
        
        self.vocab = set(counts.keys())
        self.vocab.add("<UNK>")
        self.vocab_size = len(self.vocab)

    def replace_oov(self, tokens):
        return [t if t in self.vocab else "<UNK>" for t in tokens]

    def train(self, data):
        for method in data:
            tokens = self.replace_oov(method)
            tokens = ["<s>"] * (self.n - 1) + tokens

            for i in range(self.n - 1, len(tokens)):
                context = tuple(tokens[i - self.n + 1:i])
                token = tokens[i]

                self.ngram_counts[(context, token)] += 1
                self.context_counts[context] += 1

    def get_prob(self, context, token):
        context_count = self.context_counts.get(context, 0)
        ngram_count = self.ngram_counts.get((context, token), 0)

        num = ngram_count + self.alpha
        denom = context_count + self.alpha * self.vocab_size

        return num / denom

    def perplexity(self, data):
        total_log = 0.0
        total_tokens = 0

        for method in data:
            tokens = self.replace_oov(method)
            tokens = ["<s>"] * (self.n - 1) + tokens

            for i in range(self.n - 1, len(tokens)):
                context = tuple(tokens[i - self.n + 1:i])
                token = tokens[i]

                prob = self.get_prob(context, token)
                total_log += math.log(prob)
                total_tokens += 1

        return math.exp(-total_log / total_tokens)

    def predict(self, context):
        best_token = None
        best_prob = 0

        for token in self.vocab:
            prob = self.get_prob(context, token)
            if prob > best_prob:
                best_prob = prob
                best_token = token

        return best_token, best_prob
