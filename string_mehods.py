msg = "Hi, all"
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())

msg1 = "              hi      hi   "
print(msg1.strip())

msg2 = "--------hi      hi-----------"
print(msg2.strip("-"))
print(msg2.lstrip("-"))
print(msg2.rstrip("-"))

msg3 = "hi, all bye all"
print(msg3.find("all")) #index of first match 

print(msg3.replace("all", "everyone"))
print(msg3.count("all"))
print(msg3.endswith("all"))
print(msg3.startswith("hi"))

bage_no = "454545"

print(bage_no.isdigit())

print(len(bage_no))