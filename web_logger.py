"""
Web Logger
"""
"""
Setup

We are building a new website, and we want to know how many visitors we are getting to the website. All we care about is how many visits we've gotten in the past 5 minutes, nothing more. Your job is to build this system, but implementing two functions:

# This function gets called every time the site is visited.
log_visit()

# This function is called whenever I visit an administrator page summarizing the website traffic. It should return the number of visits in the last 5 minutes.
get_visits() -> int

Part I: implement these functions

Please implement log_visit() and get_visits().You can use a function like time.time() in Python to get the current time, if that's useful.

The functions need to work even if the website becomes popular. For example, if we are using a list to store timestamps, that list will need to be pruned periodically so it doesn't become millions of items long (we only need to be able to report the number of visits in the last 5 minutes anyway).

Depending on how you are storing timestamps, you will likely need to implement a prune function that prunes old data from that data structure, and that prune function should be called in the right places in log_visit() and get_visits().
"""
import time

# initialize some data structure to hold each visit in past 5 min (300 seconds)
# TODO reset this to empty array for real case rather than hardcoded times
#  for testing
visits = [1610305864.0861466, 1610305865.0863435, 1610305867.087183,
          1610306258.0923035, 1610306248.0923035, 1610306238.0923035,
          1610306268.0923035]


def log_visit():
    # everytime this function is called log the time visited
    visits.append(time.time())
    # if the first entry in visits is more than 5 min ago we can prune it
    if time.time() - visits[0] > 300:
        prune_visits()


def get_visits():
    # first check if the first entry in visits is more than 5 min ago
    if time.time() - visits[0] > 300:
        prune_visits()
    # return the number of visits by returning the length of visits
    return len(visits)


# run this function if the first entry in visits is more than 300 seconds ago
# (5 min)
def prune_visits():
    # search visits to find the oldest timestamp within 5 min of time when
    # this function is called
    # binary search
    # init the max idx and the min idx
    max_time_idx = 0
    min_time_idx = len(visits) - 1
    # keep checking while the min time idx is not less than the max time idx
    while not min_time_idx < max_time_idx:
        # init the check point to be the middle of the list
        check = (max_time_idx + min_time_idx) // 2

        # init time passed into a variable for reuse in the checks below
        # TODO change time_now to equal time.time() for real case rather than
        #  hardcoded time being used for testing
        time_now = 1610306268.0923035
        time_passed = time_now - visits[check]

        # if the time passed has been more than 5 min
        if time_passed > 300:
            # check if the next item is not,
            # if it is not then we can stop and remove all previous visits
            # and return the pruned array
            if time_now - visits[check + 1] < 300:
                visits[:] = visits[check + 1:]
                return visits
            # if the next item is also over 5 min ago keep searching
            # change the max search idx to 1 more than the check point
            max_time_idx = check + 1
        # if the time passed was less than 5 min
        elif time_passed < 300:
            # keep searching and change the min search index to 1 less
            # than the check point
            min_time_idx = check - 1


log_visit()
print(f'get_visits: {get_visits()}')
print(visits)
