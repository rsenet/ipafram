#!/usr/bin/env python3
from lib import parser
import argparse
import sys
import os

__author__  = 'Regis SENET'
__email__   = 'regis.senet@orhus.fr'
__git__     = 'https://github.com/rsenet/ipafram'
__version__ = '0.1'
__license__ = 'GPLv3'
__pyver__   = '%d.%d.%d' % sys.version_info[0:3]
short_desc  = "Android Framework Identifier"

arg_parser = argparse.ArgumentParser(description=short_desc)
arg_parser.add_argument('--file', help="Specify your IPA file")
u_args = arg_parser.parse_args()

# Get variable
apkFile = u_args.file

try:
    if apkFile:
        if os.path.exists(apkFile):
            name, extension = os.path.splitext(apkFile)

            if ".ipa" in extension:
                parser.get_result(apkFile)

            else:
                print("[x] Error! Only IPA files are allowed")

        else:
            print("[x] Error! File '%s' not found" % apkFile)

    else:
        print("[x] Error! Missing attribute ('file' is mandatory)")

except KeyboardInterrupt:
    print("\n[x] Leaving ...")
