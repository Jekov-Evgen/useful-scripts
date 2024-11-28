import psutil
import GPUtil
import logging

cpu = psutil.cpu_percent(interval=1, percpu=True)
gpu = GPUtil.getGPUs()
memory = psutil.virtual_memory()

print("Нагрузка на процессор: ", round(sum(cpu)))
print("Данные видеокарты: ")

for i in gpu:
    print("Температура видеокарты: ", i.temperature)
    
    if i.load == 0.0:
        print("Ваша дискретаная видеокарта не рабоатет")
        break
    
    print("Нагрузка видеокарты: ", i.load)
    
print("Количество загруженной памяти пк: ", round(memory.used / 1024 ** 3))
    
    
