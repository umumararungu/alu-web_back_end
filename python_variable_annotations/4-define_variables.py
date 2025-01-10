#!/usr/bin/env python3
'Define variables'


a = 1,
pi = 3.14,
i_understand_annotations = True,
school = "Holberton"

def define_variable(a: int, pi: float, i_understand_annotations: bool, school: str):
    'Return default value'

    a = a
    pi = pi
    i_understand_annotations = i_understand_annotations
    school = school

    return a, pi, i_understand_annotations, school
