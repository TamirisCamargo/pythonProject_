def myMethod(param3, param2, param1=str, param4=None):
    print(param1, param2, param3)

    soma = int(param2) + int(param3)
    print(soma)

    result = {
        "param1": param1,
        "param2": param2,
        "param3": param3,
        "Soma": soma
    }
    print(result)
    return result


myMethod(30, 50, "Teste", 444)









