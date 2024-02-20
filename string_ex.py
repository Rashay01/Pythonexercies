message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

#strat
key = "🔑"

index = message.find(key)

output = message[index+1:].upper() if index >= 0 else "No secrect is preset"

#print(output)
if(output == code):
  print("You are an hacker")

else:
  print("try again")

#===================================================================================
#Task2

message = "    🚨🔍📱secret_code✌️"
code = "SECRET_CODE✌️"
error_nokey = "No secrect is preset"

#strat
key = "🔑"

index = message.find(key)

output = message[index+1:].upper() if index >= 0 else "No secrect is preset"

#print(output)
if(output == code):
  print("You are an hacker")
elif (output == error_nokey):
  print(output)
else:
  print("try again")
