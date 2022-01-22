def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    inclusive_stop = stop + 1
    given_range = range(start,inclusive_stop)
    for number in given_range:
        print(number)

count_up(5, 7)        
