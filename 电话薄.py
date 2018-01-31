# -*- coding: UTF-8 -*-
class Phone_Book(object):
    def __init__(self,name='',path='/home/gao/桌面/phonebook.data'):
        self.name = name
        self.path = path

    def add_or_alter(self):
        tel = raw_input('请输入电话号码')
        try:
            fp = open(self.path,'r+')
        except IOError:
            fp = open(self.path,'w+')
            fp.write('{}')
        content = fp.read()
        fp.close()
        try:
            content = eval(content)
        except SyntaxError:
            content = {}
        content[self.name]=tel
        fp = open(self.path,'w')
        fp.write(str(content))
        fp.close()

    def delete(self):
        try:
            fp = open(self.path,'r+')
        except IOError:
            fp = open(self.path, 'w+')
            fp.write('{}')
            fp.close()
            fp = open(self.path, 'r+')
        content = fp.read()
        fp.close()
        content = eval(content)
        if self.name in content:
            del content[self.name]
        elif content == {}:
            print '通讯录为空，无法删除'
            exit()
        else:
            print "输入错误,请重新输入"
            return -1
        fp = open(self.path,'w')
        fp.write(str(content))
        fp.close()

    def select(self):
        try:
            fp = open(self.path,'r+')
        except IOError:
            fp = open(self.path, 'w+')
            fp.write('{}')
            fp.close()
            fp = open(self.path, 'r+')
        content = fp.read()
        fp.close()
        content = eval(content)
        if self.name in content:
            print '%s的电话为%s'%(self.name,content[self.name])
        elif content == {}:
            print '通讯录为空'
            exit()
        else:
            print '输入错误,请重新输入'
            return -1

    def select_all(self):
        try:
            fp = open(self.path,'r+')
        except IOError:
            fp = open(self.path, 'w+')
            fp.write('{}')
            fp.close()
            fp = open(self.path, 'r+')
        contents = fp.read()
        fp.close()
        try:
            contents = eval(contents)
        except SyntaxError:
            contents = {}
        if contents == {}:
            print '通讯录为空'
        else:
            for content in contents.items():
                print '%s的电话为%s'%content

    def delete_all(self):
        fp = open(self.path,'w+')
        fp.close()

if __name__ == '__main__':
    while True:
        input = raw_input('1.添加或修改 2.删除 3.查找 4.查看全部 5.删除全部 6.退出')
        if input == '1':
            name = raw_input('请输入姓名')
            phone_book=Phone_Book(name)
            phone_book.add_or_alter()
            break
        if input == '2':
            while True:
                name = raw_input('请输入姓名')
                phone_book = Phone_Book(name)
                if phone_book.delete()==-1:
                    pass
                else:
                    break
            break
        if input == '3':
            while True:
                name = raw_input('请输入姓名')
                phone_book = Phone_Book(name)
                if phone_book.select()==-1:
                    pass
                else:
                    break
            break
        if input == '4':
            phone_book = Phone_Book()
            phone_book.select_all()
            break
        if input == '5':
            while True:
                ask = raw_input('确定清除全部通讯录？Y/N')
                if ask == 'Y' or ask == 'y':
                    phone_book = Phone_Book()
                    phone_book.delete_all()
                    print '已清空'
                    break
                elif ask == 'N' or ask == 'n':
                    exit()
                else:
                    print '输入错误请重新输入'
            break
        if input == '6':
            exit()
        else:
            print '输入错误,请重新输入'



