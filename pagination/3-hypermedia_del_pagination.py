#!/usr/bin/env python3
""" 3. Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict, Any


class Server:
    """ Server class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset function
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexed by sorting position, starting at 0 function
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Returns a dictionary.(funtion)
        """
        assert type(index) == int
        assert type(page_size) == int
        csv = self.indexed_dataset()
        csv_size = len(csv)
        assert 0 <= index < csv_size
        data = []
        _next = index
        for _ in range(page_size):
            while not csv.get(_next):
                _next += 1
            data.append(csv.get(_next))
            _next += 1
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": _next
        }
