class TestSuite:

    def __init__(self, name):
        self.name = name
        self.suites = []
        self.cases = []

    def add_test_cases(self, case):
        self.cases.append(case)

    def add_test_suites(self, suite):
        self.suites.append(suite)

    @staticmethod
    def print_hierarchy(suite, indentation=0):
        print(" " * indentation + f"Test Suite Name: {suite.name}")
        for test_case in suite.cases:
            print(" " * (indentation + 1) + f"Test Case Name: {test_case.name}")
        for test_suite in suite.suites:
            test_suite.print_hierarchy(test_suite, indentation=indentation + 1)


class TestCase:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    main_suite_case_one = TestCase(name="MainSuiteCaseOne")
    main_suite_case_two = TestCase(name="MainSuiteCaseTwo")
    main_suite_sub_suite_one = TestSuite(name="MainSuiteSubSuiteOne")
    main_suite_sub_case_one = TestCase(name="MainSuiteSubCaseOne")
    main_suite_sub_suite_one.add_test_cases(main_suite_sub_case_one)
    main_suite = TestSuite(name="MainSuite")
    main_suite.add_test_suites(main_suite_sub_suite_one)
    main_suite.add_test_cases(main_suite_case_one)
    main_suite.add_test_cases(main_suite_case_two)
    for i in range(3, 10, 1):
        tmp_case = TestCase(name=f"MainSuiteCase{i}")
        main_suite.add_test_cases(tmp_case)
    main_suite.print_hierarchy(suite=main_suite)
