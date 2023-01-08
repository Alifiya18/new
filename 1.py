import tabula 
myfile = '2.pdf'
mytable = tabula.read_pdf(myfile, pages = 2)
print (mytable[0])
tabula.convert_into(myfile, 'table.csv', pages = 2)
print('Создан файл формата csv')
