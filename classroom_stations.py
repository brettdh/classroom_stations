#!/usr/bin/env python

from random import shuffle
import sys

def format_student(student):
    return "Student {0}".format(student)

def available_stations(stations, students_per_station):
    for i, station in enumerate(stations):
        if len(station) < students_per_station[i]:
            yield i, station

num_students = 28
num_stations = 6
students_per_station = [num_students / num_stations + 1] * num_stations
for i in xrange(num_students - sum(students_per_station)):
    students_per_station[i] += 1

teacher_table_count = 4
teacher_table_order = range(num_students)
shuffle(teacher_table_order)

assert sum(students_per_station) >= num_students

students = [range(num_stations) for i in xrange(num_students)]

def get_student_choices(student, students, stations, students_per_station):
    choices = [station for station in students[student]
               if len(stations[station]) < students_per_station[station]]
    shuffle(choices)
    return choices

def find_swap_station(student, students, stations, students_per_station):
    for empty_slot, _ in available_stations(stations, students_per_station):
        for choice in students[student]:
            for swap_candidate in stations[choice]:
                if empty_slot in students[swap_candidate]:
                    print "{0} swaps with {1}".format(
                        format_student(student),
                        format_student(swap_candidate))
                    students[swap_candidate].append(choice)
                    students[swap_candidate].remove(empty_slot)
                    stations[choice].remove(swap_candidate)
                    stations[empty_slot].append(swap_candidate)
                    return [choice]
    return []


for i in xrange(num_stations + 1):
    stations = [[] for j in xrange(num_stations)]
    teacher_table = teacher_table_order[:teacher_table_count]
    teacher_table_order = teacher_table_order[teacher_table_count:]
    
    student_order = filter(lambda x: x not in teacher_table, range(num_students))
    shuffle(student_order)
    for student in student_order:
        available = get_student_choices(student, students, stations, students_per_station)
        if not available:
            available = find_swap_station(student, students, stations, students_per_station)
            if not available:
                print "{0} has nowhere to go!".format(format_student(student))
                print "{0}: {1!s}".format(format_student(student), students[student])
                print "Stations: ", stations
                sys.exit(1)

        choice = available[0]
        stations[choice].append(student)
        students[student].remove(choice)
        
    print "Round {0}: {1!s}  Teacher: {2!s}".format(i + 1, stations, teacher_table)
