import math

# Returns the member of a VDC sequence at index with base
def vdc(index, base):
  result = 0
  denom = 1
  while index > 0:
    denom *= base
    index, remainder = divmod(index, base)
    result += float(remainder) / denom
    
  return result

def main():
  vdc_7 = [vdc(i, 7) for i in range(600, 611)]
  vdc_11 = [vdc(i, 11) for i in range(600, 611)]

  print("Van der Corput sequence for base 7: {} \n base 11: {}".format(vdc_7, vdc_11))

# main()