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
        self._title = ""
        self._writer = ""
        self._reviewer = ""
        self._approver = ""

    def setReportInfo(self, report_info):
        self._title = report_info['title']
        self._writer = report_info['writer']
        self._reviewer = report_info['reviewer']
        self._approver = report_info['approver']

    def makeReport(self, db, template):

        for rule_key in db.keys():
            print(rule_key)
            for did in db[rule_key].keys():
                document = MailMerge(template)
                print(did)
                dr_list = []
                i = 1
                for item in db[rule_key][did]:
                    d = {}
                    d['ListNo'] = str(i)
                    d['FileName'] = item[1]
                    d['FileLine'] = str(item[2])
                    t = catex.catex(d['FileName'])
                    d['FileContent'] = t.catex(item[2], 1, 1)
                    t.close()
                    dr_list.append(d)
                    i = i + 1


                document.merge(DR_Rule_Title=rule_key,
                               DR_Rule_Category=did,
                               DR_Reviewer=self._reviewer,
                               DR_Approver=self._approver,
                               DR_Writer=self._writer)
                document.merge_rows("ListNo", dr_list)
                document.write("result_%s.docx" % (rule_key + did))
                document.close()

