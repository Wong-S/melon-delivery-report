# Create a function:
def file_reader(file):
    """Function reads through the file text
    outputs cost of produce from file"""

    for line in file:
        line = line.rstrip()
        words = line.split("|")

        melon = words[0]
        count = words[0]
        amount = words[0]

        print("Delivered {} {}s for total of ${}".format(count, melon, amount))
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

