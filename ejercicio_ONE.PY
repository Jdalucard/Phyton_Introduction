# DIFFERENCE IN PERCENTAGE BETWEEN CURRENT AND PREVIOUS COURSES
""" 
THE FASTEST OF OTHER COURSES
THE SLOWEST OF OTHER COURSES
THE AVERAGE OF THE COURSES

PERCENTAGE OF UNUSABLE MATERIAL

-THE AVERAGE OF THE COURSES
-THE CURRENT COURSE (THIS COURSE)

SEE HOW MANY HOURS OF THIS COURSE ARE EQUIVALENT TO IN OTHER COURSES AND VICE VERSA 
"""

CURRENT_COURSE_HOURS = 1.5
MAX_COURSE_HOURS = 7
AVERAGE_COURSE_HOURS = 4.0
MIN_COURSE_HOURS = 2.5
RAW_OTHER = 5
RAW_CURRENT = 3.5

#
percentage_current_course = 100 - (CURRENT_COURSE_HOURS / MIN_COURSE_HOURS) * 100
percentage_slow_course = 100 - (CURRENT_COURSE_HOURS / MAX_COURSE_HOURS) * 100
average = 100 - (CURRENT_COURSE_HOURS / AVERAGE_COURSE_HOURS) * 100


print("Percentage curs actual: {:.2f}%".format(percentage_current_course))
print("Percentage curs lento: {:.2f}%".format(percentage_slow_course))
print("Average: {:.2f}%".format(average))  
print()

# Parte B
time_variation = 100 - (AVERAGE_COURSE_HOURS / RAW_OTHER) * 100
time_variation_dalton = 100 - (CURRENT_COURSE_HOURS / RAW_CURRENT) * 100

print("Other course B: {:.2f}%".format(time_variation))
print("Other course B (Dalton): {:.2f}%".format(time_variation_dalton))
print()

# Parte C
other_course_equivalent_dalton = AVERAGE_COURSE_HOURS / CURRENT_COURSE_HOURS * 10
print("Other course is equal to: {:.2f} hours of this course".format(other_course_equivalent_dalton))

other_course_equivalent_current = CURRENT_COURSE_HOURS / AVERAGE_COURSE_HOURS * 10
print("This course is equal to: {:.2f} hours of other course".format(other_course_equivalent_current))