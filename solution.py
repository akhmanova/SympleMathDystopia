#!/usr/bin/env python3

from sys import stdout

class ProposalInput:
  def __init__(self, law):
    self.law = law

class QueryInput:
  def __init__(self):
    pass

class PingInput:
  def __init__(self):
    pass

#To be extended by our custom input messages
class CommunicationInput:
  def __init__(self, source, payload):
    self.source = source
    self.payload = payload

class NoResultOutput:
  def __init__(self, source):
    pass

class ResultOutput:
  def __init__(self, result):
    self.result = result

#To be extended by our custom output messages
class CommunicationOutput:
  def __init__(self, target, payload):
    self.target = target
    self.payload = payload



class Senator:
    def __init__(self, n, senator_id):
        self.n = n
        self.quorum = n / 2 + 1
        self.senator_id = senator_id
        self.laws_list = []
        self.vote = Vote()
        self.promise_time = 0
        self.vote_attempts = 0

    def start_vote(self):
        pass

    def send_vote(self):
        pass

    def get_propose(self):
        pass

    def get_query(self):
        pass


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
        if self.is_voted and (self.who_voted is not senator or self.voted_law is not law)\
                or self.is_promise and(self.who_promise is not senator or self.voted_law is not law):
            return False

        self.is_voted = True
        self.who_voted = senator
        self.voted_law = law
        return True


def parse_input(line):
  if line.startswith("PROPOSE"):
    return ProposalInput(line[len("PROPOSE "):])
  if line.startswith("QUERY"):
    return QueryInput()
  if line.startswith("PING"):
    return PingInput()

  si = line.index(' ')
  source = int(line[:si])
  return CommunicationInput(source, line[si + 1:])


def main():
    idx = input().split(' ')
    senator = Senator(int(id([0])), int(idx[1]) - 1)

    while True:
        parcedInput = parse_input(input())

if __name__ == '__main__':
    main()
