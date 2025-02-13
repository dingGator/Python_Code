programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}


#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
#********************************program********
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# scoring_criteria = {
#     91 - 100: 'Outstanding',
#     81 - 90: 'Exceeds Expectations',
#     71 - 80: 'Acceptable',
#     70 or lower: 'Fail',
# }

student_grades = {}
def convert_score_to_grades(student_scores,student_grades):
    score_value= ""
    for student_name in student_scores:
        if student_scores[student_name] >= 91:
            print(student_name)
            print("Outstanding")
            score_value = "Outstanding"
        elif student_scores[student_name] >=81:
            print(student_name)
            print("Exceeds Expectations")
            score_value = "Exceeds Expectations"
        elif student_scores[student_name] >= 71:
            print(student_name)
            print("Acceptable")
            score_value = "Acceptable"
        elif student_scores[student_name] <= 70:
            print(student_name)
            print("Fail")
            score_value = "Fail"
        else:
            print(student_name)
            print(f"Invalid score for {student_name} score {score_value}")
        student_grades[student_name] = score_value
        print(f"dictionary: {student_grades}")

convert_score_to_grades(student_scores,student_grades)

print("\n********** Nested Lists and Dictionaries ********************\n")

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested List of Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany":["Stuttgart", "Berlin"],
}

#print Lille
print(travel_log)
print(travel_log["France"][1])

#nested list
nest_list = ["A","B", ["C","D"]]

print(nest_list[2][1])

travel_log2 = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log2)
print(travel_log2["Germany"]["cities_visited"][2])
print(f" travel_log2  {travel_log2['Germany']['cities_visited'][2]}")



