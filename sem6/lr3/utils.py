import functools
import json
import os


class Memoize:
    def __init__(self):
        self.cache = {}

    def load_cache(self, path):
        if not os.path.isfile(path):
            return
        try:
            with open(path,) as f:
                self.cache = dict(json.load(f))
        except json.JSONDecodeError:
            self.cache = {}

    def dump_cache(self, path):
        with open(path, 'w') as f:
            json.dump(self.cache, f)

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = self._generate_key(func.__name__, args, kwargs)
            if key not in self.cache:
                self.cache[key] = func(*args, **kwargs)
            return self.cache[key]

        return inner

    @staticmethod
    def _generate_key(name, args, kwargs):
        return str((name, args, str(kwargs)))