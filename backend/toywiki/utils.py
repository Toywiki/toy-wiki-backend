# coding=utf-8

class Result(dict):
    """
    {
        key1 : value1,
        key2 : value2,
        statuscode : 1,
    }
    """

    def __init__(self):
        super(Result, self).__init__()
        self["statuscode"] = 0

    def setOK(self):
        self["statuscode"] = 1

    def setData(self, key, value):
        self[key] = value
