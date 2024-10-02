
while True:
  numero = int(input("Informe um numero:"))
  if numero == -1:
     print("Encerramento do programa")
     break

  a, b = 0, 1
  numero_sequencia = [a, b]

  while b < numero:
    a,b = b, a + b
    numero_sequencia.append(b)

    

  if numero in numero_sequencia:
       print(f"O numero {numero} pertence a sequencia de Fibonacci")

  else:

      print(f"O numero {numero} não pertence a sequencia de Fibonacci")