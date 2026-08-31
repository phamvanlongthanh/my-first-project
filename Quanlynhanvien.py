# ==========================================
# CHUONG TRINH QUAN LY SINH VIEN
# ==========================================

students = []


# ------------------------------------------
# 1. Them sinh vien
# ------------------------------------------
def add_student():
    print("\n--- THEM SINH VIEN ---")

    student_id = input("Nhap ma sinh vien: ")

    # Kiem tra ma trung
    for student in students:
        if student["id"] == student_id:
            print("Ma sinh vien da ton tai!")
            return

    name = input("Nhap ho ten: ")

    # Kiem tra tuoi
    while True:
        try:
            age = int(input("Nhap tuoi: "))

            if age > 0:
                break

            print("Tuoi phai lon hon 0!")

        except ValueError:
            print("Tuoi phai la so nguyen!")

    # Kiem tra diem
    while True:
        try:
            score = float(input("Nhap diem: "))

            if 0 <= score <= 10:
                break

            print("Diem phai tu 0 den 10!")

        except ValueError:
            print("Diem phai la so!")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "score": score
    }

    students.append(student)

    print("Them sinh vien thanh cong!")


# ------------------------------------------
# 2. Hien thi danh sach
# ------------------------------------------
def display_students():
    print("\n--- DANH SACH SINH VIEN ---")

    if len(students) == 0:
        print("Danh sach sinh vien rong!")
        return

    for student in students:
        print(
            "Ma:", student["id"],
            "| Ten:", student["name"],
            "| Tuoi:", student["age"],
            "| Diem:", student["score"]
        )


# ------------------------------------------
# 3. Tim sinh vien
# ------------------------------------------
def find_student():
    print("\n--- TIM SINH VIEN ---")

    student_id = input("Nhap ma sinh vien can tim: ")

    for student in students:
        if student["id"] == student_id:
            print("Tim thay sinh vien:")
            print(
                "Ma:", student["id"],
                "| Ten:", student["name"],
                "| Tuoi:", student["age"],
                "| Diem:", student["score"]
            )
            return student

    print("Khong tim thay sinh vien!")
    return None


# ------------------------------------------
# 4. Sua sinh vien
# ------------------------------------------
def update_student():
    print("\n--- SUA SINH VIEN ---")

    student_id = input("Nhap ma sinh vien can sua: ")

    for student in students:

        if student["id"] == student_id:

            student["name"] = input("Nhap ten moi: ")

            while True:
                try:
                    age = int(input("Nhap tuoi moi: "))

                    if age > 0:
                        student["age"] = age
                        break

                    print("Tuoi phai lon hon 0!")

                except ValueError:
                    print("Tuoi phai la so nguyen!")

            while True:
                try:
                    score = float(input("Nhap diem moi: "))

                    if 0 <= score <= 10:
                        student["score"] = score
                        break

                    print("Diem phai tu 0 den 10!")

                except ValueError:
                    print("Diem phai la so!")

            print("Cap nhat thanh cong!")
            return

    print("Khong tim thay sinh vien!")


# ------------------------------------------
# 5. Xoa sinh vien
# ------------------------------------------
def delete_student():
    print("\n--- XOA SINH VIEN ---")

    student_id = input("Nhap ma sinh vien can xoa: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            print("Xoa sinh vien thanh cong!")
            return

    print("Khong tim thay sinh vien!")


# ------------------------------------------
# 6. Xep loai sinh vien
# ------------------------------------------
def classify_student():
    print("\n--- XEP LOAI SINH VIEN ---")

    student_id = input("Nhap ma sinh vien: ")

    for student in students:

        if student["id"] == student_id:

            score = student["score"]

            if score >= 8:
                rank = "Gioi"

            elif score >= 6.5:
                rank = "Kha"

            elif score >= 5:
                rank = "Trung binh"

            else:
                rank = "Yeu"

            print("Sinh vien:", student["name"])
            print("Diem:", score)
            print("Xep loai:", rank)

            return

    print("Khong tim thay sinh vien!")


# ------------------------------------------
# MENU CHINH
# ------------------------------------------
def main():

    while True:

        print("\n================================")
        print("     QUAN LY SINH VIEN")
        print("================================")
        print("1. Them sinh vien")
        print("2. Hien thi danh sach")
        print("3. Tim sinh vien")
        print("4. Sua sinh vien")
        print("5. Xoa sinh vien")
        print("6. Xep loai sinh vien")
        print("0. Thoat")
        print("================================")

        choice = input("Nhap lua chon: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            find_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            classify_student()

        elif choice == "0":
            print("Da thoat chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


# Chay chuong trinh
if __name__ == "__main__":
    main()