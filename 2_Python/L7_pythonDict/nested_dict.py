courses = {
    "CSE101": {
        "Title": "Structure Programming",
        "Duration": 6,
        "Credit": 3
    },
    "CSE102": {
        "Title": "Discrete Mathematics",
        "Duration": 6,
        "Credit": 3
    },
    "SE106": {
        "Title": "Introduction to SE",
        "Duration": 6,
        "Credit": 3
    }
}
print(courses)

print(courses["CSE101"]["Title"])
print(courses["SE106"]["Credit"])

courses["CSE102"]["Duration"] = 4
print(courses["CSE102"])
