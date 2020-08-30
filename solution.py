one_hours = int(input())
one_minuts = int(input())
one_seconds = int(input())
two_hours = int(input())
two_minuts = int(input())
two_seconds = int(input())

seconds_one = (one_hours * 60 * 60) + (one_minuts * 60) + one_seconds
seconds_two = (two_hours * 60 * 60) + (two_minuts * 60) + two_seconds

print(seconds_two - seconds_one)
