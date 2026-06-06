#Cricket Tournament Scorecard
'''----------------------------------------------
Write a program to: 
• Count half-centuries and centuries.  
• Find the highest score.  
• Display all scores below 20.  
• Calculate the average score. 
---------------------------------------------------'''
# Batsman's Scores

scores = [45, 78, 12, 100, 67, 8, 90, 55]

# -----------------------------------------
# Count half-centuries and centuries

half_century = 0
century = 0

for score in scores:
    if score >= 100:
        century = century + 1
    elif score >= 50:
        half_century = half_century + 1

print("Half-centuries:", half_century)
print("Centuries:", century)

# -----------------------------------------
# Find the highest score

highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("Highest Score:", highest_score)

# -----------------------------------------
# Display all scores below 20

print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score)

# -----------------------------------------
# Calculate average score

total = 0

for score in scores:
    total = total + score

average = total / len(scores)

print("Average Score:", average)