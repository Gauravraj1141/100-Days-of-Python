import requests
import pandas as pd
from collections import Counter
from heapq import heappush, heappop



# # Send an HTTP request to the link and store the response
# response = requests.get("https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset/download?datasetVersionNumber=1")
# print(response.content)

# we consider file from our dir
df = pd.read_csv("Resume.csv")

# Print the shape of the DataFrame (number of rows and columns)
print(df)



# get the column containing the resumes
resumes = df["Category"].tolist()

# create a list of all the words in the resumes
all_words = []
for resume in resumes:
    words = resume.split()
    all_words.extend(words)

# count the occurrences of each word and sort them in descending order
word_counts = Counter(all_words)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# print the sorted word counts
for word, count in sorted_word_counts:
    print(f"{word} : {count}")



# create an empty heap
heap = []

# add the word counts to the heap
for word, count in word_counts.items():
    heappush(heap, (-count, word))

# retrieve the top N words with the highest count
N = 10
top_words = []
for _ in range(N):
    count, word = heappop(heap)
    top_words.append((word, -count))

# print the top words
print(top_words)



# create a dictionary to store the word counts
word_count_dict = {}

# add the word counts to the dictionary
for word, count in word_counts.items():
    word_count_dict[word] = count

# retrieve the count for a given word
word = "skills"
count = word_count_dict.get(word, 0)
print(f"{word}: {count}")