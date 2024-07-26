#!/usr/bin/env python3
""" LIFO caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching """
    def __init__(self):
        """ Initialize LIFO cache """
        super().__init__()

    def put(self, key, item):
        """ Add item to cache """
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get item from cache """
        if key in self.cache_data:
            return self.cache_data[key]

