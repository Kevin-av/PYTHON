with open("students.txt", "r") as file:
    content = file.readlines()
    if len (content) >= 5:
        line = content[0:3]
    else:
        line = content
    
    for content in line:
        print (content.strip())
