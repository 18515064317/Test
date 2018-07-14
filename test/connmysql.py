#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
from urllib.request import localhost

import aiomysql


def log (sql,args=()):
    logging.log('SQL: %s' % sql)
#为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读
# 把@asyncio.coroutine替换为async；
#把yield from替换为await。
async def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool=await aiomysql.create_pool(
        host=kw.get('host',localhost),
        post=kw.get('port',3306),
        user=kw['root'],
        password=kw['root'],
        db=['test'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize','10'),
        minsize=kw.get('minsize','1'),
        loop=loop
    )
async  def select(sql,args,size=None):
    logging.log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur=await conn.cursor(aiomysql.DictCursor)
        await cur.excute(sql.replace('?','%s'),args or ())
        if size:
            rs=await cur.fetchmany(size)
        else:
            rs=await cur.fetchall()
            await cur.close()
        logging.info('rows returned: %s'%len(rs))
        return rs

