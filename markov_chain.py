import random
import string
from collections import defaultdict, Counter

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.char_model = defaultdict(Counter)
        self.word_model = defaultdict(Counter)

    def clean_text(self, text):
        """
        Clean the text by removing punctuation and extra spaces.
        """
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = ' '.join(text.split())  # Remove extra spaces
        return text

    def build_char_chain(self, text):
        """
        Build the Markov chain model at the character level from the given text.
        """
        for i in range(len(text) - self.order):
            current_state = text[i:i + self.order]
            next_state = text[i + self.order]
            self.char_model[current_state][next_state] += 1

    def build_word_chain(self, text):
        """
        Build the Markov chain model at the word level from the given text.
        """
        words = text.split()
        for i in range(len(words) - self.order):
            current_state = tuple(words[i:i + self.order])
            next_state = words[i + self.order]
            self.word_model[current_state][next_state] += 1

    def generate_char_text(self, length=100):
        """
        Generate text at the character level using the Markov chain model.
        Start with a random state and generate text of the given length.
        """
        current_state = random.choice(list(self.char_model.keys()))
        generated_text = current_state

        while len(generated_text) < length:
            if current_state in self.char_model:
                next_char = self._get_next_char(current_state)
                generated_text += next_char
                current_state = generated_text[-self.order:]
            else:
                break

        return generated_text

    def generate_word_text(self, length=100):
        """
        Generate text at the word level using the Markov chain model.
        Start with a random state and generate text of the given length.
        """
        current_state = random.choice(list(self.word_model.keys()))
        generated_text = ' '.join(current_state)

        while len(generated_text.split()) < length:
            if current_state in self.word_model:
                next_word = self._get_next_word(current_state)
                generated_text += ' ' + next_word
                current_state = tuple(generated_text.split()[-self.order:])
            else:
                break

        return generated_text

    def _get_next_char(self, current_state):
        """
        Helper function to get the next character based on probabilities.
        """
        transitions = self.char_model[current_state]
        total = sum(transitions.values())
        rand_num = random.randint(1, total)
        cumulative_prob = 0

        for char, count in transitions.items():
            cumulative_prob += count
            if rand_num <= cumulative_prob:
                return char

    def _get_next_word(self, current_state):
        """
        Helper function to get the next word based on probabilities.
        """
        transitions = self.word_model[current_state]
        total = sum(transitions.values())
        rand_num = random.randint(1, total)
        cumulative_prob = 0

        for word, count in transitions.items():
            cumulative_prob += count
            if rand_num <= cumulative_prob:
                return word

    def print_probabilities(self, num_words=10):
        """
        Print probabilities of next characters and a few words based on the previous ones.
        Limit to showing probabilities for a maximum of `num_words` words.
        """
        print("Character-level Model:")
        for state in sorted(self.char_model.keys()):
            print(f"{state}: {list(self.char_model[state].keys())}")

        print("\nWord-level Model:")
        count = 0
        for state in sorted(self.word_model.keys()):
            if len(state) == self.order:  # Print probabilities for states with the specified order
                print(f"{' '.join(state)}: {list(self.word_model[state].keys())}")
                count += 1
                if count >= num_words:
                    break

# Example usage
def main():
    # Read text from input file
    input_file = 'input.txt'
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Create Markov chain model
    markov_model = MarkovChain(order=2)  # Adjust the order for different levels of context
    cleaned_text = markov_model.clean_text(input_text)
    markov_model.build_char_chain(cleaned_text)
    markov_model.build_word_chain(cleaned_text)

    # Print probabilities of next characters and limited number of words
    markov_model.print_probabilities(num_words=10)

    # Generate text at character level
    generated_char_text = markov_model.generate_char_text(length=200)
    print("\nGenerated Character Level Text:")
    print(generated_char_text)

    # Generate text at word level
    generated_word_text = markov_model.generate_word_text(length=50)
    print("\nGenerated Word Level Text:")
    print(generated_word_text)

if __name__ == "__main__":
    main()



#Code Overview
#MarkovChain Class
#The MarkovChain class encapsulates the core functionality of the project. Here's a brief overview of its methods:

#__init__(self, order=1): Initializes the Markov chain model with the specified order (context length).
#clean_text(self, text): Cleans the input text by removing punctuation and extra spaces.
#build_char_chain(self, text): Builds the Markov chain model at the character level.
#build_word_chain(self, text): Builds the Markov chain model at the word level.
#generate_char_text(self, length=100): Generates text at the character level using the Markov chain model.
#generate_word_text(self, length=100): Generates text at the word level using the Markov chain model.
#_get_next_char(self, current_state): Helper function to get the next character based on probabilities.
#_get_next_word(self, current_state): Helper function to get the next word based on probabilities.
#print_probabilities(self, num_words=10): Prints probabilities of next characters and a few words based on the previous ones.)
