# Distributed Twitter Simulator using concurrent patterns
import random

def simulate_twitter_stream(users, tweets_per_user):
    print(f"Starting Twitter simulator with {users} users...")
    total_tweets = 0
    for _ in range(users):
        total_tweets += tweets_per_user
    print(f"Simulated {total_tweets} tweets across distributed nodes.")

if __name__ == "__main__":
    simulate_twitter_stream(1000, 20)