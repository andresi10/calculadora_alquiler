print('\n')
print('Bienvenido a mi calculadora de alquileres.')
print('------------------------------------------')
print('Vicente López --- ')
print('Inicio de contrato 1 de Marzo 2024. Ajuste trimestral por IPC')
print('Valor Inicial:                  $330.000')
print('Valor actualizado a Junio:      $415.300 (25.86%)')
print('Valor actualizado a Septiembre: $470.800 (12.8%)')
print('Valor actualizado a Diciembre:  $511.460 (8.6%)')
print('Valor actualizado a Marzo:      $549.710 (7.3%)')

#Para llegar al 25.84 = 1.11*1.088*1.042 (25.84), mas redondo 25.85
print('Próxima actualización: Marzo 25')
#print('\n')
print('------------------------------------------')

#ipc1 = float(input('IPC de Junio: '))/100 +1
ipc1 = 1.027 #2.7%
print('El IPC de Diciembre informado es de 2.7 %')
ipc2 = 1.022 #2.2%
print('El IPC de Enero informado    es de 2.2 %')
#ipc3 = float(input('IPC de Febrero (aún no publicado): '))/100 +1
ipc3 = 1.024 #2.4%
print('El IPC de Febrero informado es de 2.4 %')
ipc1EnPor = (ipc1-1)*100
ipc2EnPor = (ipc2-1)*100
ipc3EnPor = (ipc3-1)*100
sumaPor = ipc1EnPor + ipc2EnPor + ipc3EnPor

#print('\n')
print(f'                         Acumulado = {round(sumaPor,2)} %')

#print('\n')

alquiler = 511460
inflacionAcumulada = ((ipc1*ipc2*ipc3)-1)*100
aumento = round(alquiler * inflacionAcumulada /100 ,2)
nuevoValor = round(alquiler + aumento ,2)

print('------------------------------------------')
print(f'El alquiler era de ${alquiler}. El aumento de ${aumento}')
print('\n')
print('   -----------------------------------------')

print(f'|| El nuevo monto a abonar es de: ${nuevoValor}  ||')
print('   -----------------------------------------')
print('\n')
print('Gracias por utilizar mi programa.')
input('                                 @andresi10     ')

"""Podria hacer mas sencillo
nuevoValor = round(alquiler*ipc1*ipc2*ipc3,2)
aumento = nuevoValor - alquiler"""
