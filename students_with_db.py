import pyodbc
conn=pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=USER-PC;"
    "Database=python_db;"
    "Trusted_Connection=yes;"
)



def entry_of_student():
    temp_list=gather_information()
    print(temp_list)
    temp_std_id=temp_list[4]
    cursor=conn.cursor()
    cursor.execute('insert into student1(name,age,father_name,std_id,std_address,personal_phone_no,father_phone_no) values(?,?,?,?,?,?,?)',(
        temp_list[0],temp_list[1],temp_list[2],temp_list[4],temp_list[5],temp_list[6],temp_list[7]
    ))
    cursor.commit()

    print("Entry Done")
    temp_decision=int(input("Enter No Of Course This Student is it in: "))
    print(temp_std_id)
    for i in range(0,temp_decision):
        temp_list=gather_information_couse()
        print(temp_list)
        cursor=conn.cursor()
        cursor.execute('insert into courses1(course_id,course_name,course_fees,course_duration_month,std_id,fees_paid_by_student) values(?,?,?,?,?,?)',(
            str(temp_list[0]),str(temp_list[1]),str(temp_list[2]),str(temp_list[3]),str(temp_std_id),str(temp_list[4])
        ))
        cursor.commit()


    #Procedure to Enter Course Detail
def gather_information():
    temp_list=[]
    temp_name=input("Enter Student's Name: ")
    temp_list.append(temp_name)
    temp_age=input("Enter Student's Age: ")
    temp_list.append(temp_age)
    temp_fathername=input("Enter Student's Father Name: ")
    temp_list.append(temp_fathername)
    temp_date_of_admission=input("Enter Date Of Admission: ")
    temp_list.append(temp_date_of_admission)
    temp_std_id=input("Enter Student Id: ")
    temp_list.append(temp_std_id)
    temp_address=input("Enter Student's Address: ")
    temp_list.append(temp_address)
    temp_personal_phone_no=input("Enter Student's Phone No: ")
    temp_list.append(temp_personal_phone_no)
    temp_father_phone_no=input("Enter Father's Phone No: ")
    temp_list.append(temp_father_phone_no)

    return temp_list
def gather_information_couse():
    temp_list=[]
    course_id=input("Enter Course id: ")
    temp_list.append(course_id)
    courses_name=input("Enter Course Name: ")
    temp_list.append(courses_name)
    courses_fees=input("Enter Fees of Course: ")
    temp_list.append(courses_fees)
    courses_duration_month=input("Enter Duration Of Course: ")
    temp_list.append(courses_duration_month)
    fees_paid_by_student=input("Enter Fees paid by Students For this Course: ")
    temp_list.append(fees_paid_by_student)
    return temp_list
def update_student():
    print('Select Option:\n 1)To Change Name \n 2)To Change Age \n 3)To Change Fathername \n 4)To Change Address \n 5)To Change Phone No. \n 6)To Change Father Phone No.')
    temp_decision=input("Enter: ")
    if(temp_decision=='1'):
        temp_std_id=input("Enter Student Id")
        temp_info=input("Enter Name: ")
        cursor=conn.cursor()
        cursor.execute("UPDATE student1 SET name = ? WHERE std_id = ?", temp_info, temp_std_id)
        cursor.commit()
    elif(temp_decision=='2'):
        temp_std_id=input("Enter Student Id")
        temp_info=input("Enter Age : ")
        cursor=conn.cursor()
        cursor.execute("UPDATE student1 SET age = ? WHERE std_id = ?", temp_info, temp_std_id)
        cursor.commit()
    elif(temp_decision=='3'):
        temp_std_id=input("Enter Student Id")
        temp_info=input("Enter Fathername : ")
        cursor=conn.cursor()
        cursor.execute("UPDATE student1 SET father_name = ? WHERE std_id = ?", temp_info, temp_std_id)
        cursor.commit()
    elif(temp_decision=='4'):
        temp_std_id=input("Enter Student Id")
        temp_info=input("Enter New Address : ")
        cursor=conn.cursor()
        cursor.execute("UPDATE student1 SET std_address = ? WHERE std_id = ?", temp_info, temp_std_id)
        cursor.commit()
    elif(temp_decision=='5'):
        temp_std_id=input("Enter Student Id")
        temp_info=input("Enter Phone No. : ")
        cursor=conn.cursor()
        cursor.execute("UPDATE student1 SET personal_phone_no = ? WHERE std_id = ?", temp_info, temp_std_id)
        cursor.commit()
    elif(temp_decision=='6'):
        temp_std_id=input("Enter Student Id")
        temp_info=input("Enter FatherPhone No. : ")
        cursor=conn.cursor()
        cursor.execute("UPDATE student1 SET father_phone_no = ? WHERE std_id = ?", temp_info, temp_std_id)
        cursor.commit()
    else:
        print("No Such Fucntionality Yet")

    print('\n')
    print('#####################################################')
    print('\n')
