from hashtag_collection import raw_data


with open('followers_of_person/@Emma4Change_followers.txt') as f:
    content = f.readlines()

emma_folowers = [x.strip() for x in content]
print('Emma4Change: ' + str(len(content)))

with open('followers_of_person/@DLoesch_followers.txt') as f:
    content = f.readlines()

loesch_followers = [x.strip() for x in content]
print('@DLoesch: ' + str(len(content)))


for user in emma_folowers[:5]:
    raw_data(user)
