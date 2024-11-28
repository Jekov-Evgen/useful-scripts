import psutil
import GPUtil
import logging

cpu = psutil.cpu_percent(interval=1, percpu=True)
gpu = GPUtil.getGPUs()
memory = psutil.virtual_memory()
logging.basicConfig(level=logging.DEBUG, filename="data_system.log", 
                    format="%(asctime)s - %(message)s", encoding='utf-8')

logging.info(f"Нагрузка на процессор: {round(sum(cpu))}")
logging.info("Данные видеокарты: ")

for i in gpu:
    logging.info(f"Температура видеокарты: {i.temperature}")
    
    if i.load == 0.0:
        logging.info("Ваша дискретаная видеокарта не рабоатет")
        break
    
    logging.info(f"Нагрузка видеокарты: {i.load}")
    
logging.info(f"Количество загруженной памяти пк: {round(memory.used / 1024 ** 3)}")
    
    
