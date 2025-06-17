#!/usr/bin/env python3

# ขอให้ผู้ใช้ป้อนตัวเลข 2 ตัว
first = float(input("Give me the first number: "))
second = float(input("Give me the second number: "))

print("Thank you!")

# แสดงผลการคำนวณ
print(f"{int(first)} + {int(second)} = {int(first + second)}")
print(f"{int(first)} - {int(second)} = {int(first - second)}")
print(f"{int(first)} / {int(second)} = {int(first / second)}")
print(f"{int(first)} * {int(second)} = {int(first * second)}")