def update_course_detail():
    print('Select Option:\n 1)To Change Course Name \n 2)To Change Course Duration \n 3)To Change Fees paid By Student')
    temp_decision=input("Enter: ")
    if(temp_decision=='1'):
        temp_std_id=input("Enter Student Id")
        temp_course_id=input("Enter Student Id")
        temp_info=input("Enter Course name: ")
        cursor=conn.cursor()
        cursor.execute("UPDATE courses1 SET course_name = ? WHERE std_id = ? and course_id", temp_info, temp_std_id,temp_course_id)
        cursor.commit()
    elif(temp_decision=='2'):
        temp_std_id=input("Enter Student Id")
        temp_course_id=input("Enter Course Id")
        temp_info=input("Enter Course Duration: ")
        cursor=conn.cursor()
        cursor.execute("UPDATE courses1 SET course_duration_month = ? WHERE std_id = ? and course_id", temp_info, temp_std_id,temp_course_id)
        cursor.commit()
    elif(temp_decision=='3'):
        temp_std_id=input("Enter Student Id")
        temp_course_id=input("Enter Course Id")
        temp_info=input("Enter Fees by Student: ")
        cursor=conn.cursor()
        cursor.execute("UPDATE courses1 SET fees_paid_by_student = ? WHERE std_id = ? and course_id", temp_info, temp_std_id,temp_course_id)
        cursor.commit()

    else:
        print("No Such Fucntionality Yet")

    print('\n')
    print('#####################################################')
    print('\n')
def view_detail():
    cursor=conn.cursor()
    cursor.execute("select * from student1")
    for row in cursor.fetchall():
        print (row)
    cursor.commit()
    print("Here are Name, age, student id, Fathername, Date Of Addmissino, Address, Personal Phone No and Father Phone No")


def view_detail_by_id(std_id):
    cursor=conn.cursor()
    cursor.execute("select * from student1 where std_id=?",std_id)
    '''
        temp_list=cursor.fetchall()
    print("Name is : ",temp_list[0])
    print("Age is : ",temp_list[1])
    print("Student Id is: ",temp_list[2])
    print("FatherName is : ",temp_list[3])
    print("Date Of Admission :",temp_list[4])
    print("Student Address: ",temp_list[5])
    print("Student Phone No: ",temp_list[6])
    print("Father Phone No: ",temp_list[7])

    '''
    print("Here are Name, age, student id, Fathername, Date Of Addmissino, Address, Personal Phone No and Father Phone No")
    for row in cursor.fetchall():
        print (row)
def remove_courses(std_id,temp_course_name):
    cursor=conn.cursor()
    cursor.execute("delete from courses1 where std_id=? and course_name=?",std_id,temp_course_name)
    cursor.commit()
def remove_student(std_id):
    cursor=conn.cursor()
    cursor.execute("delete from student1 where std_id=?",std_id)
    cursor.commit()

#for driver in pyodbc.drivers():
#    print(driver)

for i in range(0,6):
    print('Select Option:\n 1)For Student Entry \n 2)View Students Complete Detail \n 3)Search Student By Id \n 4)Cancel the Entry \n 5)Update information \n 6)Remove Courses')
    temp_decision=input("Enter: ")
    if(temp_decision=='1'):
        entry_of_student()
    elif(temp_decision=='2'):
        view_detail()
    elif(temp_decision=='3'):
        temp_std_id=input("Enter Student id : ")
        view_detail_by_id(temp_std_id)
    elif(temp_decision=='4'):
        temp_std_id=input("Enter Student id : ")
        remove_student(temp_std_id)
    elif(temp_decision=='5'):
        update_student()
    elif(temp_decision=='6'):
        temp_std_id=input("Enter Student id : ")
        temp_course_name=input("Enter Student Course Name : ")
        remove_courses(temp_std_id,temp_course_name)
    else:
        print("No Such Fucntionality Yet")

    print('\n')
    print('#####################################################')
    print('\n')
