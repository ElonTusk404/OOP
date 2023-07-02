class User:
    users_id = []

    def __init__(self, username) -> None:
        self.id = len(User.users_id) + 1
        self.username = username
        self.tweets = []
        User.users_id.append(self.id)
    
    def new_tweet(self, text):
        tweet = Tweet(text)
        self.tweets.append(tweet)

    def get_tweets(self):
        return self.tweets

class Tweet:

    def __init__(self, text) -> None:
        self.text = text
        self.likes = 0
user1 = User('Mike')
user2 = User('Ann')
print(user1.id)
print(user2.id)
user1.new_tweet('Привет это Майки')
user1.new_tweet('Как тут интересно')
user2.new_tweet('Добрый день меня зовут Анна')
user2.new_tweet('Как тут играть в Танки?')
tweets_user1 = user1.get_tweets()
tweets_user2 = user2.get_tweets()

for tweet in tweets_user1:
    print(tweet.text)
for tweet in tweets_user2:
    print(tweet.text)






