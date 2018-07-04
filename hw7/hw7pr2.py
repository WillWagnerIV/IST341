# Will Wagner
# IST341 - Python
# 3/29/2018
# hw3pr2.py 
#
# Person or machine?  The rps-string challenge...
#
# This file should include your code for 
#   + extract_features( rps ),               returning a dictionary of features from an input rps string
#   + score_features( dict_of_features ),    returning a score (or scores) based on that dictionary
#   + read_data( filename="rps.csv" ),       returning the list of datarows in rps.csv
#
# Be sure to include a short description of your algorithm in the triple-quoted string below.
# Also, be sure to include your final scores for each string in the rps.csv file you include,
#   either by writing a new file out or by pasting your results into the existing file
#   And, include your assessment as to whether each string was human-created or machine-created
# 
#

"""
Short description of (1) the features you compute for each rps-string and 
      (2) how you score those features and how those scores relate to "humanness" or "machineness"





"""

import random
import os
import os.path
import shutil
import csv
from collections import defaultdict


r_avg = 0
rp_avg = 0
rps_avg = 0

r_total = 0
rp_total = 0
rps_total = 0

human = False
human_count = 0



# Here's how to machine-generate an rps string.
# You can create your own human-generated ones!
def gen_rps_string( num_characters ):
    """ return a uniformly random rps string with num_characters characters """
    result = ''
    for i in range( num_characters ):
        result += random.choice( 'rps' )
    return result

# Two example machine-generated strings:
rps_machine1 = gen_rps_string(200)
rps_machine2 = gen_rps_string(200)

#
# extract_features( rps ):   extracts features from rps into a defaultdict
#
def extract_features( rps ):
    """ Started by testing with just simple r p s and added to dictionary d
    """

    print(rps)
    d = defaultdict( float )  # other features are reasonable
    
    num_r = rps.count('r')  # counts all of the 'r's in rps
    print('num r:',num_r)
    d['r'] = float(num_r/len(rps)*3)

    num_rp = rps.count('rp')  # counts all of the 'rp's in rps
    print('num rp:',num_rp)
    d['rp'] = float(num_rp/len(rps)*10)

    num_rps = rps.count('rps')  # counts all of the 'rps's in rps
    print('num rps:',num_rps)
    d['rps'] = float(num_rps/len(rps)*30)

    return d   # return our features



#
# score_features( dict_of_features ): returns a score based on those features
#
def score_features( dict_of_features ):
    """ <include a docstring here!>
    """
    d = dict_of_features
    # random_value = random.uniform(0,1)


    r_score = d['r']
    rp_score = d['rp']
    rps_score = d['rps']

    print('r_score = ',r_score)
    print('rp_score = ',rp_score)
    print('rps_score = ',rps_score)

    score = (r_score+rp_score+rps_score)/(len(d)*10)*10
    return r_score,rp_score,rps_score,score   # return a humanness or machineness score


#
# read_data( filename="rps.csv" ):   gets all of the data from "rps.csv"
#
def read_data( filename="rps.csv" ):
    """ <include a docstring here!>
    """
    # you'll want to look back at reading a csv file!
    List_of_rows = []   # for now...

    with open('./hw7/rps.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            #print(', '.join(row))
            List_of_rows += row


    return List_of_rows


def create_bot_tests():
    # Test 200x with random bot list
    
    r_total = 0
    rp_total = 0
    rps_total = 0

    avg = 0
    score = 0
    score_total = 0 
    for x in range(200):
        rps_machine1 = gen_rps_string(200)
        cnt_d = extract_features(rps_machine1)
        r_score,rp_score,rps_score,score = score_features(cnt_d)
        score_total += score
        r_total += cnt_d['r']
        rp_total += cnt_d['rp']
        rps_total += cnt_d['rps']

    r_avg = r_total / 200
    rp_avg = rp_total / 200
    rps_avg = rps_total / 200
    score_avg = score_total / 200

    # print('Average randomized scores',r_avg,rp_avg,rps_avg,"Score average:",score_avg)

    return r_avg,rp_avg,rps_avg,score_avg



#
# Start of Main Loop
#

# Create Bot test numbers
bot_r_avg,bot_rp_avg,bot_rps_avg,bot_score_avg = create_bot_tests()
print('Average Bot scores',bot_r_avg,bot_rp_avg,bot_rps_avg,"Bot Score average:",bot_score_avg)


# Test on cvs file

LoR = read_data()
#print(LoR)
#print("length = ",str(len(LoR)))
print()

for i in range(1,len(LoR),2):   

    dict_of_features = extract_features( LoR[i] )
    r_score,rp_score,rps_score,score = score_features( dict_of_features )
    print('scores = ',r_score,rp_score,rps_score,score)

    r_total += dict_of_features['r']
    rp_total += dict_of_features['rp']
    rps_total += dict_of_features['rps']


    if ((abs(r_score) - abs(bot_r_avg)) >=.85) or ((abs(rp_score) - abs(bot_rp_avg)) >=.85) or (abs(rps_score) - abs(bot_rps_avg) >= 1) :
        print(r_score,rp_score,rps_score)
        print(abs(r_score) - abs(bot_r_avg))
        print(abs(rp_score) - abs(bot_rp_avg))
        human = True 
        human_count += 1
        #d_humans['humans'] += i

    print(human, human_count)

    human = False

    print('\n\n')









#
# you'll use these three functions to score each rps string and then
#    determine if it was human-generated or machine-generated 
#    (they're half and half with one mystery string)
#
# Be sure to include your scores and your human/machine decision in the rps.csv file!
#    And include the file in your hw3.zip archive (with the other rows that are already there)
#









    # ifile = open(filename, 'rb')
    # reader = csv.reader(ifile)
        
    # rownum = 0
    # for row in reader:
    #     # Save header row.
    #     if rownum ==0:
    #         header = row
    #     else:
    #         colnum = 0
    #         for col in row:
    #             print('%-8s: %s %' (header[colnum], col))
    #             colnum += 1
    
    #     rownum += 1
        
    # ifile.close()