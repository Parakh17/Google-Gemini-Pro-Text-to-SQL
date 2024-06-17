from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import sqlite3

import google.generativeai as googleai

googleai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(prompt, question):
    model=googleai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt,question])
    print(response)
    print("--",response.text)
    return response.text

def read_sql(db,sql):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = [
    """
    You are a master in converting questions asked in english into sql query !
    you have the accuracy of 100%
    the sql database contains table named STUDENT
    in which it has columns - (NAME, CLASS, SECTION, MARKS)
    \n for example \n ques 1 - display all the records \n answer - SELECT * FROM STUDENT;
    \n ques 2 - what is the total number of students present \n answer - SELECT COUNT(*) FROM STUDENT;
    \n ques 3 - who scored the highest marks \n answer - SELECT * FROM STUDENT ORDER BY MARKS DESC LIMIT 1;
    
    """
]

question = """which student got marks above 90  """

get_gemini_response(prompt=prompt[0], question=question)


