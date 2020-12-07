
friends = []
answer = None

"""while answer != "quit":
    answer = input("what is the name of your friend? ")
    if answer == "quit":
        break
    friends.append(answer.title())"""
    
    
while True:
    answer = input("what is the name of your friend? ")
    if answer == "quit":
        break
    friends.append(answer.title())

print(f"You have {len(friends)} friends")
print("The name of your friends are: " + ", ".join(friends))


