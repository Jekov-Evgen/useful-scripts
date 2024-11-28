import psutil
import GPUtil

cpu = psutil.cpu_percent(interval=1, percpu=True)
gpu = GPUtil.getGPUs()

print("Нагрузка на процессор: ", round(sum(cpu)))
print("Данные видеокарты: ")

for i in gpu:
    print("Температура видеокарты: ", i.temperature)
    
    if i.load == 0.0:
        print("Ваша дискретаная видеокарта не рабоатет")
        break
    
    print("Нагрузка видеокарты: ", i.load)
    
    
