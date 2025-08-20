from datetime import date
import time
"O objetivo desse arquivo e trabalhar  maneiras simples de obter data e hora"

today = date.today()
current_time = time.localtime()

print("Data de hoje:", today)
print("Hora atual:", current_time.tm_hour, ":", current_time.tm_min, ":", current_time.tm_sec)