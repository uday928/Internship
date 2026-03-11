import mysql.connector
from datetime import datetime

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="students_evaluation",
    port=3306    
)
cursor=conn.cursor()
print("check 1: database connection done!")

cursor.execute(
    '''
    INSERT INTO students 
(name, age, gender, maths, science, computer, `operating systems`, total, percentage, grade, result)
VALUES
('Aarav', 20, 'M', 85, 78, 90, 88, 341, 85, 'A', 'PASS'),
('Vivaan', 21, 'M', 72, 69, 75, 70, 286, 72, 'B', 'PASS'),
('Aditya', 19, 'M', 91, 88, 95, 92, 366, 92, 'A', 'PASS'),
('Vihaan', 22, 'M', 60, 65, 58, 62, 245, 61, 'C', 'PASS'),
('Arjun', 20, 'M', 48, 52, 45, 50, 195, 49, 'D', 'FAIL'),

('Sai', 21, 'M', 76, 80, 79, 77, 312, 78, 'B', 'PASS'),
('Reyansh', 20, 'M', 89, 84, 91, 87, 351, 88, 'A', 'PASS'),
('Krishna', 19, 'M', 67, 70, 65, 68, 270, 68, 'C', 'PASS'),
('Ishaan', 22, 'M', 55, 60, 58, 57, 230, 58, 'C', 'PASS'),
('Shaurya', 20, 'M', 92, 94, 96, 90, 372, 93, 'A', 'PASS'),

('Ananya', 19, 'F', 88, 90, 85, 87, 350, 88, 'A', 'PASS'),
('Diya', 20, 'F', 74, 76, 72, 75, 297, 74, 'B', 'PASS'),
('Myra', 21, 'F', 69, 64, 70, 68, 271, 68, 'C', 'PASS'),
('Aadhya', 20, 'F', 58, 62, 60, 59, 239, 60, 'C', 'PASS'),
('Pari', 22, 'F', 45, 48, 50, 47, 190, 48, 'D', 'FAIL'),

('Riya', 19, 'F', 95, 92, 94, 96, 377, 94, 'A', 'PASS'),
('Saanvi', 21, 'F', 82, 85, 80, 83, 330, 83, 'A', 'PASS'),
('Navya', 20, 'F', 71, 68, 73, 70, 282, 71, 'B', 'PASS'),
('Anika', 22, 'F', 64, 66, 62, 65, 257, 64, 'C', 'PASS'),
('Sara', 19, 'F', 52, 55, 50, 53, 210, 53, 'D', 'FAIL'),

('Kabir', 21, 'M', 87, 82, 85, 88, 342, 86, 'A', 'PASS'),
('Rudra', 20, 'M', 78, 74, 76, 79, 307, 77, 'B', 'PASS'),
('Aryan', 22, 'M', 69, 72, 68, 70, 279, 70, 'B', 'PASS'),
('Dev', 19, 'M', 61, 63, 60, 62, 246, 62, 'C', 'PASS'),
('Yash', 21, 'M', 49, 45, 50, 48, 192, 48, 'D', 'FAIL'),

('Meera', 20, 'F', 90, 88, 92, 91, 361, 90, 'A', 'PASS'),
('Kavya', 19, 'F', 84, 80, 83, 85, 332, 83, 'A', 'PASS'),
('Ira', 22, 'F', 75, 78, 72, 74, 299, 75, 'B', 'PASS'),
('Tara', 21, 'F', 66, 64, 68, 65, 263, 66, 'C', 'PASS'),
('Zara', 20, 'F', 54, 50, 52, 55, 211, 53, 'D', 'FAIL'),

('Rahul', 22, 'M', 88, 86, 84, 87, 345, 86, 'A', 'PASS'),
('Karan', 19, 'M', 79, 77, 75, 78, 309, 77, 'B', 'PASS'),
('Manav', 20, 'M', 70, 68, 72, 71, 281, 70, 'B', 'PASS'),
('Nikhil', 21, 'M', 63, 60, 65, 62, 250, 63, 'C', 'PASS'),
('Varun', 22, 'M', 50, 48, 52, 49, 199, 50, 'D', 'FAIL'),

('Pooja', 20, 'F', 91, 93, 89, 92, 365, 91, 'A', 'PASS'),
('Sneha', 21, 'F', 83, 81, 85, 82, 331, 83, 'A', 'PASS'),
('Nisha', 19, 'F', 74, 72, 70, 73, 289, 72, 'B', 'PASS'),
('Simran', 22, 'F', 65, 67, 63, 66, 261, 65, 'C', 'PASS'),
('Aisha', 20, 'F', 53, 55, 50, 52, 210, 53, 'D', 'FAIL'),

('Harsh', 21, 'M', 86, 88, 84, 85, 343, 86, 'A', 'PASS'),
('Rohan', 19, 'M', 77, 79, 75, 76, 307, 77, 'B', 'PASS'),
('Siddharth', 22, 'M', 68, 70, 65, 69, 272, 68, 'C', 'PASS'),
('Aman', 20, 'M', 60, 58, 62, 61, 241, 60, 'C', 'PASS'),
('Deepak', 21, 'M', 47, 49, 45, 48, 189, 47, 'D', 'FAIL');
'''
)
conn.commit()