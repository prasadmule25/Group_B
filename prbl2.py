# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]
#
#   return str1
#
# print(change_char('restart'))

def chnage_char(str1):
  char=str1[0]
  str1=str1.replace(char,"$")
  str1=char + str1[1:]

  return str1
print(chnage_char("hello spastic, how r u?"))