from ctypes.wintypes import INT
import sqlite3
conn = sqlite3.connect('bases_de_datos.db')

# ------------------- CINE --------------------
conn.execute('''CREATE TABLE IF NOT EXISTS PreguntasCine
                (id_pregunta INT PRIMARY KEY,
                contenido_pregunta TEXT NOT NULL,
                categoria TEXT NOT NULL);''')
conn.commit()

conn.execute("""INSERT OR IGNORE INTO PreguntasCine
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (1, "Esta es una pregunta de cine", "Cine");""")
conn.commit()

conn.execute('''CREATE TABLE IF NOT EXISTS RespuestasCine
                (id_respuesta INT PRIMARY KEY,
                contenido_respuesta TEXT NOT NULL,
                categoria TEXT NOT NULL,
                es_correcta BOOLEAN);''')
conn.commit()

conn.execute("""INSERT OR IGNORE INTO RespuestasCine
                (id_respuesta, contenido_respuesta, es_correcta, categoria)
            VALUES
                (1, "Cine correcta", 1, "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO RespuestasCine
                (id_respuesta, contenido_respuesta, es_correcta, categoria)
            VALUES
                (2, "Cine incorrecta", 0, "Cine");""")
conn.commit()

# --------------------- MUSICA ------------------------
conn.execute('''CREATE TABLE IF NOT EXISTS PreguntasMusica
                (id_pregunta INT PRIMARY KEY,
                categoria TEXT NOT NULL,
                contenido_pregunta TEXT NOT NULL);''')
conn.commit()

conn.execute("""INSERT OR IGNORE INTO PreguntasMusica
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (1, "Esta es una pregunta de musica", "Musica");""")
conn.commit()

conn.execute('''CREATE TABLE IF NOT EXISTS RespuestasMusica
                (id_respuesta INT PRIMARY KEY,
                contenido_respuesta TEXT NOT NULL,
                categoria TEXT NOT NULL,
                es_correcta BOOLEAN);''')
conn.commit()

conn.execute("""INSERT OR IGNORE INTO RespuestasMusica
                (id_respuesta, contenido_respuesta, es_correcta, categoria)
            VALUES
                (1, "Musica correcta", 1, "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO RespuestasMusica
                (id_respuesta, contenido_respuesta, es_correcta, categoria)
            VALUES
                (2, "Musica incorrecta", 0, "Musica");""")
conn.commit()

# ------------------------ LIBROS --------------------------------
conn.execute('''CREATE TABLE IF NOT EXISTS PreguntasLibros
                (id_pregunta INT PRIMARY KEY,
                categoria TEXT NOT NULL,
                contenido_pregunta TEXT NOT NULL);''')
conn.commit()

conn.execute("""INSERT OR IGNORE INTO PreguntasLibros
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (1, "Esta es una pregunta de libros", "Libros");""")
conn.commit()

conn.execute('''CREATE TABLE IF NOT EXISTS RespuestasLibros
                (id_respuesta INT PRIMARY KEY,
                contenido_respuesta TEXT NOT NULL,
                categoria TEXT NOT NULL,
                es_correcta BOOLEAN);''')
conn.commit()

conn.execute("""INSERT OR IGNORE INTO RespuestasLibros
                (id_respuesta, contenido_respuesta, es_correcta, categoria)
            VALUES
                (1, "Libros correcta", 1, "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO RespuestasLibros
                (id_respuesta, contenido_respuesta, es_correcta, categoria)
            VALUES
                (2, "Libros incorrecta", 0, "Libros");""")
conn.commit()