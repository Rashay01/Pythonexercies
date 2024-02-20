msg = "Hi, all"
print(msg.upper())
print(msg.lower())
print(msg.capitalize())

msg1 = "              hi      hi   "
print(msg1.strip())

msg2 = "--------hi      hi-----------"
print(msg2.strip("-"))
print(msg2.lstrip("-"))
print(msg2.rstrip("-"))

msg3 = "hi, all bye all"
print(msg3.find("all")) #index of first match 
