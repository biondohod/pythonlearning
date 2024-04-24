def  meow(n: int) -> None:
    for _ in range(n):
        print("meow")

    
# PS C:\Web\pythonlearning> mypy mypy.py
# mypy.py:7: error: Argument 1 to "meow" has incompatible type "str"; expected "int"  [arg-type]
number: int = input("Number: ")
# PS C:\Web\pythonlearning> mypy mypy.py
# mypy.py:7: error: Argument 1 to "meow" has incompatible type "str"; expected "int"  [arg-type]
meows: str = meow(number)
print(meows)