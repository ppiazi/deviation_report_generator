# -*- coding: utf-8 -*-
"""
Copyright 2015 Joohyun Lee(ppiazi@gmail.com)

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
import getopt

__author__ = 'ppiazi'
__version__ = 'v0.0.2'

CODE_FORMATTER = "%s : %s"

def print_usage():
    """
    사용법에 대한 내용을 콘솔에 출력한다.
    :return:
    """
    print("catex.py [options] [files_name]")
    print("    Version %s" % __version__)
    print("    Options:")
    print("    -f : set target file")
    print("    -s : set start line number")
    print("    -u : set upper bound")
    print("    -l : set lower bound")

class catex:
    def __init__(self, file_name):
        self.file_name = file_name
        self._code = ""

        try:
            self.file_handle = open(self.file_name, "r", encoding='utf-8')
        except Exception as e:
            self.file_handle = None
            print(str(e))
            self._code = str(e)
            return 1

    def catex(self, line_number_s, line_number_u=0, line_number_l=0):
        if self.file_handle == None:
            print("File handle closed.")
            return None

        self.line_number_s = line_number_s
        self.line_number_u = line_number_u
        self.line_number_l = line_number_l

        lines = self.file_handle.readlines()
        line_total_num = len(lines)

        # get line_start and line_end
        line_start = self.line_number_s - self.line_number_u
        line_end = self.line_number_s + self.line_number_l

        if line_start <= 0:
            line_start = 1
        if line_end > line_total_num:
            line_end = line_total_num

        # calculate 0 padding level
        rfill_num =len(str(line_end)) + 1

        for line_num in range(line_start - 1, line_end):
            # make line number string
            line_num_str = str(line_num + 1).zfill(rfill_num)

            # make formatted code string
            temp_code = CODE_FORMATTER % (line_num_str, lines[line_num])
            self._code = self._code +temp_code

        return self._code

    def close(self):
        if self.file_handle == None:
            return -1

        self.file_handle.close()

    def get_code(self):
        return self._code

if __name__ == "__main__":
    optlist, args = getopt.getopt(sys.argv[1:], "s:u:l:f:")

    file_name = ""
    line_number_s = 1
    line_number_u = 0
    line_number_l = 0

    for op, p in optlist:
        if op == "-s":
            try:
                line_number_s = int(p)
            except Exception as e:
                print(str(e))
                os._exit(1)
        elif op == "-u":
            try:
                line_number_u = int(p)
            except Exception as e:
                print(str(e))
                os._exit(1)
        elif op == "-l":
            try:
                line_number_l = int(p)
            except Exception as e:
                print(str(e))
                os._exit(1)
        elif op == "-f":
            file_name = p
        else:
            file_name = op
            print("Invalid Argument : %s / %s" % (op, p))

    if file_name == "":
        print_usage()
        os._exit(1)

    t_catex = catex(file_name)
    code = t_catex.catex(line_number_s, line_number_u, line_number_l)
    print(code)
    t_catex.close()
