import os
import time

os.system('adb root')
time.sleep(1)
os.system('adb remount')
time.sleep(1)
while True:
    os.system('echo gpu_core >>gpu.txt')
    os.system('adb shell "cat /sys/kernel/debug/clk/clk_gpu_core/clk_rate ">>gpu.txt')
    os.system('echo gpu_core>>gpu.txt')
    os.system('adb shell "cat /sys/kernel/debug/clk/clk_gpu_mem/clk_rate ">>gpu.txt')
    time.sleep(0.8)