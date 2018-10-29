from home_page_app.models import Book


class Cartltem():
    def __init__(self,book,amount):
        self.book = book
        self.amount = amount


class Cart():
    def __init__(self):
        self.cartltems = []
        self.total_price = 0
        self.save_price = 0
        #计算总价
    def sum(self):
        # self.total_dprice = 0
        # self.save_price = 0
        a=0
        b=0
        print(12322,len(self.cartltems))
        for i in self.cartltems:
            a += round(i.book.book_dprice * i.amount,2)
            b += round((i.book.book_price - i.book.book_dprice) * i.amount,2)
        self.total_price = a
        self.save_price = b
        print(i.amount, i.book.book_dprice, self.total_price)
    #添加购物车
    def add(self,book_id,amount):
        for i in self.cartltems:
            print(amount)
            if i.book.book_id == book_id :
                i.amount += int(amount)
                self.sum()
                return self
        book = Book.objects.get(pk=book_id)
        self.cartltems.append(Cartltem(book,int(amount)))
        self.sum()
        return self

    #删除购物车
    def delete(self,book_id):
        for i in self.cartltems:
            if i.book.book_id == book_id:
                self.cartltems.remove(i)
            self.sum()

    #修改购物车
    def modify(self,book_id,amount):
        for i in self.cartltems:
            if i.book.book_id == book_id:
                i.amount += amount
        self.sum()
        return self

