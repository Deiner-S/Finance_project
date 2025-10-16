import threading
import time
class Bot(threading.Thread):
    def __init__(self, group = None, target = None, name = None, args = ..., 
                 kwargs = None, *, daemon = None,email,password,active,operation_value,account_type):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.name = "BB-Strategy"
        self.email = email
        self.password = password
        self.active = active
        self.operation_value = operation_value
        self.account_type = account_type 
        self.stop_flag = threading.Event() 

    def run(self):
        while not self.stop_flag.is_set():
            print("Bot em execução")
            time.sleep(1)

    def stop(self):
        self.stop_flag.set()
