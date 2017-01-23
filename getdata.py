import praw
import config
import datetime
from collections import defaultdict
from urllib.parse import urlparse
from common_words import word_list

reddit = praw.Reddit(user_agent=config.user_agent,
                     client_id=config.client_id,
                     client_secret=config.client_secret)

subreddit = reddit.subreddit('politics')  # Defining subreddit

url_dict = defaultdict(int)  # Creating dictionary for URL counter
title_dict = defaultdict(int)  # Creating dictionary for words in title

# Setting start date
year = 2017
month = 1
day = 19
hour = 0
minute = 0


while day <= 21:  # Setting end date

    print("Getting Submissions on " + str(month) + "/" + str(day) + "/" + str(year))

    start_timestamp = datetime.datetime(year, month, day, hour, minute).timestamp()
    end_timestamp = datetime.datetime(year, month, day, hour + 23, minute + 59).timestamp()
    # Generating UNIX timestamps for beginning and end of day in UTC

    for submission in subreddit.submissions(start=start_timestamp, end=end_timestamp):  # Gets submissions for whole day
        submission_url = urlparse(submission.url).hostname  # Parsing out "www.example.com"
        url_dict[submission_url] += 1  # Counting URL in dictionary
        for word in submission.title.split():  # Breaking title into individual words
            if word not in word_list:  # If it's not a common word
                title_dict[word] += 1  # Counting word in dictionary

    day += 1  # Moving onto the next day to repeat the loop

# Can be reconfigured to write to text file instead
for k, v in sorted(url_dict.items()):
    print(k + ',' + str(v))

for k, v in sorted(title_dict.items()):
    print(k + ',' + str(v))
