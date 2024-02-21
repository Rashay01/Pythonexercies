# i =0
# while i < 3:
#   print(i)
#   i+=1


# i=0
# rows = int(input("How many rows would you like? "))
# while i < rows:
#   i+=1
#   print("🤩"*(i))
  

#range(3) excluding 3
#range(1,3) starting 1 excluding 3
#range(0,10,2) starting at 0 excluding 10 with step 2
# for curr in range(1,50,2):
#   print(curr)


# rows = int(input("How many rows would you like? "))
# for i in range(1,rows+1):
#   print("🤩"*(i))

#================================================================
#task
# player_stats = [10, 30, 60]

# power_up_stats = player_stats.copy()

# for i in range(len(power_up_stats)):
#   power_up_stats[i] = power_up_stats[i]*2

# print(f"Power up: {power_up_stats} player stats: {player_stats}")

#================================================================
# powered_up_stats = [stat*2 for stat in player_stats]
# print(powered_up_stats, player_stats)

#================================================================
# #task2

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]

char_count = [len(character) for character in avengers]

print(char_count)

#================================================================
# task3 all the names of all the avengers with 10 chars
char_over_10 =[]

for i in range(len(char_count)):
  if(char_count[i] > 10):
    char_over_10.append(avengers[i])

print(char_over_10)