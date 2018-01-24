def func(a, b, c=0, *args, **kw):
    """a,b - 必选参数，c - 默认参数, *args - 可变参数, kw - 关键字参数"""
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

func(1, 2, 3, 4, x=9)
# a = 1 b = 2 c = 3 args = (4,) kw = {'x': 9}

nums = list(range(4, 8))

func(1, 2, 3, *nums)
# a = 1 b = 2 c = 3 args = (4, 5, 6, 7) kw = {}

func(1, 2, 3, nums)
# a = 1 b = 2 c = 3 args = ([4, 5, 6, 7],) kw = {}
