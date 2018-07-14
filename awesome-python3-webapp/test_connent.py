#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from test.models import User

async def test():
    await test.orm.create_at_pool(user='root',password='root',database='awesome')

    u = User(name='test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

for x in test():
    pass
