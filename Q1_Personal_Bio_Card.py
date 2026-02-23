# Program: Personal Bio Card
#---------------------------------------------------------
#  Storing  personal details in variables
name = "Anusha Raykar"
age = 23
course = "Python Programming"
college = "PES Institute"
email = "anuraykar@gmail.com"

# width of the card
width = 42

#top border of the card
print("+" + "-" * width + "+")

# title centered inside the card 
print("|" + "STUDENT BIO CARD".center(width) + "|")

#seperator line below title
print("+" + "-" * width + "+")

#student details in aligned format
print("| {:<10}: {:<29}|".format("Name", name))
print("| {:<10}: {:<29}|".format("Age", age))
print("| {:<10}: {:<29}|".format("Course", course))
print("| {:<10}: {:<29}|".format("College", college))
print("| {:<10}: {:<29}|".format("Email", email))

#bottom border of the card
print("+" + "-" * width + "+")