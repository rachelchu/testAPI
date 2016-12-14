#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://api.douban.com/v2/book/1220562')
print r.url

#requests安装还没有搞定，本地有装了，需要删除重新安装