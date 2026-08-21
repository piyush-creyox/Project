'''Write a Python program to sort a dictionary of dictionaries based on the value of a specific 
nested key (e.g., a 'sequence' number).'''


Languages = {
    "1": {"Language" : "Python","OOP":"yes","Sequence":3},
    "2": {"Language": "Java" , "OOP": "yes","Sequence":1},
    "3": {"Language": "C", "OOP": "no", "Sequence":2}
}


sorted_languages = dict(
    sorted(Languages.items(), key=lambda item: item[1]["Sequence"])
)

print(sorted_languages)
