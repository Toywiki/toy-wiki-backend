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
        self["statuscode"] = -1

    def setOK(self):
        self["statuscode"] = 0

    def setStatuscode(self, status):
        self["statuscode"] = status

    def setData(self, key, value):
        self[key] = value

    def setStatusCode(self, status_code):
        self["statuscode"] = status_code
