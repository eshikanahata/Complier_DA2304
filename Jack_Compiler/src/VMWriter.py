class VMWriter:
    def __init__(self, filename):
        self.f = open(filename, 'w')

    def writePush(self, segment, index):
        self.f.write(f"push {segment} {index}\n")

    def writePop(self, segment, index):
        self.f.write(f"pop {segment} {index}\n")

    def writeArithmetic(self, command):
        self.f.write(f"{command}\n")

    def writeLabel(self, label):
        self.f.write(f"label {label}\n")

    def writeGoto(self, label):
        self.f.write(f"goto {label}\n")

    def writeIf(self, label):
        self.f.write(f"if-goto {label}\n")

    def writeCall(self, name, n_args):
        self.f.write(f"call {name} {n_args}\n")

    def writeFunction(self, name, n_locals):
        self.f.write(f"function {name} {n_locals}\n")

    def writeReturn(self):
        self.f.write("return\n")

    def close(self):
        self.f.close()
