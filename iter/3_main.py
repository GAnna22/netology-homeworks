class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = list(list_of_list[::-1])

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            item = self.stack.pop()
            if isinstance(item, list):
                self.stack.extend(item[::-1])
            else:
                return item
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(flat_iterator_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()