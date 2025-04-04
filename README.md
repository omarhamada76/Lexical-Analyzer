A compiler is a program that translates source code from a high-level programming language into machine code, making it executable by a computer. The compilation process consists of several phases, each responsible for a different aspect of translation.
One of the most important phases in a compiler is the Lexical Analysis phase, which scans the source code and converts it into a sequence of tokens. This report provides an implementation of a lexical analyzer that can process a subset of the C++ programming language.

1.1.	Phases 
A compiler operates in multiple phases, including:
1.	Lexical Analysis:
o	Converts source code into tokens (small meaningful units).
o	Detects identifiers, keywords, numbers, operators, and symbols.
2.	Syntax Analysis (Parsing):
o	Checks if the sequence of tokens follows the correct grammar.
o	Constructs a Parse Tree.
3.	Semantic Analysis:
o	Ensures the meaning of expressions is valid.
o	Detects type mismatches and undefined variables.
4.	Intermediate Code Generation:
o	Converts the syntax tree into an intermediate representation.
5.	Code Optimization:
o	Improves efficiency by reducing redundant instructions.
6.	Code Generation:
o	Produces the final machine code for execution.
7.	Error Handling:
o	Detects and reports errors at different compilation stages.


2.	Lexical Analyzer
A Lexical Analyzer (Scanner) is responsible for breaking the input program into tokens. It reads the source code character by character and groups them into meaningful units such as:
•	Keywords: int, float, if, else, while, return
•	Identifiers: Variable names like x, y, myFunction
•	Numbers: Integer and floating-point values like 10, 3.14
•	Strings: "Hello World"
•	Operators: +, -, *, /, =, <, >, <=, >=, ==, !=
•	Special Symbols: {, }, (, ), [, ], ;, ,
3.	Software Tools
To implement the lexical analyzer, we used the following software tools:
3.1.	Computer Program
•  Python 3.x: Used for writing the lexical analyzer.
•  Regular Expressions (re module): Used for pattern matching.
•  Text Editor (VS Code, PyCharm, .): Used for writing and testing the code.

