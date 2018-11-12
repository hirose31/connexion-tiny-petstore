# -*- coding: utf-8 -*-

import sqlalchemy as sa
from sqlalchemy import or_, and_
from sqlalchemy.orm.query import Query
import sqlalchemy_utils as sau
from typing import List, Dict, Union

__version__ = '0.0.1'


def querybuilder(
    query: Query,
    filters: Union[Dict, List[Dict]],
) -> Query:
    """build SQLAlchemy Query object from JSON filter definition

    Args:
        query: sqlalchemy.orm.query.Query
        filters: filter definition

    Returns:
        sqlalchemy.orm.query.Query

    """

    _criterion = _build_criterion(query)

    if isinstance(filters, Dict):
        filters = [filters]

    queries = []

    for _filter in filters:
        _query = query.join()  # dup
        for attr, expr in _filter.items():
            if (not isinstance(expr, dict)) and (not isinstance(expr, list)):
                expr = {'==': expr}

            if isinstance(expr, dict):
                for op, value in expr.items():
                    _query = _query.filter(_criterion(attr, op, value))

            elif isinstance(expr, list):
                boolean_op = expr.pop(0).lower()

                criteria = []
                for e in expr:
                    for op, value in e.items():
                        criteria.append(_criterion(attr, op, value))

                if boolean_op == 'or':
                    _query = _query.filter(or_(*criteria))
                elif boolean_op == 'and':
                    _query = _query.filter(and_(*criteria))
                else:
                    raise ValueError('invalid boolean op: %s' % boolean_op)

            else:
                raise ValueError('invalid expr: %s' % expr)

        queries.append(_query)

    if len(queries) == 1:
        return queries[0]
    else:
        _query = queries.pop(0)
        for q in queries:
            _query = _query.union(q)
        return _query


def _build_criterion(query):
    main_decl_class = None
    decl_class_by_tablename = {}

    # get main decl class and aliases using in query
    for entity in sau.get_query_entities(query):
        if isinstance(entity, sa.orm.util.AliasedClass):
            name = sa.inspect(entity).name
        elif isinstance(entity, sa.orm.Mapper):
            continue
        else:
            name = sau.functions.get_mapper(entity).tables[0].name
            if main_decl_class is None:
                main_decl_class = entity

        decl_class_by_tablename[name] = entity

    # get other decl classes
    base = sau.functions.get_declarative_base(main_decl_class)
    for c in base._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ not in decl_class_by_tablename:
            decl_class_by_tablename[c.__tablename__] = c

    def _criterion(attr, op, value):
        op = op.lower()

        if '.' in attr:
            (tablename, attr) = attr.split('.', maxsplit=1)
            if tablename in decl_class_by_tablename:
                class_attr = getattr(decl_class_by_tablename[tablename], attr, None)
            else:
                raise KeyError('not found declarative class: %s' % tablename)
        else:
            class_attr = getattr(main_decl_class, attr, None)

        if class_attr is None:
            raise AttributeError('main declarative class does not have attribute: %s' % attr)

        if op == '==':
            return class_attr == value
        elif op == '!=':
            return class_attr != value
        elif op == '>=':
            return class_attr >= value
        elif op == '>':
            return class_attr > value
        elif op == '<=':
            return class_attr <= value
        elif op == '<':
            return class_attr < value
        elif op == 'in':
            if not isinstance(value, list):
                value = [value]
            return class_attr.in_(value)
        elif op == '!in':
            if not isinstance(value, list):
                value = [value]
            return ~class_attr.in_(value)
        elif op == 'like':
            return class_attr.like(value)
        elif op == '!like':
            return ~class_attr.like(value)
        else:
            raise ValueError('invalid op: %s' % op)

    return _criterion
