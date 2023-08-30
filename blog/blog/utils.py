from .models import Post
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
from nltk.util import bigrams
nltk.download('vader_lexicon')
import os
import random 



def analyze_user_body(body):

    tokens = word_tokenize(body.lower())
    return [token for token in tokens if token.isalpha()]

def emotion_lexicon(word):

    emotions = {}

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'emotion.txt')
    with open(file_path, 'r') as file:
        for line in file:
            emotion, keywords = line.strip().split(':')
            emotions[emotion] = keywords.split(', ')

    for emotion, keywords in emotions.items():
        if word in keywords:
            return emotion

    return None 

def detect_emotions(text):
    preprocessed_text = analyze_user_body(text)

    emotions = []
    for token in preprocessed_text:
        emotion = emotion_lexicon(token)
        if emotion:
            emotions.append(emotion)

    return emotions


def randomize_texts(text):
    return random.choice(text)

def analyze_sentence_structure(body):
    
    pos_tag1 = [pos_tag(body) for word in body]

    return pos_tag1

def sentiment_analysis(text):
    
    emotions = {}

    sentiment_analyzer = SentimentIntensityAnalyzer()
    body = analyze_user_body(text)
    emotionstext = detect_emotions(text)


    positive_word = []
    negative_word = []
    positive = 0
    negative = 0


    for word in body:
        # Sentiment Analysis

        sentiment_score = sentiment_analyzer.polarity_scores(word)['compound']
        

        if sentiment_score >= 0.05:
            sentiment = 'Positive'
            positive_word.append(word)
            positive += 1 
            
        elif sentiment_score <= -0.05:
            sentiment = 'Negative'
            negative_word.append(word)
            negative += 1
        else:
            sentiment = 'Neutral'
        
        emotions[word] = sentiment

        total_sentiments = positive + negative
    if total_sentiments != 0:
        positive_ratio = positive / total_sentiments
        negative_ratio = negative / total_sentiments
    else:
        positive_ratio = 0
        negative_ratio = 0

    return positive_word, negative_word, positive_ratio, negative_ratio



def process_negative_text(negative):

    pos_list = analyze_sentence_structure(negative)

    text = ''
    count = 0

    for i in range(len(pos_list)):
        if count == 4:
            break
            
        if pos_list[0][i][1] == 'JJ':
            texts = [' You embrace negativity when you use words like ' + pos_list[0][i][0] + '. ',

            ' Question how your ' + pos_list[0][i][0] + ' lifestyle can be avoided. ',

            ' How does ' + pos_list[0][i][0] + ' feeling manifest in your life. What can you do to avoid this? ',

            'Remind yourself what ' + pos_list[0][i][0] + ' things means to you' 


            ]

            text += randomize_texts(texts)

            count += 1

        if pos_list[0][i][1] == 'NN':
            texts = [' It seems like you already know what ' + pos_list[0][i][0] + ' is. Find out how to avoid it.',

            'You seem to attach to your negative side based on your use of the word ' + pos_list[0][i][0] + '. ',

            'In order to love yourself, try understanding ' + pos_list[0][i][0] + '. Make habits to avoid it. '


            ]

            text += randomize_texts(texts)

            count += 1

        return text

def fafo(all):

    pos_list = analyze_sentence_structure(all)
    
    return pos_list, pos_list[0][0][0], pos_list[0][0][1]
        





