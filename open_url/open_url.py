#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import webbrowser

if len(sys.argv) < 2:
    print('Usage: python open_url.py [url_key]')
    sys.exit()

url_key = sys.argv[1]
print(url_key)
webbrowser.open(url_key)


