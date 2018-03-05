from hashtag_collection import raw_data
import sys



def main():
    username = sys.argv[1]
    beginning = sys.argv[2]
    end = sys.argv[3]

    with open('followers_of_person/' + username + '_followers.txt') as f:
        content = f.readlines()

    followers = [x.strip() for x in content]
    for user in followers[int(beginning):int(end)]:
        raw_data(user)

if __name__ == "__main__":
    main()
