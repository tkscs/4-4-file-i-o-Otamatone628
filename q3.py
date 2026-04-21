# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

####
#### YOUR CODE HERE 
####
with open("romeo_and_juliet.txt", "r") as f:
    text = f.read()
# Count how many times the word "Juliet" appears
juliet_count = text.count("Juliet")
print(f"'Juliet' appears {juliet_count} times in Romeo and Juliet")
####
#### YOUR CODE HERE 
####
