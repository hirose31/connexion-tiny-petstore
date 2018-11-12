# -*- coding: utf-8 -*-


def set_of(attr: str=None, data: dict=None):
    return set([d[attr] for d in data])
