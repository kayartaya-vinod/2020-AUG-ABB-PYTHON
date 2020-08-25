"""
This is a demonstration of 'for' loop
"""


# main() is just another function; nothing special about
def main():
    names = ["Vinod", "Shyam", "Satya", "Naveen", "Harish"]

    for name in names:
        # print("Hello %s have a nice day." % name)
        print("Hello {}, have a nice day".format(name))


main()
