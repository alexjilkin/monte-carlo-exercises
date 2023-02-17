import math

def vdc(index, base):
  result = 0
  f = 1 / base
  i = index

  while (i > 0):
      f = f / base;
      result += f * (i % base);
      i = math.floor(i / base);

  return result;

vdc_7 = [vdc(i, 7) for i in range(600, 611)]
vdc_11 = [vdc(i, 11) for i in range(600, 611)]

print("Van der Corput sequence for base 7: {} \n base 11: {}".format(vdc_7, vdc_11))