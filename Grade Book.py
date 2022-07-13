


# Original subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history",	88]]

# New grade added to lists
gradebook.append(["computer science", 100])

# Another new grade added
gradebook.append(["visual arts", 93])

# prints new updated gradebook
print(gradebook)

# altering the grade for visual arts using index
gradebook[5][1] = 98

# prints new gradebook with new grade for visual arts
print(gradebook)

gradebook.remove(["poetry", 85])
gradebook.append(["poetry", "Pass"])


# prints new gradebook with poetry deleted
print(gradebook)
