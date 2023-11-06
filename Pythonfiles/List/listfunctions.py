lucky_numbers = ["5","7","9","12","23"]
friends=["Joy","Kevin","Tom","Jerry"]
friends.extend(lucky_numbers)
print(friends)

friends.append("Mary")
print(friends)

friends.insert(2,"Oscar")
print(friends)

friends2 = friends.copy()
print(friends2)

friends.pop()
print(friends)

friends.remove("Jerry")
print(friends)

print(friends.index("Tom"))

friends.reverse()
print(friends)

friends.clear()
print(friends)

