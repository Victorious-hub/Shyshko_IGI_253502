import os
import sys
import time
import json
import signal

# Файл для хранения состояния
STATE_FILE = 'process_state.json'

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {}

def signal_handler(signum, frame):
    print("Received signal to terminate. Spawning a new process...")
    # Сохранение текущего состояния
    state = {
        'counter': counter
    }
    save_state(state)
    # Запуск новой копии процесса
    os.execv(sys.executable, ['python'] + sys.argv)

# Установка обработчика сигнала для завершения процесса
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# Загрузка состояния
state = load_state()
counter = state.get('counter', 0)

# Основной цикл работы процесса
while True:
    counter += 1
    print(f"Counter: {counter}")
    time.sleep(1)