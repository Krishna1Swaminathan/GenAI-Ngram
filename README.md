This project implements n-gram models to predict the next token in Java methods. It uses method-level code extracted from the Google Guava repository and evaluates models using perplexity. The goal is to provide probabilistic code completion for Java methods using n-gram statistics.

The project includes:

Training and validation on extracted Java methods.

Evaluation on both a professor-provided test set and a self-created test set.

Output predictions in JSON format with token context, predicted token, predicted probability, and ground truth token.


GenAI
 ngram_model.py  # N-gram model implementation
 train.py # Training, validation, testing, and prediction generation
 clean_methods.py # Extracts and cleans method-level Java code
 split_dataset.py # Splits cleaned methods into training, validation, and self-test sets
 data/
    train.txt # Training data
    val.txt # Validation data
    test.txt # Professor-provided test set
 predictions_test.json # Predictions on professor test set
 predictions_self_test.json # Predictions on self-created test set
 README.md # This file

Dependancies

pandas
requests
numpy

To run the project in order

python clean_methods.py
python split_dataset.py
python train.py


What this will do is:
Extract the method level code
Clean them by removing duplicates, non-ASCII characters, and methods with less than 10 tokens
Spilt them into T1, T2, T3, val and test
It will them train the 3-gram, 5-gram, and 7-gram models on the training sets
Compute the validation perplexity for each size
Selects the best model and then generates the predictions on the prof test set and my own test set

After running train.py the outputs will be predictions_test.json which has the predictions for the professor test set and predictions_self_test.json as the results for the test I created

For every method the JSON has:
Context which shows the preceding tokens
predToken - which is the token predicted my the model
predProbability - probability of the predicted token
groundTruth - the actual token from the test set
perplexity - the overall perplexity for the data set

The hyperparameters:
n-gram sizes tested: 3, 5, 7
Smoothing I used Add-α smoothing with α = 0.1
Padding I used <s> tokens at the start of each method
OOV tokens were replaced with <UNK>


Overview

The 3-gram model performed best across validation sets and was used for final evaluation
The professor test set had a lot higher perplexity than the test I created. 
JSON was structured so it would be easy to read and go through



Training 3-gram model on T1
Validation Perplexity (T1, n=3): 167.34165074699644
Training 5-gram model on T1
Validation Perplexity (T1, n=5): 984.4556975600761
Training 7-gram model on T1
Validation Perplexity (T1, n=7): 2547.648797499736
Training 3-gram model on T2
Validation Perplexity (T2, n=3): 187.38464188361172
Training 5-gram model on T2
Validation Perplexity (T2, n=5): 1144.175276203456
Training 7-gram model on T2
Validation Perplexity (T2, n=7): 3028.5762092251325
Training 3-gram model on T3
Validation Perplexity (T3, n=3): 187.38464188361172
Training 5-gram model on T3
Validation Perplexity (T3, n=5): 1144.175276203456
Training 7-gram model on T3
Validation Perplexity (T3, n=7): 3028.5762092251325



Validation Perplexity (n=3): 15.349659348496818
Validation Perplexity (n=5): 15.380650527624233
Validation Perplexity (n=7): 15.382551518659808


Validation Perplexity: 167.34165074699644
Professor Test Perplexity: 3438.0598822850197
Self Test Perplexity: 171.75280942171617