def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # first I need to set a dictionary to hold all the results
    results = {}
    # how does the cache hold the info
    for pos_and_neg in a:

        # what happens if the list has no numbers? return None
        if a == 0:
            return None
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
