EzTextCrypt รองรับทั้งการเข้ารหัสจากข้อความที่ป้อนเข้ามา และการเข้ารหัสจากไฟล์

[NOTE]: case#1 และ case#2 ให้คัดลอกข้อความภายในไฟล์ที่ระบุไว้ใน input มาวางในโปรแกรม
case#1
  input : case#1_input.txt
  output: ERROR
case#2
  input : case#2_input.txt
  output: case#2_output.txt [512 chars]

[NOTE]: ตั้งแต่ case#3 ขึ้นไป ให้ลากไฟล์ input ใส่สคริปต์ได้เลย
                     หรือรันสคริปต์โดยใช้คำสั่ง 'python encrypt.py <filename>'
case#3
  input: case#3_input.txt
  output: ERROR
case#4
  input: case#4_input.txt
  output: case#4_output.txt [339 chars]
case#5
  input: case#5_input.txt
  output: case#5_output.txt [9936 chars]

[NOTE]: ผลลัพธ์ที่ได้จากการเข้ารหัสข้อความเดียวกันในแต่ละรอบ จะออกมาไม่เหมือนกัน
                    ทุก testcase ได้ผ่านการทดลองเข้ารหัส และถอดรหัสอย่างถูกต้องแล้ว
                    และได้เปรียบเทียบผลลัพธ์ทั้งความยาวข้อมูล และขนาดของข้อมูลเป็นที่เรียบร้อย
        GOOD LUCK HAVE FUN!