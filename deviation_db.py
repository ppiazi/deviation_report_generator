# -*- coding: utf-8 -*-
"""
Copyright 2018 Joohyun Lee(ppiazi@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from collections import defaultdict

class DeviationDB:
    def __init__(self):
        self._db = {}

    def insert(self, deviationComment, filename, line):
        key0 = deviationComment.getStandard()
        key1 = deviationComment.getRuleID()
        key2 = deviationComment.getDeviationID()

        if not key0 in self._db.keys():
            self._db[key0] = {}

        if not key1 in self._db[key0].keys():
            self._db[key0][key1] = {}

        if not key2 in self._db[key0][key1].keys():
            self._db[key0][key1][key2] = []

        self._db[key0][key1][key2].append((deviationComment, filename, line))

    def printAll(self):
        for key0 in self._db.keys():
            for key1 in self._db[key0].keys():
                for key2 in self._db[key0][key1].keys():
                    for item in self._db[key0][key1][key2]:
                        print("%s %s %s %s %s" % (key0, key1, key2, item[1], item[2]))

    def getDB(self, standard):
        return self._db[standard]

class DeviationComment:
    def __init__(self, comment, sep = "#", style="C"):
        self.comment = comment
        self._sep = sep
        self._style = style

        self._parse(self.comment)

    def _parse(self, comment):
        c = comment.replace("/*", "")
        c = comment.replace("*/", "")
        c = c.strip()

        tokens = c.split(self._sep)
        self._standard = tokens[1].strip()
        self._rule_id = tokens[2].strip()
        self._deviation_id = tokens[3].strip()
        self._desc = tokens[4].strip()

    def getStandard(self):
        return self._standard

    def getRuleID(self):
        return self._rule_id

    def getDeviationID(self):
        return self._deviation_id

    def getDesc(self):
        return self._desc
