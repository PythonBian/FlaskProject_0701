
def login_outer(fun):
    def inner():
        print("我是校验饰器")
        fun()
        print("给你校验后视图")
    return inner

def url_outer(fun):
    def inner():
        print("我是路由装饰器")
        fun()
        print("给你视图处理的结果")
    return inner

@url_outer
@login_outer
def views():
    print("我是视图")

views()