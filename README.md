# Twitter-Boot

This program interacts with the Twitter API using the Tweepy library. It searches for tweets containing a specified keyword and likes a specified number of them. It also includes commented-out code that follows back a specific user. The program demonstrates how to authenticate with the Twitter API and interact with the API using Tweepy.

## Requirements

- Python 3.x
- Tweepy library

## Installation

1. Clone the repository:

git clone https://github.com/bautiallende/Twitter-Boot.git
cd twitter-boot


2. Create a virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Replace the placeholder values for the authentication keys and access tokens in the TweeterBoot.py file with your actual Twitter API keys and access tokens.

## Usage
Run the TweeterBoot.py script:
```bash
python TweeterBoot.py
```
After running the script, it will search for tweets containing the specified keyword and like the specified number of tweets. The console will display a message when a tweet is liked.

## Files
TweeterBoot.py: The main script that interacts with the Twitter API using the Tweepy library.
