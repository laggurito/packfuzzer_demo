# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

from lib.Controller import Project
from lib.common.banner import RandomBanner
from lib.common.cmdline import CommandLines
from lib.common.readConfig import ReadConfig
import PackerFuzzer
import sys


class Program():
    
    def __init__(self,options):
        self.options = options

    def check(self):
        url = self.options.url
        t = Project(url,self.options)
        t.parseStart()

if __name__ == '__main__':
    sys.argv= ['PackerFuzzer.py', '-u', 'https://www.bountyteam.com/']
    cmd = CommandLines().cmd()
    tt = Program(cmd)
    tt.check()



