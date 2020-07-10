def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # first I need to set a dictionary to hold somehting. the fuck if i know what.
    # next I need to figure out how to hold an array of just numbers that have a corresponding negative value in the dictoinary
    ## fuck this bullshit.

    # this is the dictionary
    num_cache = {}

    # this is how I want the result to be dipslayed, it needs to come back out in an array
    # in it  are the numbers that have neg and pos from the same list
    result = []

    # i'll be appending some sort of info to that result list
    # how the fuck do I compare them...

    # loop over a and find the duplicates and put them in the cache
    for x in a:

        if x < 0 and x not in num_cache:
            # cache set and full of negatives
            num_cache[x] = x
            print("this is the cache", num_cache)
    # now loop through the cache and comparing the lists
    for x in num_cache:
        print("this is x", num_cache)
        if x in a:
            print("this is if x", x)
            result.append(x * -1)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
