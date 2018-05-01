#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import start_demo
def edits(title,file):
    file_edit=start_demo.edit(title=title,text=file)
    start_demo.db.session.add(file_edit)
    start_demo.db.session.commit()