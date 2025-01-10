#!/usr/bin/env python3
'Define variables'


a = 1
pi = 3.14
i_understand_annotations = True
school = "Holberton"


def define_variable(a: int = 1, pi: float = 3.14,
    i_understand_annotations: bool = True,
    school: str = "Holberton"):
    'Return default value'

    a = a
    pi = pi
    i_understand_annotations = i_understand_annotations
    school = school

    return a, pi, i_understand_annotations, school
