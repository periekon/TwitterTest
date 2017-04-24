import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = 'C:\\Users\\pc-fastcode101\\PycharmProjects\\TwitterTest\\twitJoziSA.js'
tweets = pd.DataFrame()
tweets_data = []

def initData():
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    print (len(tweets_data))

def plot2():
    tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
    lists = []

    lists.append([tweet for tweet in tweets['text'] if word_in_text('Johannesburg', tweet)])
    lists.append([tweet for tweet in tweets['text'] if word_in_text('Jozi', tweet)])
    lists.append([tweet for tweet in tweets['text'] if word_in_text('Joburg', tweet)])

    x_val = ['Johannesburg','Jozi','Joburg']
    y_val = [ len(lists[0]),  len(lists[1]),  len(lists[2])]

    x_pos = list(range(len(x_val)))
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, y_val, width, alpha=1, color='g')

    # Setting axis labels and ticks
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('xxx', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(x_val)
    plt.grid()


def plot1():
    tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
#   tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
    tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))

    tweets_by_country = tweets['country'].value_counts()
    """
    for c in tweets_by_country.index.tolist():
        print(c)
    """
    #tweets_by_country = pd.Series(data = dict([('a',10), ('b', 5), ('c',8), ('d',12), ('e',19)]))

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Countries', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

    plt.show()

#find words
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def main():
    initData()
    #plot1()
    plot2()
    plt.show()

if __name__ == '__main__':
    main()
