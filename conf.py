# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "imxiaolong/site-blog@gh-pages"
}

# 站点设置
site_name = "老张博客"
site_logo = "${static_prefix}dragon-png.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "老张"
email = "myaceact@outlook.com"
author_homepage = "https://www.aceact.com"
description = "知易行难，知行合一"
key_words = ['英语', '生活', '管理', '日常']
language = 'zh-CN'
external_links = [
    
    {
        "name": "ACEACT.COM",
        "url": "https://www.aceact.com",
        "brief": "管理学习笔记"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/imxiaolong",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/imxiaolong",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/imxiaolong/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
