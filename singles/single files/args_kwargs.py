def test1(a, b, c):
    print(a, b, c)

def test2(a, b, c, *args):
    print(type(args))
    print(a, b, c, args)

def test3(a, b, c, *args):
    # print(type(*args)) # Error
    print(a, b, c, *args)

def test4(a, b, c, *args, **kwargs):
    print(type(kwargs))
    print(a, b, c, *args, kwargs)

def test5(a, b, c, *args, **kwargs):
    # print(type(*kwargs)) # Error
    print(a, b, c, *args, *kwargs)

def test6(a, b, c, *args, **kwargs):
    # print(type(**kwargs)) #Error
    # print(a, b, c, *args, **kwargs) # Error
    pass

def render_template(template_name, **kwargs):
    print(template_name)
    print(type(kwargs))
    print(kwargs)
# test1("ali", "sara", "arta")
# test1("ali", "sara", "arta", 1, 2, 3) # Error
# test2("ali", "sara", "arta", 1, 2, 3)
# test3("ali", "sara", "arta", 1, 2, 3)
# test3("ali", "sara", "arta", 1, 2, 3, m=6)
# test4("ali", "sara", "arta", 1, 2, 3, m=6)
# test5("ali", "sara", "arta", 1, 2, 3, m=6, n=4, t=9)
# test6("ali", "sara", "arta", 1, 2, 3, m=6, n=4, t=9)

context = {
    'device_id': '12354',
    'password': '1124',
}
# render_template('test.html', context) # Error
render_template('test.html', context=context)
render_template('test.html', k=context)
render_template('test.html', **context)