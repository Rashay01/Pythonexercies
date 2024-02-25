from math import pi
from datetime import datetime

now = datetime.now()
print(now)
print(f"The current date is: {now:%d-%m-%Y}")
print(f"The current date is: {now:%d/%m/%Y}")
print(f"The current date is: {now:%d/%b/%Y}")

salary = 420_000_000

#numbers
print(f"Your salary is R{salary}")  #DX
print(f"Your salary is R{salary:,}")
print(f"Your salary is R{salary:_}")

#float formatting
print(f"Pi value is {round(pi)}")
print(f"Pi value is {pi:.2f}")
print(f"Pi value is {pi:.3f}")

#Text formatig
name = "Lilita"
person = "Quinlan"
print(f"{name:>20}:")
print(f"{name:<20}:")
print(f"{name:^20}:")

print(f"{person:*>20}:")
print(f"{person:#<20}:")
print(f"{person:$^20}:")

caleb = 0.925
print(f"The test results are out and caleb got {caleb:.2%}")

ans = """
The current date is: 14-03-2024
hi   
  
"""

print(ans)
