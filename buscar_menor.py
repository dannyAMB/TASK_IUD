array_lluvia = {
1967: {"enero":54, "febrero":25.5, "marzo":128, "abril":156.1, "mayo":207.1, "junio":314.5, "julio":217.5, "agosto":240.1, "septiembre":109.1, "octubre":77.5, "noviembre":280.2, "diciembre":51.1},

1977: {"enero":0, "febrero":35, "marzo":85, "abril":107, "mayo":82.1, "junio":224, "julio":430.5, "agosto":144, "septiembre":339.5, "octubre":192, "noviembre":401.5, "diciembre":88},

1987: {"enero":27, "febrero":55, "marzo":71.9, "abril":77.4, "mayo":139.1, "junio":81.7, "julio":82.6, "agosto":130.5, "septiembre":78.8, "octubre":102.6, "noviembre":57.4, "diciembre":63.1},

1997: {"enero":79.6, "febrero":59.7, "marzo":38.8, "abril":81, "mayo":111.4, "junio":83.9, "julio":201.8, "agosto":108.1, "septiembre":57.9, "octubre":73, "noviembre":77.5, "diciembre":5},

2007: {"enero":0, "febrero":32.7, "marzo":95.4, "abril":128.2, "mayo":88.3, "junio":223.7, "julio":57.9, "agosto":128.2, "septiembre":58.5, "octubre":147.8, "noviembre":77.3, "diciembre":127.2},

2017: {"enero":119.1, "febrero":57.8, "marzo":210.7, "abril":66.6, "mayo":170.8, "junio":189.5, "julio":190, "agosto":132.8, "septiembre":52.2, "octubre":140.4, "noviembre":92.7, "diciembre":102.5}
}

print("1. El promedio anual de precipitación en el Lago para cada año presentado en la tabla:")
print("Año  | Promedio")

for year, meses in array_lluvia.items():
    suma = 0
    cont = 0

    for mes, valor in meses.items():
        suma += valor
        cont += 1

        promedio = suma / cont
        promedio = int(promedio * 100) / 100
    print(year, "|", promedio)

print("  ")
print("2. El promedio mensual de precipitación en el Lago para cada mes presentado en la tabla")
print("Meses  | Promedio")

array_meses_sumados={}
for year, meses in array_lluvia.items():
    cont+=1

    for mes, valor in meses.items():
        if mes not in array_meses_sumados:
           array_meses_sumados[mes] = 0
        array_meses_sumados[mes]+= valor

for mes, value in array_meses_sumados.items():
    promedio = value/cont
    promedio = int(promedio * 100) / 100

    print(mes,": ", promedio)

print("  ")
print("3.El mes y año que registra menor precipitación:")


array_meses_lluvia_minima = {}

for year, meses in array_lluvia.items():
  mes_menor = ""
  menor_valor = float("inf")

  for mes, valor in meses.items():


      if valor <= menor_valor:
           menor_valor = valor
           mes_menor = mes

  array_meses_lluvia_minima[year] = (mes_menor, menor_valor)

valor_min_aux= float("inf")

for year, (mes, valor) in array_meses_lluvia_minima.items():
       
        if valor < valor_min_aux:
           valor_min_aux = valor
           year_menor = year
           mes_menor= mes

print(year_menor," y ",mes_menor) 
print("4. Tambien el siguiente año y mes cuenta con misma cifra mínima: ")
for year, (mes, valor) in array_meses_lluvia_minima.items():

    if valor == valor_min_aux and year != year_menor:
        print(year," y ",mes) 

print("  ")
print("El año más lluvioso:")
array_max_lluvia= {}

for year, meses in array_lluvia.items():
  
  suma_valor = 0

  for mes, valor in meses.items():
      suma_valor += valor
            
       

  array_max_lluvia[year] =  suma_valor

valor_max_year_aux= 0
year_mayor =""
for year, (mes, valor) in array_meses_lluvia_minima.items():
       
        if valor >= valor_max_year_aux:
           valor_max_year_aux = valor
           year_mayor = year

print(year_mayor)   
print("  ")
print("5. El mes más lluvioso:")
valor_mes_mayor_aux = 0
mes_mayor =""

#aquí reciclamos un arreglo de datos ya creado
#con los datos que necesitamos con la suma de los valores por mes
#print(array_meses_sumados)


for mes, valor_sumado in array_meses_sumados.items():
       
        if valor > valor_mes_mayor_aux:
           valor_mes_mayor_aux = valor
           mes_mayor = mes

print(mes_mayor)