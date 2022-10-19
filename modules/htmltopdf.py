'''
Convertir archivo .html a .pdf

Usar weasyprint - unica opcion
'''
import weasyprint as wp

pdf = wp.HTML('http://www.google.com').write_pdf()

with open('google.pdf', 'wb') as file:
    file.write(pdf)