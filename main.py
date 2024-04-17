import re 
 
email = input("what's ur email? ").strip()
# re.search - searching substring in the string
# re.match - searching  substring in the string from the beggingin  
# re.fullmatch - comparing 2 string
if re.search(r"^(\w+\.)*\w+@(\w+\.)*\w+\.(edu|com)$", email, re.IGNORECASE):
  print("valid")
else:
  print("invalid")