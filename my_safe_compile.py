def safe_evaluate(str_code_expr: str, variables: dict):
    """
    Безопасное выполнение кода с помощью compile().
    :param str_code_expr: Строка c кодом выражения Python для выполнения.
    :param variables: словарь с разрешенными переменными.
    """
    
    compiled_code = compile(str_code_expr, "<string>", "eval")
    print("Байт-код: ", compiled_code.co_code)
    safe_globals = {"__builtins__": {}}
    safe_locals = variables
    
    try:
        result = eval(compiled_code, safe_globals, safe_locals)
        return result
    except Exception as e:
        return f"Ошибко выполнения {e}"
    
if __name__ == "__main__":
    code = "a+b"
    allowed_vars = {
        "a": 22,
        "b": 30,
    }
    
    print(f"Результат выполнения: {code}, при {allowed_vars}: ", safe_evaluate(code, allowed_vars))
    malicious_code = "__import__('os').system('echo malicious code')"
    print(f"Результат выполнения потенциально вредоносного кода: ", safe_evaluate(malicious_code, allowed_vars))