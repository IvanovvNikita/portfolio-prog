import numpy as np


class MathStats():

    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._combine = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        self._disp = None
        self._sigma_sq = None
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)
        for d in self._data:
            self._combine.append(d['Online'])
            self._combine.append(d['Offline'])

    @property
    def data(self):
        return self._data

    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """

        sums = {'offline': 0, 'online': 0}
        for _l in data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        self._mean = (sums['offline'] / len(data), sums['online'] / len(data))

        return self._mean

    @property
    def max(self):
        self._max = np.max(self._combine)
        return self._max

    @property
    def min(self):
        self._min = np.min(self._combine)
        return self._min

    @property
    def disp(self):
        self._disp = np.var(self._combine)
        return self._disp

  
    @property
    def sigma_sq(self):
        self._sigma_sq = np.std(self._combine)
        return self._sigma_sq
