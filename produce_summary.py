# Create a function:
def file_reader(file):
    """Function reads through the file text
    outputs cost of produce from file"""

    for line in file:
        line = line.rstrip()
        words = line.split("|")

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    file.close()


# =====================================

print("Day 1")
# Function call:
file_reader(file=open("um-deliveries-20140519.txt"))

print("Day 2")
# Function call:
file_reader(file=open("um-deliveries-20140520.txt"))

print("Day 3")
# Function call:
file_reader(file=open("um-deliveries-20140521.txt"))

