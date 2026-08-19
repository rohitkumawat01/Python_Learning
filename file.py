# # how to read the file..

# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()

# # how to write in a file

# a="hello rohit, how are you ?"
# f=open("my.txt","w")
# f.write(a)
# f.close()


# with statement 
# with open("file.txt") as f:
#     print(f.read())


# f=open("poeam.txt")
# content=f.read()
# if("twinkel"in content):
#     print("yes it in the file")

# else:
#     print("there is not a such type of word")

# f.close()


# question 

# import random
# def game():
#     print("you are playing game..")
#     score=random.randint(1,62)

#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print(f"your score:-{score}")
#     if(score>hiscore):
#         with open("hiscore.txt","w") as f:
#          f.write(str(score))

#     return score

# game()


# question
# def generateTable(n):
#     table=""
#     for i in range(1,11):
#         table +=f"{n} x {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)


# for i in range(2,6):
#     generateTable(i)


# question  

# word="donkey"
# with open("new.txt","r") as f:
#     content = f.read()

# contentNew=content.replace(word,"######")

# with open("new.txt", "w") as f:
#     f.write(contentNew)



