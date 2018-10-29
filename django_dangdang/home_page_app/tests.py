import django
from django.test import TestCase
import os
# Create your tests here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_dangdang.settings")
django.setup()
from home_page_app.models import Book

def addBook(b_name,b_product_image_path,b_book_author,b_price,b_dprice,b_customer_socre):
    book = Book(book_name=b_name,product_image_path=b_product_image_path,book_author=b_book_author,book_price=b_price,book_dprice=b_dprice,customer_socre=b_customer_socre)
    book.save()

if __name__ == '__main__':
    addBook("名人传",'/static/images/20175470-1_l.jpg','罗曼·罗兰',120,60,8.8)
    addBook("学会自己长大",'/static/images/22855492-1_l_3.jpg','和云峰',100,60,9.1)
    addBook("哲人与先知的价值追求",'/static/images/22860102-1_l_1.jpg','洪恩赐',50,30,8.2)
    addBook("我们仨",'/static/images/22880790-1_l_2.jpg','杨绛',40,30,6.5)
    addBook("从你的全世界路过",'/static/images/23353342-1_l.jpg','张嘉佳',55,44,6.7)
    addBook("大败局2",'/static/images/23368526-1_l.jpg','吴晓波',22,15,7.8)
    addBook("摆渡人",'/static/images/23694647-1_l_1.jpg','克莱儿·麦克福尔', 65,45,7.7)
    addBook("喜欢我也没关系",'/static/images/24156322-1_l_6.jpg','牛牛吖',49.80,30,8.1)
    addBook("你的努力,终将成就无可替代的自己",'/static/images/1900513383-1_l_3.jpg','汤木',32,23,8.0)
    addBook("自控力",'/static/images/1900537714-1_l_4.jpg','凯利·麦格尼格尔',39.8,33,8.3)
    addBook("30岁后,我靠投资生活",'/static/images/1900542997-1_l_4.jpg','搜狐采集栏目组   钟慧   罗为加',32.80,30,8.1)
    addBook("知更鸟女孩",'/static/images/1900560686-1_l_8.jpg','查克·温迪格',32,22,7.5)


