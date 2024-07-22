#!/usr/bin/env python3
""" Pagination """

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing a start index
    and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """ Server class to paginate a database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_F)
