from shared_tweeters_cluster import shared_tweeters
from shared_tweeters_cluster import assign_number

# emma4chang

population1_dict = dict()
control_dict = dict()

population1 = ['Emma4Change', 'GunOwners', 'DLoesch']
control = []

for user in population1:
    hashtag_dict = shared_tweeters(user)
    number_dict = assign_number(hashtag_dict)

    for key in number_dict:
        if key not in population1_dict:
            population1_dict[key] = number_dict[key]
        else:
            population1_dict[key] += number_dict[key]

    print 'Complete: ' + user


biggest = None

for key in population1_dict:
    if population1_dict[key] >= biggest or population1_dict[key] >= (biggest) or biggest is None or population1_dict[key]por > 0.04:
        biggest = population1_dict[key]
        print biggest
        print key
