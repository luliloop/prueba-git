#CodingBat Warmup 2
#exercise 1
"""Given a string and a non-negative int n,return a larger string that is
n copies of the original string."""
def string_times(str, n):
  if n<=0:
    return ""
  new_string=str*n
  return new_string
result = string_times("christchurch",0)
print(result)


