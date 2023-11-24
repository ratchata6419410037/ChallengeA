# main.py

import area
import cube

def main():
    while True:
        print("\nเมนู:")
        print("1. พื้นที่สี่เหลี่ยม")
        print("2. พื้นที่วงกลม")
        print("3. ปริมาตรทรงสี่เหลี่ยม")
        print("4. ปริมาตรทรงกลม")
        print("0. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกเมนู: ")

        if choice == '0':
            print("จบการทำงานของโปรแกรม")
            break
        elif choice in ['1', '2', '3', '4']:
            if choice == '1':
                width = float(input("ป้อนความกว้าง: "))
                length = float(input("ป้อนความยาว: "))
                result = area.rectangle_area(width, length)
                print(f"พื้นที่สี่เหลี่ยม: {result:.2f}")
            elif choice == '2':
                radius = float(input("ป้อนรัศมี: "))
                result = area.circle_area(radius)
                print(f"พื้นที่วงกลม: {result:.2f}")
            elif choice == '3':
                width = float(input("ป้อนความกว้าง: "))
                length = float(input("ป้อนความยาว: "))
                height = float(input("ป้อนความสูง: "))
                result = cube.rectangle_volume(width, length, height)
                print(f"ปริมาตรทรงสี่เหลี่ยม: {result:.2f}")
            elif choice == '4':
                radius = float(input("ป้อนรัศมี: "))
                result = cube.sphere_volume(radius)
                print(f"ปริมาตรทรงกลม: {result:.2f}")
        else:
            print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")

if __name__ == "__main__":
    main()
