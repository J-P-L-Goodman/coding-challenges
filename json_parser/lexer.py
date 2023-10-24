TOKEN_STRING = 1
TOKEN_NUMBER = 2
TOKEN_TRUE = 3
TOKEN_FALSE = 4
TOKEN_NULL = 5
TOKEN_COLON = 6
TOKEN_COMMA = 7
TOKEN_LBRACE = 8
TOKEN_RBRACE = 9
TOKEN_LBRACKET = 10
TOKEN_RBRACKET = 11


def tokenize(json_str):
    tokens = []

    i = 0
    while i < len(json_str):
        char = json_str[i]
        if char.isspace():
            i += 1
        elif char == "{":
            tokens.append((TOKEN_LBRACE, char))
            i += 1
        elif char == "}":
            tokens.append((TOKEN_RBRACE, char))
            i += 1
        elif char == "[":
            tokens.append((TOKEN_LBRACKET, char))
            i += 1
        elif char == "]":
            tokens.append((TOKEN_RBRACKET, char))
            i += 1
        elif char == ":":
            tokens.append((TOKEN_COLON, char))
            i += 1
        elif char == ",":
            tokens.append((TOKEN_COMMA, char))
            i += 1
        elif char == '"':
            start = i + 1
            i += 1
            while i < len(json_str) and json_str[i] != '"':
                i += 1
            if i < len(json_str):
                tokens.append((TOKEN_STRING, json_str[start:i]))
                i += 1
            else:
                raise ValueError("Unterminated string")
        elif char.isdigit() or char == "-":
            start = i
            i += 1
            while i < len(json_str) and json_str[i].isdigit():
                i += 1
            tokens.append((TOKEN_NUMBER, json_str[start:i]))
        elif json_str[i : i + 4] == "true":
            tokens.append((TOKEN_TRUE, "true"))
            i += 4
        elif json_str[i : i + 5] == "false":
            tokens.append((TOKEN_FALSE, "false"))
            i += 5
        elif json_str[i : i + 4] == "null":
            tokens.append((TOKEN_NULL, "null"))
            i += 4
        else:
            raise ValueError(f"Invalid character: {char}")
    return tokens
