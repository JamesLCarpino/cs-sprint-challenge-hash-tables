#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        # represents the starting airport
        # self.source.prev = NONE
        self.destination = destination
        # represents the next airport on trip
        # final trip has a destination of NONE
        # self.destination.next = NONE


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    route = []
    for t in tickets:
        if t.source == "NONE":
            # check to see if the source is NONE, if it is append it to the route list
            route.append(t.destination)
        # link the destination Name to the Source Name
        cache[t.source] = t.destination
        # set the current ticket to the cashed first ticket in the index...which is the one with NONE
    c_ticket = cache[route[0]]
    # keep track of the trip index count
    trips = 1

    while trips < length:
        route.append(c_ticket)
        c_ticket = cache[c_ticket]
        trips += 1

    # array of entire route to be returned

    return route


# notes
