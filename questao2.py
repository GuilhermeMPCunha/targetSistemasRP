numero_str = input("Digite um numero: ")
numero = int(numero_str)

anterior = 0
proximo = 1
soma = 1
fib = []




while(soma<numero):
    soma = proximo + anterior
    anterior = proximo
    proximo = soma
    fib.append(soma)
    
print (fib)

if numero in fib:
    print("numero informado pertence a sequencia Fibonacci ")

else:
    print("numero informado nao pertence a sequencia Fibonacci ")