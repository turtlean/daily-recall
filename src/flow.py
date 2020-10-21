from entries import find_random_entry, print_entry, add_entry, count


def recall_flow():
    print_entry(find_random_entry())


def add_flow():
    entry = input("\nEntry:  ")

    add_entry(entry)
    print("\nYour entry was successfully added\n")


def count_flow():
    print('\n %s entries \n' % (count()))
