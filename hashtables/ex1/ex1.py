def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    #store each weight in the input list as keys: 
    if (weights, length, limit) in cache:
        return cache[(weights, length, limit)]
    elif weights <= 0:
        cache[(weights, length, limit)] = 
    return None
