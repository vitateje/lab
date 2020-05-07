#!/usr/bin/env python3

import time    
import subprocess
import psutil

def UsoCPU():
    #obtem informacao da freq do processador
    cur_uso_cpu = psutil.cpu_percent() 
    return cur_uso_cpu
