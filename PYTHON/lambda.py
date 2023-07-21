people = [
    {"name": "Harry", "house": "Glffidor"},
    {"name": "Han", "house": "Slydinidor"},
    {"name": "buck", "house": "Asandador"}
      ]
##SUB this code here 
def f(pers):
    return pers["name"]
    
people.sort(key = f)

print(people)


#OR
people.sort
(key = lambda pers: pers["name"]
 print(people)

