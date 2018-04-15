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

import catex
from mailmerge import MailMerge

class DeviationReport:
    def __init__(self):
        pass

    def makeReport(self, db, template):
        document = MailMerge(template)

        for rule_key in db.keys():
            print(rule_key)
            for did in db[rule_key].keys():
                print(did)
                dev_list = []
                i = 1
                for item in db[rule_key][did]:
                    d = {}
                    d['ListNo'] = i
                    d['FileName'] = item[1]
                    d['FileLine'] = item[2]
                    #t = catex.catex(d['FileName'])
                    #d['FileContent'] = t.catex(d['FileLine'], 1, 1)
                    #t.close()
                    dev_list.append(d)
                    i = i + 1

                document.merge(DR_Title=rule_key, DR_Reviewer="Joohyun", DR_Approver="Lee")
                #document.merge_rows("ListNo", dev_list)
                document.write("result_%s.docx" % (rule_key + did))

