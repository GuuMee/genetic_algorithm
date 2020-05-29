import sqlite3 as sql
conn = sql.connect('class_schedule.db')
c = conn.cursor()
c.execute("""create table room (number text, capacity integer)""")
c.execute("insert into room Values ('R1', 25),"
                                  "('R2', 45),"
                                  "('R3', 35),"
                                  "('R4', 40)")
c.execute("""create table meeting_time (id text, time text)""")
c.execute("insert into meeting_time Values ('MT1', 'MWF 09:00 - 10:00'),"
                                          "('MT2', 'MWF 10:00 - 11:00'),"
                                          "('MT3', 'TTH 09:00 - 10:30'),"
                                          "('MT4', 'TTH 10:30 - 12:00')")
c.execute("""create table instructor (number text, name text)""")
c.execute("insert into instructor Values ('I1', 'Dr James Web'),"
                                        "('I2', 'Mr. Mike Brown'),"
                                        "('I3', 'Dr Steve Day'),"
                                        "('I4', 'Mrs Jane Doe'),"
                                        "('I5', 'Dr. Julia Blue')")
c.execute("""create table course_instructor (course_number text, instructor_number text)""")
c.execute("insert into course_instructor Values ('C1', 'I1'),"
                                               "('C1', 'I2'),"
                                               "('C2', 'I1')," 
                                               "('C2', 'I2')," 
                                               "('C2', 'I3')," 
                                               "('C3', 'I1'),"
                                               "('C3', 'I2'),"
                                               "('C4', 'I3'),"
                                               "('C4', 'I4'),"
                                               "('C5', 'I4'),"
                                               "('C6', 'I1'),"
                                               "('C6', 'I3'),"
                                               "('C7', 'I2'),"
                                               "('C7', 'I4'),"
                                               "('C8', 'I5'),"
											   "('C9', 'I5'),"
											   "('C10','I1'),"
											   "('C10','I2')")
c.execute("""create table course (number text, name text, max_numb_of_students)""")
c.execute("insert into course Values ('C1', '325K', 25),"
                                    "('C2', '319K', 35)," 
                                    "('C3', '462k', 25),"
                                    "('C4', '464K', 30),"
                                    "('C5', '360C', 35),"
                                    "('C6', '303K', 45),"
                                    "('C7', '303L', 45),"
                                    "('C8', '323',  30),"
                                    "('C9', '150k', 40),"
								    "('C10','M341', 40)")


c.execute("""create table dept (name text)""")
c.execute("insert into dept Values ('MATH'),"
                                  "('EE'),"
                                  "('PHY'),"
                                  "('SDS')")
c.execute("""create table dept_course (name text, course_numb text)""")
c.execute("insert into dept_course Values ('MATH', 'C1'),"
                                         "('MATH', 'C3'),"
                                         "('EE',   'C2'),"
                                         "('EE',   'C4'),"
                                         "('EE',   'C5'),"
                                         "('PHY',  'C6'),"
                                         "('PHY',  'C7'),"
                                         "('SDS',  'C8'),"
                                         "('SDS',  'C9'),"
                                         "('MATH', 'C10')")
conn.commit()
c.close()
conn.close()