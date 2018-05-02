#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import start_demo
def search_keyword(keyword):
    list1=start_demo.text.query.filter_by(title=keyword).all()
    return list1