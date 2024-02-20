import os
from datetime import datetime
from modules.application.salary import calculate_salary

def logger(path):

    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a+') as log_file:
                nl = '\n'
                log_file.write(f'{datetime.now()}: {old_function.__name__} - '
                               f'{args} - {kwargs} - {result} {nl}')
            return result

        return new_function

    return __logger


def test_3():
    paths = ('log_decor.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def calc_sal():
            return calculate_salary()

        assert "Salaries: {'Anna': 90000, 'Peter': 200000, 'Ivan': 65000, 'Alexander': 120000}" == calc_sal()

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'calculate_salary' in log_file_content, 'должно записаться имя функции'


if __name__ == '__main__':
    test_3()
