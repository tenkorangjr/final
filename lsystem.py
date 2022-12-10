"""
Name: Michael Tenkorang
Project: 8
Course: CS151
Section: A
Date: 26 November 2022

Version 2
"""

import sys


class Lsystem:
    def __init__(self, filename=None):
        """Initializer of class Lsystem"""
        self.filename = filename
        self.base = ''
        self.rules = []

        if self.filename:
            self.read(filename)

    def getBase(self):
        """Returns the base of the lsystem"""
        return self.base

    def setBase(self, b):
        """Returns the base of the lsystem"""
        self.base = b

    def getRule(self, i):
        """Returns the base of the lsystem"""
        return self.rules[i:]

    def addRule(self, newrule):
        """Returns the base of the lsystem"""
        self.rules.append(newrule)

    def numRules(self):
        """Returns the base of the lsystem"""
        return len(self.rules)

    def read(self, filename):
        """Returns the base of the lsystem"""
        self.rules = []

        with open(file=filename, mode="r") as file:
            data = file.readlines()

            for line in data:
                line = line.strip()
                words = line.split(" ")

                if words[0] == 'base':
                    self.setBase(words[1])

                elif words[0] == 'rule':
                    self.addRule(words[1:])

    def replace(self, istring):
        """Returns the base of the lsystem"""

        tstring = ''
        for char in istring:
            found = False
            for rule in self.rules:
                if rule[0] == char:
                    tstring += rule[1]
                    found = True
                    break
            if not found:
                tstring += char
        return tstring

    def buildString(self, iterations):
        """Returns the base of the lsystem"""
        nstring = self.base
        for _ in range(iterations):
            nstring = self.replace(nstring)
        return nstring


def main(argv):
    """Function to test lsystem files"""
    if len(argv) < 2:
        print('Usage: lsystem.py <filename>')
        exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read(filename)

    print(lsys)
    print(lsys.getBase())

    for i in range(lsys.numRules()):
        rule = lsys.getRule(i)
        print(rule[0] + ' -> ' + rule[1])

    lstr = lsys.buildString(iterations)
    print(lstr)


if __name__ == "__main__":
    main(sys.argv)
