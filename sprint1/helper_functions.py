import random 
import pandas as pd
adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
def random_phrase():
    adjectives = random.choice(adjectives)
    nouns = random.choice(nouns)
    return adjectives, nouns

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def random_bowling_score():
    return random.randint(0, 300)

def silly_tuple():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    star_rating = round(random.uniform(1, 5), 1)
    bowling_score = random.randint(0, 300)    
    return (f"{adjective} {noun}", star_rating, bowling_score)

def silly_tuple_list(num_tuples):
    def silly_tuple():
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        star_rating = round(random.uniform(1, 5), 1)
        bowling_score = random.randint(0, 300)
        return (f"{adjective} {noun}", star_rating, bowling_score)
    return [silly_tuple() for _ in range(num_tuples)]

def null_count(df):
    return df.isnull.sum()

