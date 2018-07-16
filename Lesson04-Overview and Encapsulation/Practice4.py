import time

class Computer:
    def poweron(self):
        pass
    def load_BIOS(self):
        time.sleep(1)
    def load_bootloader(self):
        time.sleep(1)
    def load_OS(self):
        time.sleep(3)
    def boot(self):
        pc.poweron()
        print('Power turned on')
        pc.load_BIOS()
        print('BIOS loaded')
        pc.load_bootloader()
        print('Bootloader loaded')
        pc.load_OS()
        print('OS loaded')
        print('Boot complete')
        
pc = Computer()
pc.boot()
