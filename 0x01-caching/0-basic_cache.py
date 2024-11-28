#!/usr/bin/env python3
"""class BasicCache that inherits from BaseCaching
and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class that inherit from basecaching"""

    def put(self, key, item):
        """assign the item value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to the key"""
        if key:
            return self.cache_data.get(key, None)
