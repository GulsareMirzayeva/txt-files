# Task1

# import os

# fayl_adı = "bazam.txt"

# while True:
#     emeliyyat = input("1: Faylı sil\n2: Məlumat əlavə et\nSeçiminizi daxil edin (1 və ya 2): ")

#     if emeliyyat == "1":
#         try:
#             os.remove(fayl_adı)
#             print("Fayl silindi.")
#         except FileNotFoundError:
#             print("Belə bir fayl tapılmadı.")
#     elif emeliyyat == "2":
#         melumat = input("Əlave etmək istədiyiniz məlumatı daxil edin: ")
#         with open(fayl_adı, 'r') as fayl:
#             məlumatlar = fayl.readlines()
#             if melumat + "\n" not in məlumatlar:
#                 with open(fayl_adı, 'a') as fayl:
#                     fayl.write(melumat + "\n")
#                 print("Məlumat fayla əlavə edildi.")
#             else:
#                 print("Bu məlumat zaten bazada mövcuddur.")
#     else:
#         print("Düzgün bir əməliyyat seçilməyib. Yalnız 1 və ya 2 seçimini edin.")

#     with open(fayl_adı, 'r') as fayl:
#         məlumatlar = fayl.readlines()
#         məlumat_sayı = len(məlumatlar)
#         print(f"Faylda {məlumat_sayı} məlumat mövcuddur.")
#         davam_et = input("Təkrar əməliyyat etmək istəyirsinizmi? (Bəli/Yox): ")
#         if davam_et.lower() != "bəli":
#              break



# Task2

# fayl_adı = "bazam.txt"


# with open(fayl_adı, "r") as fayl:
#     content = fayl.read().split()

# print("Faylın içindəkilər:")
# print(content)

# print(content[0])
# print(content[-1])



# Task3
# class Employee:
#     def __init__(self, emp_name, emp_id, emp_salary, emp_department):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department

#     def calculate_emp_salary(self, hours_worked):
#         if hours_worked <= 50:
#             return self.emp_salary
#         else:
#             overtime = hours_worked - 50
#             overtime_amount = (overtime * (self.emp_salary / 50))
#             return self.emp_salary + overtime_amount

#     def assign_department(self, new_department):
#         self.emp_department = new_department

#     def print_employee_details(self):
#         print("Employee Name:", self.emp_name)
#         print("Employee ID:", self.emp_id)
#         print("Employee Salary:", self.emp_salary)
#         print("Employee Department:", self.emp_department)


# employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
# employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
# employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
# employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")


# employee1.print_employee_details()

# employee2.assign_department("HR")
# print("Employee Department after change:")
# employee2.print_employee_details()

# salary_with_overtime = employee3.calculate_emp_salary(60)
# print("Employee Salary with Overtime:", salary_with_overtime)
