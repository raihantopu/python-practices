import re

url = input("enter URL: ").strip()

username = re.sub(r"^(https?://)(www\.)?twitter\.com/", "", url)

print(f"username: {username}")

name = input("enter your name: ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches: 
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")