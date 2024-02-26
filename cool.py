
#Utility functions
def to_upper_case(text):
  """
  This is a method will uppercase all the characters."""
  return text.upper()

def to_lower_case(text):
  return text.lower()

help(to_upper_case)

# dunder variables -> __variable__
if __name__ == "__main__":
  print(__name__, type(__name__))
  print(to_upper_case("Quinlan"))
