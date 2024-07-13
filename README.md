# Markov Chain Text Generation
Welcome to the Markov Chain Text Generation project! This repository contains a Python implementation of a text generation algorithm using Markov chains. The aim of this project is to build a statistical model that can predict the probability of a character or word based on the preceding ones, allowing us to generate new text that mimics the style of the input text.

## Introduction
Markov chains are mathematical systems that undergo transitions from one state to another based on certain probabilistic rules. They are named after the Russian mathematician Andrey Markov. In the context of text generation, Markov chains can be used to model the probability of a character or word following a given sequence of characters or words. By analyzing a large corpus of text, we can create a model that captures these probabilities and use it to generate new, coherent text sequences.

This project demonstrates how to build and use Markov chain models at both the character and word levels. The key steps involved are:

1. Text Cleaning: Preprocessing the input text by removing punctuation and extra spaces.
2. Model Building: Constructing the Markov chain models based on the cleaned text.
3. Text Generation: Using the models to generate new text sequences.
4. Probability Analysis: Printing the probabilities of next characters and words to understand the model's behavior.

## Features
* Character-Level Model: Generates text by predicting the next character based on a sequence of preceding characters.
* Word-Level Model: Generates text by predicting the next word based on a sequence of preceding words.
* Configurable Order: Allows setting the order of the Markov chain, which determines the length of the context used for predictions.
* Text Cleaning: Includes functionality to clean and preprocess the input text.

## Installation
To get started with this project, ensure you have Python 3 installed.  
Clone the repository and navigate to the project directory:  
1. ```
   git clone https://github.com/yourusername/markov-chain-text-generation.git
   ```  
2. ```
   cd markov-chain-text-generation
   ```
## Usage  
1. Prepare Input Text  
Place your input text in a file named input.txt in the project directory. This file will be used to build the Markov chain models.

2. Run the Script  
Execute the script to build the models and generate text:  
```
python markov_chain.py
```  
4. Example Output  
The script will clean the input text, build the Markov chain models, and print the probabilities of the next characters and words. It will also generate and display sample text at both character and word levels.
## Contributing
Contributions to improve this project are welcome! If you'd like to contribute:

- Fork the repository.
- Create a new branch with a descriptive name (`git checkout -b my-branch-name`).
- Make your changes and commit them (`git commit -am 'Add some feature'`).
- Push to the branch (`git push origin my-branch-name`).
- Create a new Pull Request.
  


