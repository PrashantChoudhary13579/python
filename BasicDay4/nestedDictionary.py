#nested dictionary - dictionary into dictionary

student ={
    "name": "Prashant",
    "score":{
        "Chemistry":95,
        "Physics":95,
        "Maths":99
    },
    "class" : 12,
    "school" : "Gita Niketan Awasiya Vidhyalay"
}

print(student)
print(student["score"])
print(student["score"]["Maths"])
