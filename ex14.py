from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, looks like you ran a python file called \"{script}\".")
print(f"Would you like to continue, {user_name}? ")
answer = input(prompt)

print(f"You answered {answer}.")