class Senator:
    def __init__(self, n, senator_id):
        self.n = n
        self.quorum = n / 2 + 1
        self.senator_id = senator_id
        self.laws_list = []
        self.vote = Vote()


class Vote:
    def __init__(self):
        self.is_promise = False
        self.who_promise = -1
        self.promise_law = ""

        self.is_voted = False
        self.who_voted = -1
        self.voted_law = ""

    def promise(self, senator, law):
        if self.is_promise or self.is_voted:
            return False

        self.is_promise = True
        self.who_promise = senator
        self.promise_law = law
        return True

    def vote(self, senator, law):
        if self.is_voted and (self.who_voted is not senator or self.voted_law is not law):
            return False

        self.is_voted = True
        self.who_voted = senator
        self.voted_law = law
        return True
