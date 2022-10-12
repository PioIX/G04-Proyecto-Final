from ctypes.wintypes import INT
import sqlite3
conn = sqlite3.connect('bases_de_datos.db')

# ------------------- PREGUNTAS --------------------
conn.execute('''CREATE TABLE IF NOT EXISTS Preguntas
                (id_pregunta INT PRIMARY KEY,
                contenido_pregunta TEXT NOT NULL,
                categoria TEXT NOT NULL);''')
conn.commit()

# ------------- PREGUNTAS DE MUSICA -------------
conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (1, "¿Qué es lo que caracteriza a la Cantante Emilia Mernes?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (2, "¿Cuál fue la primera canción de Duki?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (3, "Cómo sigue la canción: No culpes a la noche, no culpes a la playa, no culpes a la lluvia…", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (4, "¿Cuál es el nombre artístico del cantante Dylan León Masa?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (5, "¿Cuál de estas canciones no es de Charly Garcia?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (6, "¿Quién canta la canción colgando en tus manos?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (7, "¿Cómo se llama el cantante de la imagen?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (8, "¿Cómo se llama Bad Bunny?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (9, "¿Quién no pertenece al grupo de música Queen?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (10, "¿Cuál de estas composiciones no es de Beethoven?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (11, "¿De quién es este logo?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (12, "¿Quién es el cantante de la banda musical Divididos?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (13, "¿Qué cantante ganó un oscar con la canción 'Shallow'?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (14, "¿A qué grupo se lo conoce como 'sus satánicas majestades'?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (15, "¿Cuál fue el primer álbum de Taylor Swift?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (16, "¿Cual es estás figuras públicas no es cantante?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (17, "¿Cuál de estas canciones es de la banda músical no te va a gustar?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (18, "¿Cuál fue el último álbum que lanzó la banda Soda Stereo?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (19, "¿A qué bandas perteneció Residente?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (20, "¿Cuál de estas canciones es de Tego Calderón?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (21, "¿Cual era el nombre de pila del artista Pappo?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (22, "¿Quién era conocido como 'El León Santafesino'?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (23, "¿Con cuál de estos artistas no hizo colaboración Rodrigo Bueno?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (24, "¿Cuál fue la primera canción de Katy Perry?", "Musica");""")
conn.commit()
# -----------------------------------------------------------------------------------
# ----------------------------- PREGUNTAS DE CINE -----------------------------------
conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (25, "Pregunta de cine", "Cine");""")
conn.commit()

# ----------------------- PREGUNTAS DE LIBROS --------------------------------------
conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (id_pregunta, contenido_pregunta, categoria)
                VALUES
                    (26, "Pregunta de libros", "Libros");""")
conn.commit()


# ------------------------------- RESPUESTAS ----------------------------------------
conn.execute('''CREATE TABLE IF NOT EXISTS Respuestas
                (id_respuesta INT PRIMARY KEY,
                contenido_respuesta TEXT NOT NULL,
                categoria TEXT NOT NULL,
                id_pregunta INT,
                es_correcta BOOLEAN);''')
conn.commit()

# ------------------------- RESPUESTAS DE MUSICA ------------------------------------
# 1
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (1, "Los brillos bajo los ojos", 1, "Musica", 1);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (2, "Tener el cuerpo con muchos tatuajes", 0, "Musica", 1);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (3, "Tener muchos piercings", 0, "Musica", 1);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (4, "Todas son Correctas ", 0, "Musica", 1);""")
conn.commit()

# 2
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (5, "No vendo Trap", 1, "Musica", 2);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (6, "Loca", 0, "Musica", 2);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (7, "Givenchy", 0, "Musica", 2);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (8, "Perreo  bendito", 0, "Musica", 2);""")
conn.commit()

# 3
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (9, "ya quiero que te vayas", 0, "Musica", 3);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (10, "Será que no me amas", 1, "Musica", 3);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (11, "Será que me amas", 0, "Musica", 3);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (12, "Ninguna de las anteriores", 0, "Musica", 3);""")
conn.commit()

# 4
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (13, "Lit Killah", 0, "Musica", 4);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (14, "Neo Pistea", 0, "Musica", 4);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (15, "Dillom", 1, "Musica", 4);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (16, "YSY A", 0, "Musica", 4);""")
conn.commit()

# 5
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (17, "Promesas Sobre el bidet", 0, "Musica", 5);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (18, "Los años salvajes", 1, "Musica", 5);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (19, "Demoliendo Hoteles", 0, "Musica", 5);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (20, "Rezo por vos", 0, "Musica", 5);""")
conn.commit()

# 6
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (21, "Carlos Baute y Marta Sanchez", 1, "Musica", 6);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (22, "Carlos Baute", 0, "Musica", 6);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (23, "Carlos Baute y Thalia", 0, "Musica", 6);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (24, "Thalía y David Bisbal", 0, "Musica", 6);""")
conn.commit()

# 7
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (25, "Andres Calamaro", 0, "Musica", 7);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (26, "Luis Alberto Spinetta", 0, "Musica", 7);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (27, "Gustavo Cerati", 0, "Musica", 7);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (28, "Fito Paez", 1, "Musica", 7);""")
conn.commit()

# 8
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (29, "Benito Antonio Martínez Ocasio", 1, "Musica", 8);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (30, "Emmanuel Gazmey Santiago", 0, "Musica", 8);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (31, "Noel Santos Román", 0, "Musica", 8);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (32, "José Daniel Betances", 0, "Musica", 8);""")
conn.commit()

# 9
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (33, "Freddie Mercury", 0, "Musica", 9);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (34, "Roger Taylor", 0, "Musica", 9);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (35, "Brian May", 0, "Musica", 9);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (36, "Peter Criss", 0, "Musica", 9);""")
conn.commit()

# 10
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (37, "Para Elisa", 0, "Musica", 10);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (38, "La Flauta Mágica", 1, "Musica", 10);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (39, "Marcha Turca", 0, "Musica", 10);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (40, "Himno a la Alegría", 0, "Musica", 10);""")
conn.commit()

# 11
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (41, "La Renga", 0, "Musica", 11);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (42, "Intoxicados", 0, "Musica", 11);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (43, "Los piojos", 1, "Musica", 11);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (44, "Las Pelotas", 0, "Musica", 11);""")
conn.commit()

# 12
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (45, "Pity Álvarez", 0, "Musica", 12);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (46, "Emiliano Branccia", 0, "Musica", 12);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (47, "Rolando Sartori", 0, "Musica", 12);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (48, "Ricardo Mollo", 1, "Musica", 12);""")
conn.commit()

# 13
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (49, "Taylor Swift", 0, "Musica", 13);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (50, "Lady Gaga", 1, "Musica", 13);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (51, "Ariana Grande", 0, "Musica", 13);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (52, "Britney Spears", 1, "Musica", 13);""")
conn.commit()

# 14
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (53, "Rolling Stones", 1, "Musica", 14);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (54, "Pink Floyd", 0, "Musica", 14);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (55, "AC/DC", 0, "Musica", 14);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (56, "Metallica", 0, "Musica", 14);""")
conn.commit()

# 15
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (57, "Lover", 0, "Musica", 15);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (58, "Taylor Swift (Taylor's version)", 1, "Musica", 15);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (59, "Red", 0, "Musica", 15);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (60, "Evermore", 0, "Musica", 15);""")
conn.commit()

# 16
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (61, "Ángela Torres", 0, "Musica", 16);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (62, "Miguel Ángel Rodríguez", 1, "Musica", 16);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (63, "Natalia Oreiro", 0, "Musica", 16);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (64, "Lali Espósito", 0, "Musica", 16);""")
conn.commit()

# 17
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (65, "Sin pena ni gloria", 1, "Musica", 17);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (66, "Campanas en la noche", 0, "Musica", 17);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (67, "Ambas", 0, "Musica", 17);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (68, "Ninguna de las anteriores", 0, "Musica", 17);""")
conn.commit()

# 18
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (73, "Obras cumbres", 1, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (74, "Ruido blanco", 0, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (75, "Zona de promesas", 0, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (76, "Sueño stereo", 0, "Musica", 19);""")
conn.commit()

# 19
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (77, "Callejeros", 0, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (78, "No pertenecío a ninguna banda", 0, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (79, "Calle 13", 1, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (80, "Los tigres del Norte", 0, "Musica", 19);""")
conn.commit()

# 20
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (81, "Chambean", 0, "Musica", 20);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (82, "Jangueo", 0, "Musica", 20);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (83, "Pa’ que retozen", 0, "Musica", 20);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (84, "Todas lo son", 1, "Musica", 20);""")
conn.commit()

# 21 
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (85, "Norberto Aníbal Napolitano", 1, "Musica", 21);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (86, "Alejandro Andrés Lococo", 0, "Musica", 21);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (87, "Luciano Napolitano", 0, "Musica", 21);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (88, "Adrián Otero", 0, "Musica", 21);""")
conn.commit()

# 22
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (89, "Daniel Agostini", 0, "Musica", 22);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (90, "Ulises Bueno", 0, "Musica", 22);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (91, "Walter Olmos", 0, "Musica", 22);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (92, "Leo Mattioli", 1, "Musica", 22);""")
conn.commit()

# 23
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (89, "Daniel Agostini", 0, "Musica", 23);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (90, "Ulises Bueno", 0, "Musica", 23);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (91, "Walter Olmos", 0, "Musica", 23);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (92, "Leo Mattioli", 1, "Musica", 23);""")
conn.commit()

# 24
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (93, "Roar", 0, "Musica", 24);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (90, "I kissed a girl", 1, "Musica", 24);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (91, "Dark horse", 0, "Musica", 24);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (92, "E.T", 0, "Musica", 24);""")
conn.commit()

# ------------------------------ RESPUESTAS DE CINE ---------------------------------------
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_respuesta)
            VALUES
                (93, "Respuesta de cine", 0, "Cine", 25);""")
conn.commit()
# ---------------------------- RESPUESTAS DE LIBROS ---------------------------------------
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (id_respuesta, contenido_respuesta, es_correcta, categoria, id_respuesta)
            VALUES
                (94, "Respuesta de libros", 1, "Libros", 26);""")
conn.commit() 