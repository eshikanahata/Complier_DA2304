import re

class JackTokenizer:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            code = f.read()
        code = re.sub(r'//.*', '', code) 
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL) 
        keywords = r'\b(?:class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return \b'
        symbols = r'[\{\}\(\)\[\]\.\,\;\+\-\*\/\&\|\<\>\=\~]'
        integer = r'\d+'
        string = r'"[^"\n]*"'
        identifier = r'[A-Za-z_][A-Za-z0-9_]*'
        token_pattern = re.compile(
            f'(?P<KEYWORD>{keywords})|'
            f'(?P<SYMBOL>{symbols})|'
            f'(?P<INT_CONST>{integer})|'
            f'(?P<STRING_CONST>{string})|'
            f'(?P<IDENTIFIER>{identifier})'
        )
        self.tokens = []
        for match in token_pattern.finditer(code):
            for t_type, t_val in match.groupdict().items():
                if t_val is not None:
                    if t_type == 'STRING_CONST':
                        t_val = t_val[1:-1] 
                    self.tokens.append((t_type, t_val))
                    break       
        self.id = -1
        self.token = None

    def hasMoreTokens(self):
        return self.id + 1 < len(self.tokens)

    def advance(self):
        if self.hasMoreTokens():
            self.id += 1
            self.token = self.tokens[self.id]

    def tokenType(self):
        return self.token[0]

    def keyword(self):
        return self.token[1]

    def symbol(self):
        return self.token[1]

    def identifier(self):
        return self.token[1]

    def intVal(self):
        return int(self.token[1])

    def stringVal(self):
        return self.token[1]

def escape_xml(val):
    escapes = {'<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;'}
    return escapes.get(val, val)
