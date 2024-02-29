# Iterables? __iter__ | Loop it many times  Which can be looped: List
# Doesnt know where I am in the loop | losts of memory
# Iterator? __next__ | Loops it one time
# They know where we are in the loop | memory saver |lazy


def main():
    nums = [5, 10, 20]
    print(nums)
    print(dir(nums))

    # nums_iter = nums.__iter__()  # coverts to iterator | Iterables --> Iterator
    nums_iter = iter(nums)
    print(nums_iter)
    print(dir(nums_iter))  # iterator --> __next__ & __iter__
    # Conculsion All iterator are Iterables | but not the other way

    # print(next(nums_iter))
    # print(next(nums_iter))
    # print(next(nums_iter))

    while True:
        try:
            print(next(nums_iter))
        except StopIteration:
            break

    nums_iter2 = iter([80, 90, 100])
    for num in nums_iter2:
        print(num)

    # range(1, 100_000_000, 1) # List with 100 million values lots of memory
    # iterator rember on thing at time | save memory
    # __next__ & __iter__


class MyRange:
    def __init__(self, start, end):
        self.curr = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr > self.end:
            raise StopIteration
        self.curr += 1
        return self.curr - 1


# class more verbose | genererator is more consise
# Generator - clean | returns a iterator
def inifite_integers():
    n = 0
    while True:
        yield n  # return & pause
        n += 1


def fibonacci():
    a, b = 1
    while True:
        yield a
        a = b
        b = a + b


def fib(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a + b
        # temp = a
        # a = b
        # b = temp + b


if __name__ == "__main__":
    # main()

    # for n in MyRange(1, 5):
    #     print(n)

    # integers = inifite_integers()
    # print(next(integers))  # 0
    # print(next(integers))  # 1
    # print(next(integers))  # 2

    for num in fib(10):
        print(num)
