class SymbolTable:
    def __init__(self):
        self.class_table = {}
        self.sub_table = {}
        self.counts = {"static": 0, "field": 0, "argument": 0, "var": 0}

    def startSubroutine(self):
        self.sub_table = {}
        self.counts['argument'] = 0
        self.counts['var'] = 0

    def define(self, name, type_name, kind):
        entry = {'type': type_name, 'kind': kind, 'index': self.counts[kind]}
        if kind == "static" or kind == "field":
            self.class_table[name] = entry
        else:
            self.sub_table[name] = entry
        self.counts[kind] += 1

    def varCount(self, kind):
        return self.counts.get(kind, 0)

    def kindOf(self, name):
        if name in self.sub_table:
            return self.sub_table[name]['kind']
        if name in self.class_table:
            return self.class_table[name]['kind']
        return None

    def typeOf(self, name):
        if name in self.sub_table:
            return self.sub_table[name]['type']
        if name in self.class_table:
            return self.class_table[name]['type']
        return None

    def indexOf(self, name):
        if name in self.sub_table:
            return self.sub_table[name]['index']
        if name in self.class_table:
            return self.class_table[name]['index']
        return None

    def segmentOf(self, name):
        kind = self.kindOf(name)
        if kind == "field":
            return "this"
        if kind == "var":
            return "local"
        return kind
