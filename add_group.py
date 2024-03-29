import pandas as pd
from db import *


def add_students_from_text_file(text_file_path: str):
    with open(text_file_path, 'r', encoding='utf-8') as file:
        lines = file.read()
    # new_lines = lines.replace('\n\n', '\n')
    student_list = lines.split('\n')
    return student_list


def insert_group(group_name: str, text_file_path: str, teacher_id: int):
    student_list = add_students_from_text_file(text_file_path)
    group_id = add_group_to_db(group_name, teacher_id)
    for student in student_list:
        insert("students", [student, group_name, group_id])


# def check_same_group(student_list: list) -> bool:


