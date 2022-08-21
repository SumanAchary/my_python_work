"""Suffix Tree is very useful in numerous string processing and computational biology problems. Many books and
e-resources talk about it theoretically and in few places, code implementation is discussed. But still,
I felt something is missing and it’s not easy to implement code to construct suffix tree and it’s usage in many
applications. This is an attempt to bridge the gap between theory and complete working code implementation. Here we
will discuss Ukkonen’s Suffix Tree Construction Algorithm. We will discuss it in step by step detailed way and in
multiple parts from theory to implementation. We will start with brute force way and try to understand different
concepts, tricks involved in Ukkonen’s algorithm and in the last part, code implementation will be discussed. """
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


