# your code goes here!

class Anagram:
    def __init__(self, word):
        # Store the sorted lowercase letters of the word
        self.word = sorted(word.lower())
        print(f"Anagram instance created with word: {word}")

    def match(self, words):
        matches = []  # A list to store words that are anagrams

        # Check each word in the list
        for candidate in words:
            # Check if the sorted lowercase letters of the candidate match the stored word
            if sorted(candidate.lower()) == self.word:
                matches.append(candidate)  # Add the matching word to the list
                print(f"Found a match: {candidate}")

        return matches  # Return the list of matching words
    
    # Create an instance of Anagram
ana = Anagram("listen")

# Test the match method
matches = ana.match(["silent", "hello", "world"])

# Print the result
print("Matching words:", matches)


