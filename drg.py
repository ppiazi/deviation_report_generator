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
import sys
import os
import os.path
import getopt
import deviation_db
import deviation_report

__version__ = "0.0.1"
DR_PATTERN_START = "/* DR"
DR_SEPARATOR = "#"

class DeviationReportGenerator:
    def __init__(self, target_folder):
        self.target_folder = target_folder

    def searchDR(self):
        self.drd = deviation_db.DeviationDB()

        for (root, _, files) in os.walk(self.target_folder):
            print("Entering %s " % (root))

            for afile in files:
                full_file_path = os.path.join(root, afile)
                self._searchPatternInFile(full_file_path)

        self.drd.printAll()

    def _searchPatternInFile(self, afile):
        print("Reading %s " % (afile))
        f = open(afile, "r", encoding="utf-8")
        lines = f.readlines()

        i = 0
        for aline in lines:
            if DR_PATTERN_START in aline:
                print("Found Deviation Comment")
                dc = deviation_db.DeviationComment(aline)
                line = self._findDeviationLine(lines[i:])

                print("INFO %s %d" % (afile, line + i + 1))
                self.drd.insert(dc, afile, line + i + 1)

            i = i + 1

    def makeReport(self, standard, template, report_info):
        dr = deviation_report.DeviationReport()
        dr.setReportInfo(report_info)
        dr.makeReport(self.drd.getDB(standard), template)


    def _findDeviationLine(self, lines):
        line = 0

        for aline in lines:
            t = aline.strip()

            if t == "" or t.startswith("/*") or t.endswith("*/") or t.startswith("//"):
                line = line + 1
                continue
            break

        return line

def print_usage():
    """
    사용법에 대한 내용을 콘솔에 출력한다.
    :return:
    """
    print("dgr.py [-f <folder>]")
    print("    Version %s" % __version__)
    print("    Options:")
    print("    -f : (mandatory) set a target folder")

if __name__ == "__main__":
    optlist, args = getopt.getopt(sys.argv[1:], "f:")

    p_folder = None

    for op, p in optlist:
        if op == "-f":
            p_folder = p
        else:
            print("Invalid Argument : %s / %s" % (op, p))

    if p_folder == None:
        print_usage()
        os._exit(-1)

    report_info = {}
    report_info["title"] = "이주현"
    report_info["writer"] = "이주현"
    report_info["reviewer"] = "홍길동"
    report_info["approver"] = "신사임당"

    drg = DeviationReportGenerator(p_folder)

    drg.searchDR()

    drg.makeReport("MISRA C:2012", "template.docx", report_info)


