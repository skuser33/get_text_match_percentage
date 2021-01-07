###################################################
###Author: Satish Basetty  
###Date: 01/07/2021
###
### Compare Word Texts (API Call)
### Flask API call takes two Parameters as strings and compares these two text strings and returns the percentage match in 0 through 1 scale 
###
###################################################
import json
from flask import request
from flask import Flask, url_for
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/compare_texts')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/compare_texts_test',methods = ['POST'])
def api_article_test():
    if request.method == 'POST':
        sname = request.form.get('name')
        print(sname)
        return sname 
@app.route('/compare_texts',methods = ['POST'])
def api_article():
    if request.method == 'POST':
        src1 = sname = request.form.get('text1') 
        src2 = sname = request.form.get('text2') 

        #with open ('src/' + src1) as f:
        #    s = f.readline()
        lst1 = (src1.replace('.','')).split(' ')

        #with open ('src/' + src2) as f:
        #    s = f.readline()
        lst2 = ((src2.replace('.','').replace('\n','')).split(' '))
        wordDict1 = {}
        wordDict2 = {}


        for k in lst1:
            wordDict1[k] = wordDict1.get(k,0) + 1
        srtWordDict1 = sorted(wordDict1.items(), key = lambda x: x[1], reverse = True)


        for k in lst2:
            wordDict2[k] = wordDict2.get(k,0) + 1
        srtWordDict2 = sorted(wordDict2.items(), key = lambda x: x[1], reverse = True)
        strCompare = compare_word_text(srtWordDict1,srtWordDict2)
        return strCompare


##########################
### Function takes two text strigs as arguments and compares these and returns the match percentage 
### #This function currently suppresses "." punctuation this function can be enhanced to apply logic to supress the other puctuations
### Example: the word "good." is interpreted as "good" 
##########################


def compare_word_text(srtWordDict1,srtWordDict2):
    chkKey = 0
    chkValueCount = 0


    for k,v in srtWordDict1:
        for k1,v1 in srtWordDict2:
            if (k == k1):
                chkKey += 1
                chkValueCount += v + v1
    chekLargeFile = 1
    #print(str(chkKey) + " " + str(chkValueCount))
    if (len(srtWordDict1) > len(srtWordDict2)):
        assignWt = len(srtWordDict1)
    else:
        chekLargeFile = 2
        assignWt = len(srtWordDict2)


    j = 11
    wtDict1 = {}
    sRecsText1= sorted(srtWordDict1)
    for k,v in sorted(srtWordDict1):
         wtDict1[k] = j
         j += 1


    wtDict2 = {}
    j = 11
    sRecsText2= sorted(srtWordDict2)
    for k,v in sorted(srtWordDict2):
         wtDict2[k] = j
         j += 1  

    wordCountDict1 = {}
    for k,v in sRecsText1:
        wordCountDict1[k]= v 
    wordCountDict2 = {}
    for k,v in sRecsText2:
        wordCountDict2[k]= v
    matchCountfile1 = 0
    matchCountfile2 = 0
    matchCount2 = 0
    matchCount1 = 0
    keymatchCount = 0
    totaykeyCount = 0
    if chekLargeFile == 2:
        print(wordCountDict2)
        totaykeyCount = len(srtWordDict2)
        for k1,v1 in sorted(srtWordDict2):
            #print(srtWordDict1.get(k1,0))
            if k1 in wordCountDict1:
                print("Key wt cnt " + str(wtDict2[k1]))
                print("iCount " +  str(wordCountDict2[k1]))
                matchCount2 += wtDict2[k1] * wordCountDict2[k1]
                matchCount1 += wtDict1[k1] * wordCountDict1[k1]
                keymatchCount += 1
    else:
        totaykeyCount = len(srtWordDict1)
        for k1,v1 in sorted(srtWordDict1):
            #print(srtWordDict1.get(k1,0))
            if k1 in wordCountDict2:
                print("Key wt cnt " + str(wtDict1[k1]))
                print("iCount " +  str(wordCountDict1[k1]))
                matchCount2 += wtDict2[k1] * wordCountDict2[k1]
                matchCount1 += wtDict1[k1] * wordCountDict1[k1]
                keymatchCount += 1
    print("Total matchWt for TEXT2 is " + str(matchCount2))
    print("Total matchWt for TEXT1 is " + str(matchCount1))
    try:
        if matchCount2 == 0 | matchCount1 == 0:
            percetage_wt = 0.00  
        else:
            if matchCount2 > matchCount1:
                percetage_wt = (matchCount1 / matchCount2) * (keymatchCount/totaykeyCount) 
            else:
                percetage_wt = (matchCount2 / matchCount1) * (keymatchCount/totaykeyCount) 
    except Exception as err:
        print(err) 
    print(percetage_wt)
    result = ("{:.2f}".format(percetage_wt))
    #print("{:.2f}".format(percetage_wt))
    print(result)
    return result

if __name__ == '__main__':
    app.run()
