
def parse_time(time_str):
  #call time and end it at the end of the function
  seconds = 0
  i = 0
  length = len(time_str)
  num = ''
  while i < length:
    char = time_str[i]
    if str.isdigit(char):
      num += char
    elif char == 'd':
      intNum = int(num)
      seconds += intNum * 86400
      return seconds
      num = ''
    elif char == 'h':
      intNum = int(num)
      seconds += intNum * 3600
      num = ''
    elif char == 'm':
      intNum = int(num)
      seconds += intNum * 60
      num = ''
    elif char == 's':
      intNum = int(num)
      seconds += intNum
      num = ''
    i+=1
  return seconds

def yen_to_int(yen_string):
  yen_stripped = ''
  i = 0
  length = len(yen_string)
  while i < length:
    if yen_string[i].isdigit():
      yen_stripped += yen_string[i]
    i+=1
  return int(yen_stripped)

