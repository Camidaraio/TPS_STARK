#EXPRESIONES REGULARES
#OCURRENCIAS
#search()
import re
texto = ' uno 1 dos 2 tres 3 cuatro'
print(re.search(' ', texto))
#<re.Match object; span=(0, 1), match=' '>
print(re.search('[0-9]+', texto))
#<re.Match object; span=(5, 6), match='1'>
print(re.search('[a-z ]+', texto))
#<re.Match object; span=(0, 5), match=' uno '>

#findall() Busca los espacios en blanco

texto = ' uno 1 dos 2 tres 3 cuatro'
print(re.findall(' ', texto))
#[' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(re.findall('[0-9]+', texto))
#['1', '2', '3']
print(re.findall('[a-z ]+', texto))
#[' uno ', ' dos ', ' tres ', ' cuatro']

#sub()
# Borra abc
result = re.sub('abc',

'', input)

# Repmpaza abc por xyz
result = re.sub('abc', 'xyz', input)

# Eliminalos espacios duplicados
result = re.sub(r'\s+'

, ' ', input)