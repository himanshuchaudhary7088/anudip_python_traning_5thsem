'''Problem Statement 
A student enters: 
Rahul Sharma 
Tasks 
Generate a username using the rules: 
1. Remove spaces.  
2. Convert to lowercase.  
3. Append current year (2026).  
4. If username length exceeds 12, keep only first 12 characters.  
5. Count vowels in the generated username.  
6. Count consonants.  
7. Display username statistics.'''
# -------------------------------------------------------
# Username Generator System
# -------------------------------------------------------

name = "Rahul Sharma"

# Display original name
print("Original Name :", name)

# -------------------------------------------------------
# 1. Remove spaces
# -------------------------------------------------------

username = ""

for ch in name:
    if ch != " ":
        username += ch

# -------------------------------------------------------
# 2. Convert to lowercase
# -------------------------------------------------------

username = username.lower()

# -------------------------------------------------------
# 3. Append current year
# -------------------------------------------------------

username = username + "2026"

# Store actual generated username before truncation
generated_username = username

# -------------------------------------------------------
# 4. If username length exceeds 12,
#    keep only first 12 characters
# -------------------------------------------------------

if len(username) > 12:
    username = username[:12]

# -------------------------------------------------------
# 5 & 6. Count vowels and consonants
# -------------------------------------------------------

vowel_count = 0
consonant_count = 0

for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

# -------------------------------------------------------
# Display Results
# -------------------------------------------------------

print("\nGenerated Username :", generated_username)

print("\nFinal Username :", username)

print("\nUsername Length :", len(username))

print("\nVowels :", vowel_count)
print("Consonants :", consonant_count)

print("\nStatus : Username Generated Successfully")