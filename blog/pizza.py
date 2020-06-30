# product =dict()
#
# data={'aalu':'aalu','price':300}
# data.update({"tamator": "tamtor"})
#
# print(data)

#
# product = dict()
# data = input('enter your products  ')
# temp = data.split(':')
# product[temp[0]] = (temp[1])
# for key, value in product.items():
# 	print('Name: {}, Score: {}'.format(key, value))



plist =[]
orders=dict()
class Product:
    def __str__(self):
        self.name=''
        self.price =''
    def save(self):
        plist.append(self)


def order_avalablity(name=""):
    status =dict()
    for o in plist:
        if(o.name==name):
            status['res']={'name':o.name,'price':o.price}

    return status

def order(name="",price=0):
    if name:
        orders[name]=[name,price]
while True:
    print("1 addproduct\n2 order\n0 exit")
    ch =input("choice:")
    if ch =="1":
        p =Product()
        p.name=input("Product Name:")
        p.price=input("Product price:")
        p.save()
    if ch =="2":
        name = input("Product Name:")
        status =order_avalablity(name)

        if not status:
            print("No product!")
        else:
            print("Your Order is :")
            print(1," Name:",status['res']['name'],"=",status['res']['price'])
            ord =input("want to place order? 'y' or 'n' :")
            if ord =='y':
                order(name,200)
                print("your Order successfully")
    if ch=="0":
        print("Thank You ! Welcome Back")
        break

