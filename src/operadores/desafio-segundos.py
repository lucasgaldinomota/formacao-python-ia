# Peça ao usuário que insira um número total de segundos 
# e converta esse valor para horas, minutos e segundos.
# 3601 s -> 1h 0m 1s
# 3661 s -> 1h 1m 1s

UMA_HORA_EM_SEGUNDOS = 3600
UM_MINUTO_EM_SEGUNDOS = 60

total_em_segundos = int(input("Informe a qtde de segundos: "))

horas = total_em_segundos // UMA_HORA_EM_SEGUNDOS

resto = total_em_segundos % UMA_HORA_EM_SEGUNDOS
minutos = resto // UM_MINUTO_EM_SEGUNDOS

segundos = total_em_segundos % UM_MINUTO_EM_SEGUNDOS

print(f"{horas}h {minutos}m {segundos}s")
