

def create_outline():
    Course_topics = {"Functions", "How to make decisions", "How to repeat code", "How to structure data", "Introduction to Python", "Modules", "Tools of the Trade"}
    list_problems = ["Problem 1", "Problem 2", "Problem 3"]
    #new_list = ', '.join(list_problems)
    #point = '*'
    #Course_topics = [Course_topics]
    # Course_topics.sort()
    list_course = sorted(list(Course_topics))
    dict_course = dict()
    for b in list_course:
        dict_course[b] = list_problems

    #part1    
    print("Course Topics:")
    # Course_topics_1 =["Introduction to Python", "Tools of the Trade", "How to make decisions", "How to repeat code", "How to structure data", "Functions", "Modules"]
    #for x in Course_topics:
    for x in dict_course:
        print("*",x)
    
    #part2
    print("Problems:")
    for key,value in dict_course.items():
        print("*", end=' ')
        print(key, end=" : ")
        print(*value, sep=', ')
    """
    look into dict.fromkeys()
    mydict = dict.fromkeys(topics, new_list)
    """


    print('Student Progress: ')

    #Name = ["Nyari", "Adam", "Tom"]
    #Status = ["GRADED", "STARTED", "COMPLETED"]

    print("1. Nyari - How to make decisions - Problem 3 [STARTED]")
    print("2. Adam - Tools of the Trade - Problem 1 [GRADED]")
    print("3. Tom - Introduction to Python - Problem 2 [COMPLETED]")
    


if __name__ == "__main__":
    create_outline()
