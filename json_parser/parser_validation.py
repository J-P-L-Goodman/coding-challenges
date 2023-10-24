from lexer import (
    tokenize,
    TOKEN_COLON,
    TOKEN_COMMA,
    TOKEN_FALSE,
    TOKEN_LBRACE,
    TOKEN_LBRACKET,
    TOKEN_NULL,
    TOKEN_NUMBER,
    TOKEN_RBRACE,
    TOKEN_RBRACKET,
    TOKEN_STRING,
    TOKEN_TRUE,
)


def is_valid_json(json_str):
    try:
        tokens = tokenize(json_str)
        stack = []
        last_token_type = None
        for token_type, value in tokens:
            if token_type in {TOKEN_LBRACE, TOKEN_LBRACKET}:
                stack.append(token_type)
            elif token_type in {TOKEN_RBRACE, TOKEN_RBRACKET}:
                if not stack or stack[-1] != token_type - 1:
                    return False
                stack.pop()

            if last_token_type:
                if last_token_type == TOKEN_COMMA or last_token_type == TOKEN_COLON:
                    if (
                        token_type == TOKEN_LBRACE
                        or token_type == TOKEN_RBRACE
                        or token_type == TOKEN_LBRACKET
                        or token_type == TOKEN_RBRACKET
                        or token_type == TOKEN_COLON
                        or token_type == TOKEN_COMMA
                    ):
                        return False
            last_token_type = token_type
        return not stack
    except ValueError:
        return False
