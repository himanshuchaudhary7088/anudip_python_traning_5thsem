""" -----------------------------------------
5. Product Review Analyzer 
Problem Statement 
A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1. Count total words.  
2. Create a dictionary containing word frequencies.  
3. Find the most frequently used word.  
5. Count words having more than 5 characters.  
6. Display words in reverse order.  
7. Create a list of unique words.
-----------------------------------------  """

# -------------------------------------------------------
# Product Review Analyzer
# -------------------------------------------------------

review = "This product is excellent excellent excellent and very useful"

# -------------------------------------------------------
# Convert review into list of words
# -------------------------------------------------------

words = review.split()

# -------------------------------------------------------
# 1. Count total words
# -------------------------------------------------------

total_words = len(words)

print("Total Words :", total_words)

# -------------------------------------------------------
# 2. Create dictionary of word frequencies
# -------------------------------------------------------

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies :", frequency)

# -------------------------------------------------------
# 3. Find most frequently used word
# -------------------------------------------------------

most_frequent_word = ""
highest_count = 0

for word in frequency:

    if frequency[word] > highest_count:
        highest_count = frequency[word]
        most_frequent_word = word

print("\nMost Frequent Word :", most_frequent_word)
print("Frequency :", highest_count)

# -------------------------------------------------------
# 4. Find words appearing only once
# -------------------------------------------------------

single_words = []

for word in frequency:

    if frequency[word] == 1:
        single_words.append(word)

print("\nWords Appearing Once :", single_words)

# -------------------------------------------------------
# 5. Count words having more than 5 characters
# -------------------------------------------------------

count_more_than_5 = 0

for word in words:

    if len(word) > 5:
        count_more_than_5 += 1

print("\nWords Having More Than 5 Characters :", count_more_than_5)

# -------------------------------------------------------
# 6. Display words in reverse order
# -------------------------------------------------------

print("\nWords In Reverse Order :")

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

# -------------------------------------------------------
# 7. Create list of unique words
# -------------------------------------------------------

unique_words = []

for word in words:

    if word not in unique_words:
        unique_words.append(word)

print("\n\nUnique Words :", unique_words)