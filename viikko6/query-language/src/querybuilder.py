from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or


class QueryBuilder:
    def __init__(self, matcher=And()):
        self.matcher = matcher

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(self.matcher, value, attr))

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(self.matcher, matcher1, matcher2))

    def build(self):
        return self.matcher

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self.matcher, team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(self.matcher, value, attr))