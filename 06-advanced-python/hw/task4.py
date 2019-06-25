"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы
проверить их корректность
"""
import os
import pytest
import shutil

import task1
import task2
import task3


@pytest.fixture()
def resource():
    path = os.getcwd()+"\\year\\month\\week\\day\\"
    all_path = os.getcwd()+"\\year\\"
    try:
        os.makedirs(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)
    yield all_path
    try:
        shutil.rmtree(all_path)
    except OSError:
        print("Deletion of the directory %s failed" % path)
    else:
        print("Successfully deleted the directory %s" % path)


def test_task1(resource):
    expected = 'V month\n|-> V week\n|   |-> V day\n'
    folder0 = task1.PrintableFolder(resource, os.listdir(resource))
    assert str(folder0) == expected


graph0 = task2.Graph({'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']})
graph1 = task2.Graph({'A': ['B'], 'B': ['C'], 'C': []})
graph2 = task2.Graph({'A': ['C'], 'B': ['A'], 'C': ['B', 'E', 'D'],
                      'D': [], 'E': ['A']})


@pytest.mark.parametrize('graph, expected', [
    (graph0, 'ABCD'),
    (graph1, 'ABC'),
    (graph2, 'ACBED')
])
def test_task2(graph, expected):
    assert list(graph) == list(expected)


a = task3.CeasarSipher()


@pytest.mark.parametrize('input, exp_mess, exp_a_mess', [
    ('abc', 'efg', 'hij'),
    ('hij', 'lmn', 'opq'),
    ('opqrs', 'stuvw', 'vwxyz'),
    ('hellodarknessmyoldfriend',
     'lippshevoriwwqcsphjvmirh',
     'olssvkhyrulzztfvskmypluk')
])
def test_task3(input, exp_mess, exp_a_mess):
    a.message = input
    a.another_message = input
    assert a.message == exp_mess
    assert a.another_message == exp_a_mess
