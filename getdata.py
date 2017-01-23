import praw
import config
import datetime
from collections import defaultdict
from urllib.parse import urlparse
from common_words import word_list

reddit = praw.Reddit(user_agent=config.user_agent,
                     client_id=config.client_id,
                     client_secret=config.client_secret)

subreddit = reddit.subreddit('politics')

url_dict = defaultdict(int)
title_dict = defaultdict(int)

year = 2017
month = 1
day = 19
hour = 0
minute = 0


while day <= 21:

    print("Getting Submissions on " + str(month) + "/" + str(day) + "/" + str(year))

    start_timestamp = datetime.datetime(year, month, day, hour, minute).timestamp()
    end_timestamp = datetime.datetime(year, month, day, hour + 23, minute + 59).timestamp()

    for submission in subreddit.submissions(start=start_timestamp, end=end_timestamp):
        submission_url = urlparse(submission.url).hostname
        url_dict[submission_url] += 1
        for word in submission.title.split():
            if word not in word_list:
                title_dict[word] += 1

    day += 1

for k, v in sorted(url_dict.items()):
    print(k + ',' + str(v))

for k, v in sorted(title_dict.items()):
    print(k + ',' + str(v))
