"""
基于过期时间的函数结果缓存装饰器
函数结果字典的key值基于函数的位置参数和关键字参数
"""

import time


class FunctionResultCache:
    res_dict = {}

    def __init__(self, interval: int, debug=False):
        self._debug = debug
        self.interval = interval

    def __call__(self, func):
        def _wrapper(*args, **kwargs):
            hash_value = hash(self.make_key(args, kwargs))
            if hash_value not in self.res_dict or time.time() - self.res_dict[hash_value]["join_time"] > self.interval:
                if self._debug:
                    print("执行函数")
                func_res = func(*args, **kwargs)
                self.res_dict.update({
                    hash_value: {
                        "res": func_res,
                        "join_time": time.time()
                    }
                })
                return func_res
            else:
                if self._debug:
                    print("读取缓存")
                return self.res_dict[hash_value]["res"]

        return _wrapper

    @staticmethod
    def make_key(args: tuple, kwargs: dict):
        kwd_mark = (object(),)
        key = args
        if kwargs:
            key += kwd_mark
            for item in kwargs.items():
                key += item

        return key


if __name__ == '__main__':
    @FunctionResultCache(interval=3, debug=True)
    def test(name):
        time.sleep(3)
        return name

    print(time.time())
    print(time.time(), test("leon"))
    time.sleep(1)
    print(time.time(), test("leon"))
    time.sleep(1)
    print(time.time(), test("leon"))
    time.sleep(1)
    print(time.time(), test("leon"))