def process_positive_text(positive):

    pos_list = analyze_sentence_structure(positive)
    positive_synonyms = get_synonyms_for_list(positive) 
    

    text = ''
    count = 0
    
    for i in range(len(pos_list)):
        if count == 4:
            break
            
        if pos_list[0][i][1] == 'JJ':
            texts = [' You embrace positivity when you describe how you are ' + pos_list[0][i][0] + '. ',

            'You seem to have an energetic personality based on your use of the word ' + pos_list[0][i][0] + '. ',

            'Take a moment to reflect on what being ' + pos_list[0][i][0] + ' offers for you. ',

            'Remind yourself what it is like to be ' + pos_list[0][i][0] + '.' 


            ]

            text += randomize_texts(texts)

            count += 1

        if pos_list[0][i][1] == 'NN':
            texts = [' It seems like you already know what ' + pos_list[0][i][0] + ' is. Find out how to achieve it.',

            'You seem to have an energetic personality based on your use of the word ' + pos_list[0][i][0] + '. ',

            'In order to achieve this feeling of ' + pos_list[0][i][0] + ' understand it to a greater degree. ',

            'Remind yourself what it is like to be ' + pos_list[0][i][0] + '. ' 


            ]


            text += randomize_texts(texts)

            count += 1
            
    return text

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def get_synonyms_for_list(words):
    synonyms_list = []
    for word in words:
        synonyms = get_synonyms(word)
        synonyms_list.append(synonyms)
    return synonyms_list

        



def sentiment_response(text):

    positive_word, negative_word, positive, negative = sentiment_analysis(text)
    
    final_response = ''
    positive_response = ' ' 
    negative_response = ' ' 
    positive_advice = [
        
        ' Your journal entry is ultimately an indication that you are healthy and happy. I appreciate your positivity and dedication to loving life. ',
        ' Given that your journal entry is very positive, my advice to you is to practice happiness even more through different forms. Whether it be gratitude or meditation, find more ways to expand your happiness. ',
        ' I am so joyous to read that you are mostly happy in your journal entry. Though you may encounter sad emotions, it seems like you DO do a good job of focusing on happy things '

    ]

    
    negative_advice = [

        ' Your journal entry is an indication you attach to negativity in your life. This isnt to say your feelings arent valid. However, your feelings are complex and require deeper thought. In the meantime, try to incorporate gratitude, meditation, and breathing into your daily routine to see some starting changes with your lifestlye ',
        ' I may be wrong but this is a solemn journal entry. You are sad. You are angry. And you may be feeling down. Ultimately, it comes down to habits first. Are you sleeping well? Are you eating well? Figure these things out and then write again. '

    ]

    negative_positive_advice = [

        ' This mix of emotions indicates that you may be confused how to feel. Its okay to feel confused. Emotions can be complex and multifaceted, and its normal to have mixed or unclear feelings at times. ',
        ' Sometimes, simply identifying and labeling your emotions can provide clarity. Write these emotions down in Journal Love and practice understanding them. ',
        ' Think about what you might need in this moment. Do you need some alone time, a supportive conversation, or a creative outlet? Addressing your needs can help you navigate your feelings.'

    ]

    

    positive_synonyms = get_synonyms_for_list(positive_word)
    negative_snyonyms = get_synonyms_for_list(negative_word)
    


    
    
    if positive >= .1:
        positive_response += ' You seem to be very positive in this journal entry.'
        positive_response += randomize_texts(positive_advice)

    if negative >= .1:
        negative_response += 'This journal entry signifies dissatisfaction.'
        negative_response += randomize_texts(negative_advice)

    if negative >= .5 and positive >= .5:
        negative_response += 'You are experiencing a mix of both positive and negative emotions.'
        negative_response += randomize_texts(negative_positive_advice)

    positive_text = process_positive_text(positive_word)
    if positive_text != None:
        positive_response += positive_text
    

    negative_text = process_negative_text(negative_word)
    if negative_text != None:
        negative_response += negative_text

    
    if not positive_response and not negative_response:
        final_response = "No specific sentiment detected."
    else:
        final_response = positive_response + negative_response

    return final_response





def response_text(emotions):

    happy = 0 
    sad = 0 

    for i in range(len(emotions)):
        if emotions[i] == 'happy':
            happy += 1
        if emotions[i] == 'sad':
            sad += 1

    text = ' '

    if (happy >= 1 and sad == 0):
        text += 'You are so happy!'
    elif (sad >= 1 and happy == 0):
        text += 'You are so sad!'
    elif happy > sad:
        text += 'Although you are sad, you seem to hold on to your joyous side'
    elif sad < happy:
        text += 'Although you are happy, you express strong disappointment'
    else:
        text += 'I am unable to make a judgement. I apologize.'

    return text 







    
    