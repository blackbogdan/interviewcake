# coding=utf-8
"""Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as tuples ↴ of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3) # meeting from 10:00 – 10:30 am
(6, 9) # meeting from 12:00 – 1:30 pm

Write a function condense_meeting_times() that takes a list of meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams."""

m = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
m1 = [(1, 2), (2, 3)]
m2 = [(1, 5), (2, 3)]
m3 = [(1, 10), (2, 6), (3, 5), (7, 9)]
def merge_ranges(meetings):
    # sort by start times
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings
print merge_ranges(m)
# Bonus
# What if we did have an upper bound on the input values? Could we improve our runtime? Would it cost us memory?
# Could we do this "in-place" on the input list and save some space? What are the pros and cons of doing this in-place?