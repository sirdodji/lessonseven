def convert(numb, temp):
    if temp == "c":
        convertedf = (numb * 9 / 5) + 32
        convertedk = (numb + 273)
        print('%d C' % (numb))
        print('%d C = %d F' % (numb, convertedf))
        print('%d C = %d K' % (numb, convertedk))
    elif temp == "f":
        converted = (numb - 32) * 5 / 9 + 273
        convertedk = (numb + 273)
        print('%d F' % (numb))
        print('%d F = %d C' % (numb, converted))
        print('%d F = %d K' % (numb, convertedk))
    elif temp == "k":
        converted = numb - 273
        convertedf= (numb - 273) * 9 / 5 + 32
        print('%d K' % (numb))
        print('%d K = %d C' % (numb, converted))
        print('%d K = %d F' % (numb, convertedf))
    else:
        print("Error, type C or F for Celsius or Fahrenheit conversions.")

convert(0, 'c')
convert(0, 'f')
convert(0, 'k')