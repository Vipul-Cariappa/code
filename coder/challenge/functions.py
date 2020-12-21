def validate(answer):
    if answer.split("\n")[0].startswith("def function("):
        return all(True if i not in ["exec", "eval", "import",
                                     "from"] else False for i in answer.split())
    return False


def run_tests(answer, test):
    exec(answer, globals(), globals())
    exec(test, globals(), globals())

    test_case(function)
