#!/usr/bin/python3
# -*- coding:utf-8 –*-

import os
import platform


if platform.system() == "Windows":
    os.environ['http_proxy'] = "http://127.0.0.1:1080"
    os.environ['https_proxy'] = "http://127.0.0.1:1080"
else:
    os.environ['http_proxy'] = "socks5h://127.0.0.1:1080"
    os.environ['https_proxy'] = "socks5h://127.0.0.1:1080"
