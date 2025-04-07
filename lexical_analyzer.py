import re

# Define token types for C++
TOKEN_TYPES = {
    "KEYWORD": r"\b(int|float|if|else|while|for|return|void|char|string|double)\b",
    "IDENTIFIER": r"\b[a-zA-Z_][a-zA-Z0-9_]*\b",
    "NUMBER": r"\b\d+(\.\d+)?\b",
    "STRING": r'"[^"]*"',  # Matches anything inside double quotes
    "OPERATOR": r"[+\-*/=<>!]+",
    "SPECIAL_SYMBOL": r"[{}()\[\],;]",
}

def lexical_analyzer(code):
    tokens = []

    # Combine regex patterns
    combined_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES.items())

    for match in re.finditer(combined_regex, code):
        token_type = match.lastgroup
        lexeme = match.group(token_type)
        tokens.append((lexeme, token_type))

    return tokens

# Sample C++ code as a string 
cpp_code = """
int main() {
    int x =3;
    for(int i =0; i<3;i++){
    x++;
    }
    cout<<x;
    return 0;
}
"""


tokens = lexical_analyzer(cpp_code)


print("\nTokens:")
for lexeme, token_type in tokens:
    print(f"{lexeme} --> {token_type}")
