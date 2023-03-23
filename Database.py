import sqlite3 as sql

conn = sql.connect("workout.db")

c = conn.cursor()

# c.execute("""CREATE TABLE workouts_diets (
#             workout blob,
#             diet blob
#         ) """)

many_workouts = [
                    ('', ''),
                    ('', ''),
                    ('', ''),
                    ('', ''),
                    ('', ''),
                ]
c.executemany("INSERT INTO workouts VALUES(?, ?)", many_workouts)

conn.commit()
conn.close()

