import re
# Regex -> Regular Expression

# Pattern match in a string
#Credit card 16 digits 
# 38795475, 4985048584, 098305843, 987077540545, 987077540545

# They have 16 digits
# start  with 4

numbers ="""
  38795475, 4985048584, 098305843, 987077540545, 987077540545
"""

#\d\d\d matches 3 digits between 0-9
quote = "To be or not to be"
# r - raw 

is_be = re.search(r'be$',quote)
output = "Present and ends with 'be'" if is_be else "Not present"
print(output)

quote1 = "funny fun funnny fuzzy"
find_be = re.findall(r'fu[nz]{2}y',quote1)
print(find_be)
# 1. Search
# 2. findAll
# 3. sub 

#if you dot use r then when use \ you will have to escape it 

text = "This \\ that \\ those"
#raw string -> no need for escaping (i.e no \)
matches = re.findall('\\\\',text) 
#vs
matches_r = re.findall(r'\\',text)
print(matches)
print(matches_r)


tweet = "Spoiler: This movie is great, but the spoiler was unexpectes. Avoid sharing spoilers"

# ******

censor_text = re.sub(r'(spoiler|but)',"*"*7, tweet, flags=re.IGNORECASE)
print(censor_text)

list_websites = "facebook.com, google.com, twitter.in, amazon.com"
result = re.sub(r'(\w+)\.com',"blacklist.com", list_websites)
result1 = re.sub(r'(\w+)(\.com)',r'\1.net', list_websites)
print(result1)

#Task 1
names2 = ["John Doe", "Jane Smith", "Alice Johnson", "Chris Evans"]

output2 = [re.sub(r'(\w+)\s(\w+)',r'\2, \1', name) for name in names2]
print(output2)

names1 = ["John   Doe  ", "Jane    Smith", "Alice    Johnson", "  Chris  Evans  "]
output1 = [re.sub(r'(\w+)\s+(\w+)',r'\2, \1', name.strip()) for name in names1]
print(output1)


names = ["John   Doe  ", "Jane    Smith", "Alice    Johnson", "  Chris  Evans  "]
output = [re.sub(r'\s*(\w+)\s+(\w+)\s*',r'\2, \1', name) for name in names]
print(output)


# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"

hashtags = re.findall(r'#\w+', post)
print(hashtags)

# Output
#['#sunny', '#California', '#travel', '#fun']