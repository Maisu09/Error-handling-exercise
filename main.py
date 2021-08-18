#TODO: Catch the exception and make sure the code euns without crashing.

# fruits = ['Apple', 'Pear', 'Orange']
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + 'pie')

# make_pie(4)



# rezolvare

# fruits = ['Apple', 'Pear', 'Orange']
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + 'pie')

# try:
#     make_pie(4)
# except IndexError:
#     print("The value was not a good one ")
#     print("Apple pie")



#TODO: Catch the exception and make sure the code euns without crashing.

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2,'Shares':1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 3},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3},

# ]

# total_likes = 0
# for post in facebook_posts:
#     total_likes = total_likes + post['Likes']

# print(total_likes)

#rezolvare

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2,'Shares':1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 3},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3},

# ]

# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass

# print(total_likes)
