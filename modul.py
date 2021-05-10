def marked(listOfStudents):
    marks={}
    for i in listOfStudents:
        a=input(f"{i.title()}ning bahosini kiriting: ")
        marks[i]=a
    return marks

def mprint(list):
    b=marked(list)
    for i in b:
        print(f"{i.title()}ning bahosi {b.get(i)}")

