import inspect
import platform

def my_help(obj: object):
    print(f"Кастомный help по объекту '{obj}':\n{'-'*40}")
    if hasattr(obj, '__doc__') and obj.__doc__:
        print("Документация: ", obj.__doc__, sep="\n", end="\n\n")
    else:
        print("Документация не найдена\n.")
        
        
    if inspect.isfunction(obj) or inspect.isbuiltin(obj):
        sig = inspect.signature(obj)
        print(f"Сигнатура фнукции: {obj.__name__}{sig}\n")
        
    print("Тип объекта:", type(obj))
    print("Достпупные атрибуты и методы:", ", ".join(dir(obj)))
    print(f"Используемая платформа: {platform.python_implementation()}")
    print("\n\n\n")
    
    
my_help(object)
my_help(eval)

