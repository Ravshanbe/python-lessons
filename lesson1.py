# f1={'name':'elon','surname':'musk','company':['tesla','neuralink','spacex']}
# f2={'name':'jeff','surname':'bezos','company':['amazon','blue orign','disney']}
# f3={'name':'tim','surname':'kuk','company':['iphone','iwatch','macbook']}
# f4={'name':'bill','surname':'gates','company':['microsoft','surface','pixar']}
# famous=[f1,f2,f3,f4]
# for p in famous:
#     print(f"\n{p['name'].title()} {p['surname'].title()} mahsulotlari: ",end='')
#     for i in p['company']:
#         print(i.upper(),end=", ")
def q(name, surname,town,tel='',email=''):
    a={
        'name':name.title(),
        'surname':surname.title() ,
        'town':town.title() ,
        'tel':tel,
        'mail':email
    }
    return a
customer=[]
while True:
    n=input("name:")
    s=input("surname:")
    t=input("town:")

    customer.append(q(n,s,t))
    a=input("do you want add any?(yes/no)")
    if a=='no':
        break
for i in customer:
    print(f"Name: {i.get('name')}")
    print(f"Surname {i.get('surname')}")
    print(f"Town {i.get('town')}")
