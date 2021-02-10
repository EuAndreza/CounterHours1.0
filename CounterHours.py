entrada = '08:35'
saida = '11:00'

entrada1 = entrada.split(':')
saida1 = saida.split(':')

result = 0

TotalHr = int(saida1[0]) - int(entrada1[0])
TotalMin = int(saida1[1]) - int(entrada1[1])
timeHr = TotalHr * 60
timeTotal = timeHr - abs(TotalMin)

#timerest = timeTotal % 60
#time = timeTotal // timeHr  
while(timeTotal >60):
    timeTotal = timeTotal - 60
    result = result + 1
#print(timeTotal)
print("total de horas trabalhadas é:", result , ":" , timeTotal)
#print(timeTotal)