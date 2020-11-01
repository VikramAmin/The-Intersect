# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 22:56:02 2020

@author: aminv
"""

import spacy
import pandas as pd

nlp = spacy.load('en_core_web_sm')

#test={"toptags":{"@attr":{"offset":0,"num_res":50,"total":2736558},"tag":[{"name":"rock","count":3983323,"reach":395866},{"name":"electronic","count":2375997,"reach":254451},{"name":"seen live","count":2142883,"reach":81755},{"name":"alternative","count":2096764,"reach":262074},{"name":"indie","count":2019297,"reach":253815},{"name":"pop","count":1978632,"reach":226174},{"name":"female vocalists","count":1600986,"reach":167900},{"name":"metal","count":1260640,"reach":155748},{"name":"alternative rock","count":1168243,"reach":166992},{"name":"jazz","count":1152540,"reach":146682},{"name":"classic rock","count":1139745,"reach":136660},{"name":"ambient","count":1057483,"reach":144501},{"name":"experimental","count":1054148,"reach":139524},{"name":"folk","count":919195,"reach":147694},{"name":"punk","count":884093,"reach":142178},{"name":"indie rock","count":877573,"reach":133605},{"name":"Hip-Hop","count":861685,"reach":126986},{"name":"hard rock","count":859377,"reach":113968},{"name":"instrumental","count":841716,"reach":123301},{"name":"black metal","count":838012,"reach":61736},{"name":"singer-songwriter","count":832047,"reach":108214},{"name":"dance","count":798505,"reach":132113},{"name":"80s","count":776806,"reach":99952},{"name":"Progressive rock","count":723646,"reach":95345},{"name":"death metal","count":714399,"reach":71028},{"name":"heavy metal","count":700757,"reach":89574},{"name":"hardcore","count":691126,"reach":97070},{"name":"british","count":684826,"reach":92717},{"name":"soul","count":671192,"reach":100007},{"name":"chillout","count":647307,"reach":103102},{"name":"electronica","count":630579,"reach":101472},{"name":"Classical","count":562021,"reach":73696},{"name":"rap","count":560940,"reach":103409},{"name":"industrial","count":558615,"reach":83143},{"name":"Soundtrack","count":557107,"reach":83784},{"name":"punk rock","count":546869,"reach":97007},{"name":"blues","count":544561,"reach":95206},{"name":"thrash metal","count":491732,"reach":61992},{"name":"90s","count":479852,"reach":56539},{"name":"acoustic","count":475122,"reach":110010},{"name":"metalcore","count":473987,"reach":66582},{"name":"psychedelic","count":471352,"reach":77300},{"name":"japanese","count":458830,"reach":48338},{"name":"post-rock","count":440513,"reach":64624},{"name":"Progressive metal","count":432718,"reach":61803},{"name":"german","count":431844,"reach":58996},{"name":"hip hop","count":425288,"reach":76589},{"name":"funk","count":422610,"reach":82157},{"name":"new wave","count":418038,"reach":63539},{"name":"trance","count":414495,"reach":64241}]}}


mood_list =['Warm', 'Peaceful', 'Dreamy', 'Soothing', 'Enchanting', 'Sentimental', 'Heartfelt', 'Heartwarming', 'Bouncy', 'Fun', 'Feel Good', 'Bright', 'Playful', 'Whimsical', 'Comical', 'Lively', 'Quirky', 'Heartache', 'Yearning', 'Longing', 'Pensive', 'Melancholy', 'Heartbroken', 'Grim', 'Ominous', 'Mysterious', 'Gloomy', 'Dark']
mood_list = [nlp(mood) for mood in mood_list]

def tokenize_top_tags(tags):
    tokens = []
    for tag in tags:
        tokens += [[nlp(tag[0]), int(tag[1])]]
    return tokens
        
def token_dist(token1, token2):
    return token1.similarity(token2)


tokens = tokenize_top_tags(test)



distances = []
for token in tokens:
    for mood in mood_list:
        distances+=[[token[0].text, mood.text, token_dist(token[0], mood), token[1]]]
        
distances = pd.DataFrame(distances,columns=['tag','mood','dist', 'weight'])
mood_classes=distances.groupby('mood', as_index=False).mean()
distances['weigted_dist']=distances.dist*distances.weight
weigted_mood_classes=distances[['tag','mood','weigted_dist']].groupby('mood', as_index=False).mean()
