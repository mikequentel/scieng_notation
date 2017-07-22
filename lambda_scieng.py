# Calculates scientific and engineering formats from input value.

import decimal, math, os, sys

def lambda_handler(event, context):
  sci = None
  eng = None
  input_val = None
  sci_forward_exp = None
  eng_forward_exp = None
  sign = 1

  if event.has_key('input_val'):
    input_val = event['input_val']
  else:
    return

  input_val = float(input_val)

  if input_val == 0.0:
    sci = 0.0
    eng = 0.0
    forward_exp = 1
    # print('input value is zero: %f' % (input_val))
    # print('goodbye!')
    # sys.exit(os.EX_OK)

  if input_val < 0.0:
    sign = -1
  else:
    sign = 1

  absolute_input_val = float(math.fabs(input_val))
  forward_exp = math.floor(math.log10(absolute_input_val))
  backward_exp = math.floor(-1 * forward_exp)
  sci = sign * (absolute_input_val * math.pow(10, backward_exp))
  sci_forward_exp = forward_exp
  eng = sci

  while forward_exp % 3 != 0:
    forward_exp -= 1
    backward_exp = -1 * forward_exp
    eng = sign * (absolute_input_val * math.pow(10, backward_exp))

  eng_forward_exp = forward_exp

  return {"statusCode": 200,"headers":{"Content-Type":"application/json"},"body":[sci, eng, sci_forward_exp, eng_forward_exp]}
