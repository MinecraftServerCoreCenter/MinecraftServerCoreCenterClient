print('welcome')
print('please input command')
while True:
  command = input('>> ')
  if command[:4] == 'help':
    print('===========help menu===========')
    print('download [type] [releases]')
  elif command[0] == 'download':
    if command[1] == '':
      pass
