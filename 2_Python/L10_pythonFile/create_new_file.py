user_date =[
    {
        'file_name': 'user_1.txt',
        'context': 'Hello, This is from user 1'
    },
    {
        'file_name': 'user_2.txt',
        'context': 'Hello, This is from user 2'
    },
    {
        'file_name': 'user_3.txt',
        'context': 'Hello, This is from user 3'
    }
]

for data in user_date:
    file_name = data["file_name"]
    context = data["context"]
    # print(file_name, context)
    with open(file_name, 'w') as file:
        file.write(context)

