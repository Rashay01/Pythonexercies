from functools import partial

# A normal function
def h(a, b, c, x):
    return 1000*a + 100*b + 10*c + x

# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(h, 3, 1, 4)

# Calling g()
print(g(5))


# Demonstrate Currying of composition of function 
def currying( g , f ):
  def h(x):
      return g(f(x))
  return h


def rand_to_dollar(ammount):  
  return ammount*0.052  

def usd_to_pound(ammount):   
  return ammount * 0.76


Convert = currying(rand_to_dollar,usd_to_pound )
print(Convert(565))