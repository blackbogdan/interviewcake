# requests,
# http methods


# void addKey(String)
# void removeKeyWithMaxCount()
# int getCountForKey(String)
# string getKeyWithMaxCount()

# addKey('a'); getCountForKey('a') -> 1; getKeyWithMaxCount() -> 'a'; getCountForkey('a') -> ???
class test_class():
    def __init__(self):
        self.d = {}

    # {'cat':2}
    def addKey(self, String):
        self.d[String] = self.d.get(String, 0) + 1

    def getCountForKey(self, String):
        return self.d.get(String, None)

    def getKeyWithMaxCount(self):
        keys = self.d.keys()
        values = self.d.values()
        return keys[values.index(max(values))]

    def removeKeyWithMaxCount(self):
        del self.d[self.getKeyWithMaxCount()]
