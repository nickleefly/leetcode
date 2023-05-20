"""
This assignment has a few basic programming puzzles, all themed around making
change. Change as in: You need a dollar and seventy-three cents in coins. Which
coins do you get back?
You can see your progress by running this script, like follows:
> python 01.py
It will report which tests are passing and which are failing.
The assignment is complete once it reports that you've finished all the tests.
1 quarters = 25 cents
1 dime = 10 cents
1 nickel = 5 cents
1 penny = 1 cent
"""


def assignment():

    def make_change_us(cents):
        """This method should take in a number of cents, and compute the change.
        For example, if it is given 85 cents, it should return 1 quarter and one
        dime. If it is given 18 cents, it should return one dime, one nickel, and
        three pennies. It should use as few coins as possible."""

        quarters = 0
        dimes = 0
        nickels = 0

        # put your logic here!

        return [quarters, dimes, nickels, cents]

    tester = Tester()
    tester.test(make_change_us(4), [0, 0, 0, 4], "4 cents")
    tester.test(make_change_us(18), [0, 1, 1, 3], "18 cents")
    tester.test(make_change_us(43), [1, 1, 1, 3], "43 cents")
    tester.test(make_change_us(1585332), [63413, 0, 1, 2], "$15,853.32")

    def make_change_harry_potter(knuts):
        """Now we're going to do the same task, but with Harry Potter currency.
        There are 29 knuts in a sickle, and 17 sickles in a galleon."""
        galleons = 0
        sickles = 0

        # put your logic here!

        return [galleons, sickles, knuts]

    tester.test(make_change_harry_potter(5), [0, 0, 5], "5 knuts")
    tester.test(make_change_harry_potter(182), [0, 6, 8], "182 knuts")
    tester.test(make_change_harry_potter(5382), [10, 15, 17], "5382 knuts")
    tester.test(make_change_harry_potter(95333), [193, 6, 10], "95333 knuts")

    def make_change_arbitrary(c, denominations):
        """Did you notice how the logic for make_change_us and make_change_harry_potter
        was almost the same? You were basically repeating yourself for two different
        sets of numbers. We programmers hate repeating ourselves - it tends to make for
        brittle and buggy programs, because it is hard to change multiple copies of the same
        logic. If we realize that these methods have a bug, will we remember to fix both
        of them?
        This comes up so much that there's a programmer word for code that doesn't
        repeat itself - it's called DRY, which stands for Don't Repeat Yourself.
        We programmers love for our code to be DRY. So let's do that here.
        This make_change_arbitrary function should take in c, which is the number
        of the smallest coin we need to split - call it knuts or cents or whatever.
        Also, as a second argument, it takes the denominations of coins. For example,
        in the US coin case, the denominations will be [25, 10, 5, 1]. In the
        Harry Potter case, it will be [493, 29, 1]. (493 not 17, because everything
        is expressed in terms of the smallest coin).
        The tests below make use of this make_change_arbitrary function to replicate
        the behavior of your specific functions above. Once this generic function
        is implemented correctly, all of the remaining tests should pass.
        """
        out = []

        for d in denominations:
            pass  # Pass means "do nothing". You should replace this expression

        return out

    def dont_repeat_yourself_us(c):
        # Take some time to think about how this function works
        return make_change_arbitrary(c, [25, 10, 5, 1])

    def dont_repeat_yourself_harry_potter(c):
        return make_change_arbitrary(c, [493, 29, 1])

    tester.test(dont_repeat_yourself_us(4), [0, 0, 0, 4], "DRY: 4 cents")
    tester.test(dont_repeat_yourself_us(18), [0, 1, 1, 3], "DRY: 18 cents")
    tester.test(dont_repeat_yourself_us(43), [1, 1, 1, 3], "DRY: 43 cents")
    tester.test(dont_repeat_yourself_us(1585332), [
                63413, 0, 1, 2], "DRY: $15,853.32")

    tester.test(dont_repeat_yourself_harry_potter(5),
                [0, 0, 5], "DRY: 5 knuts")
    tester.test(dont_repeat_yourself_harry_potter(
        182), [0, 6, 8], "DRY: 182 knuts")
    tester.test(dont_repeat_yourself_harry_potter(
        5382), [10, 15, 17], "DRY: 5382 knuts")
    tester.test(dont_repeat_yourself_harry_potter(
        95333), [193, 6, 10], "DRY: 95333 knuts")

    tester.report()

# Everything below this line is not part of the assignment, but feel free to
# poke around.


class Tester(object):
    """This class manages keeping track of the tests. It implements two methods:
    test, which tests a condition, and report, which tells the user the overall
    progress on the assignment.
    The reason these two methods are bound to a class, is to hold onto two variables
    of state: the total number of tests, and the number of tests that passed. Otherwise,
    the report method could not know whether the user had succeeded yet."""

    def __init__(self):
        """Classes need initialization... that's just part of being a class.
        We initialize the state here.
        Class methods always take the class itself as the first argument. By
        convention, we call that argument 'self', although it could be called
        'this' or 'the_class' or such."""
        self.n_tests = 0
        self.n_successes = 0

    def test(self, expected, actual, message):
        self.n_tests += 1
        reason = ""
        if expected == actual:
            state = "passed"
            self.n_successes += 1
        else:
            state = "failed"
            reason = "(Expected %s to equal %s)" % (expected, actual)
        print("Challenge %s: %s: %s" % (self.n_tests, message, state))
        if reason:
            print("\t\t%s" % reason)

    def report(self):
        if self.n_tests == self.n_successes:
            print("Finished all %s tests! Great work!" % self.n_tests)
        else:
            print("Finished %s of %s tests. Keep going." %
                  (self.n_successes, self.n_tests))


assignment()
