print('welcome')
print('please input command')
while True:
  command = input('>> ')
  if command == 'help':
    print('===========help menu===========')
    print('download [type] [releases]')
  elif command[1] == 'download':
    if command[2] == '':
      pass
