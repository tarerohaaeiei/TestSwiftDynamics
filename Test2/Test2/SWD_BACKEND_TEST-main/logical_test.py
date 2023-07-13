
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
Num = 190

def thai_number_mapping(number):
    thai_numbers = {
        0: 'ศูนย์',
        1: 'หนึ่ง',
        2: 'สอง',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า',
        10: 'สิบ',
        100: 'ร้อย',
        1000: 'พัน',
        10000: 'หมื่น',
        100000: 'แสน',
        1000000: 'ล้าน'
    }
    return thai_numbers[number]

def number_to_thai_text(number):
    # Handling zero case separately
    if number == 0:
        return thai_number_mapping(0)
    
    # Splitting the number into individual units
    units = [1000000, 100000, 10000, 1000, 100, 10, 1]
    unit_names = ['ล้าน', 'แสน', 'หมื่น', 'พัน', 'ร้อย', 'สิบ', '']
    thai_text = ''
    
    # Looping through each unit to convert it into Thai text
    for unit, unit_name in zip(units, unit_names):
        if number >= unit:
            count = number // unit
            number %= unit
            if count > 1 and unit_name == 'สิบ':
                if  thai_number_mapping(count) == 'สอง' :
                    thai_text += 'ยี่' + unit_name
                    break
                else:
                    thai_text += thai_number_mapping(count) + unit_name + 'เอ็ด'
                    break
            else:
                if  thai_number_mapping(count) == 'สอง' and unit_name == 'สิบ':
                    thai_text += 'ยี่' + unit_name
                else:
                    thai_text += thai_number_mapping(count) + unit_name
    return thai_text

print(number_to_thai_text(201))