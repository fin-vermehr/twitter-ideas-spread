import os
import pandas as pd
import numpy as np
from semantic_clustering_metadata import algorithm_one
hashtag_set = set()
for filename in os.listdir('tweets_of_person/DLoesch'):
    if filename == '.DS_Store':
        pass
    else:
        df = pd.read_csv('tweets_of_person/DLoesch/' + filename)
        hashtags = df['Hashtags']
        for hashtag in hashtags:
            print hashtag
            if type(hashtag) == str and hashtag is not None:
                if '[' in hashtag:
                    hashtag = hashtag.replace('[', '').replace(']', '').replace("'", "").split(',')
                    for i in hashtag:
                        hashtag_set.add(i)
                else:
                    hashtag_set.add(hashtag)
                    print(hashtag)

hashtag_list = list(hashtag_set)[30:35]
a = algorithm_one(hashtag_list)

print a
print np.amax(a)

# text_file = open("hashtag_set_Emma4Change.txt", "w")
# text_file.write(str(hashtag_set))
# text_file.close()
