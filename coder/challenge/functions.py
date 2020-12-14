def validate(answer):
    return True


def run_tests(answer, test):
    exec(answer, globals(), globals())
    exec(test, globals(), globals())

    test_case(function)
