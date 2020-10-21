import sys
from flow import recall_flow, add_flow, count_flow

argv = sys.argv[1:]

if (len(argv) < 1):
    print("Options: recall, add or count")
elif (argv[0] == 'recall'):
    level = argv[2] if len(argv) > 2 else 0
    recall_flow()
elif (argv[0] == 'add'):
    add_flow()
elif (argv[0] == 'count'):
    count_flow()
else:
    print("Options: recall, add or count")
