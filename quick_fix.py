#!/usr/bin/env python3
# EPITHILIAL Quick Cancer Detection Fix - 5 lines
def quick_detect(values):
    avg = sum(values)/len(values) if values else 0
    return "CANCER" if avg > 0.75 else "NORMAL"
print("Quick fix loaded")
