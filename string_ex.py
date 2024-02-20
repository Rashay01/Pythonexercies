message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

#strat
key = "🔑"

index = message.find(key)

output = message[index+1:].upper() if index >= 0 else "No secrect is preset"

if(output == code):
  print("You are an hacker")

else:
  print("try again")

#===================================================================================
#Task2

message = "    🚨🔍📱secret_code✌️"
code = "SECRET_CODE✌️"
error_nokey = "No, secrect is preset"

#strat
key = "🔑"

index = message.find(key)

output = message[index+1:].upper() if index != -1 else print("No, secrect is preset")

if(output == code):
  print("You are an hacker")
else:
  print("try again")

#===================================================================================
#Task3

message = "    🚨🔍📱🔑((((****secret_code✌️(((((*****"
code = "SECRET_CODE✌️"
error_nokey = "No, secrect is preset"

#strat
key = "🔑"

index = message.find(key)

output = message[index+1:].upper() if index != -1 else print("No, secrect is preset")

output = str(output).strip("(")
output = str(output).strip("*")

if(output == code):
  print("You are an hacker")
else:
  print("try again")