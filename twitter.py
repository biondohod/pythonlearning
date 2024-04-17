import re 

url = input("URL: ").strip()

if matches := re.search(r"(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
  print(f"username:", matches.group(1))