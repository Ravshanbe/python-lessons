f1={'name':'elon','surname':'musk','company':['tesla','neuralink','spacex']}
f2={'name':'jeff','surname':'bezos','company':['amazon','blue orign','disney']}
f3={'name':'tim','surname':'kuk','company':['iphone','iwatch','macbook']}
f4={'name':'bill','surname':'gates','company':['microsoft','surface','pixar']}
famous=[f1,f2,f3,f4]
for p in famous:
    print(f"\n{p['name'].title()} {p['surname'].title()} mahsulotlari: ",end='')
    for i in p['company']:
        print(i.upper(),end=", ")