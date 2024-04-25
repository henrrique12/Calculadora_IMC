peso = float(input("qual seu peso:"))
altura = float(input("qual sua altura:"))
imc= peso/altura * altura

if imc <18.5:
    print("abaixo do peso:")
elif imc > 18.5 and 24.9:
    print("pesso ideal")
elif imc > 25 and imc < 29.9:
    print("levemente acima do peso")
elif imc > 30 and imc < 34.9:
    print("obesidade grau 1 ")
elif imc > 35 and imc < 39.9:
    print("obsedade grau 2")
elif imc > 40:
    print("obesidade grau 3")