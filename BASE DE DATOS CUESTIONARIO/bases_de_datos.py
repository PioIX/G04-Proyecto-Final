from ctypes.wintypes import INT
import sqlite3
conn = sqlite3.connect('base_de_datos.db')

# ------------------- PREGUNTAS --------------------
conn.execute('''CREATE TABLE IF NOT EXISTS Preguntas
                (id_pregunta INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido_pregunta TEXT NOT NULL,
                categoria TEXT NOT NULL);''')
conn.commit()

#--------------------JUGADORES--------------------

conn.execute("""CREATE TABLE IF NOT EXISTS Jugadores
	(id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
	nombre_jugador TEXT NOT NULL,
	contraseña	TEXT NOT NULL);""")
conn.commit()

# ------------- PREGUNTAS DE MUSICA -------------
conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Qué es lo que caracteriza a la Cantante Emilia Mernes?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál fue la primera canción de Duki?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("Cómo sigue la canción: No culpes a la noche, no culpes a la playa, no culpes a la lluvia…", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál es el nombre artístico del cantante Dylan León Masa?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas canciones no es de Charly Garcia?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién canta la canción colgando en tus manos?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cómo se llama el cantante de la imagen?
                    https://replit.com/@iaramareco/TP-Final#imagenes_bdd/musicapreg7.jpg", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cómo se llama Bad Bunny?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién no pertenece al grupo de música Queen?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas composiciones no es de Beethoven?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿De quién es este logo?
                    https://replit.com/@iaramareco/TP-Final#imagenes_bdd/musicapreg11.jpg", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién es el cantante de la banda musical Divididos?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Qué cantante ganó un oscar con la canción 'Shallow'?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿A qué grupo se lo conoce como 'sus satánicas majestades'?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál fue el primer álbum de Taylor Swift?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cual es estás figuras públicas no es cantante?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas canciones es de la banda músical no te va a gustar?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál fue el último álbum que lanzó la banda Soda Stereo?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿A qué bandas perteneció Residente?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas canciones es de Tego Calderón?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cual era el nombre de pila del artista Pappo?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién era conocido como 'El León Santafesino'?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Con cuál de estos artistas no hizo colaboración Rodrigo Bueno?", "Musica");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál fue la primera canción de Katy Perry?", "Musica");""")
conn.commit()
# -----------------------------------------------------------------------------------


# ----------------------------- PREGUNTAS DE CINE -----------------------------------
conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("Según el dibujito ¿Qué animal era Dumbo?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("En Toy story 4 ¿Qué es Forky?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuántas temporadas tiene hasta ahora (2022) The Walking Dead?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Qué personaje muere en Grey ‘s Anatomy?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuántos hermanos había en la familia Bridgerton?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("En Sex Education ¿Quién abre la clínica de terapia sexual en la escuela?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuántos relatos se contaban en la película 'Relatos Salvajes'?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién hace de Benjamin en el secreto de tus ojos?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estos actores no participó en la película 'El Clan'?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién fue el director de la película 'El Ángel'?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cómo se llaman las protagonistas de la serie Gilmore Girls?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("A qué personaje protagonizó la China Suárez en la telenovela de Argentina, Tierra de amor y venganza?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas telenovelas no es argentina?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas series no es infantojuvenil?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("En la película 'Chicas Pesadas' ¿Que personaje utiliza la palabra fetch?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuántos años tenia el nene de la película “Mi pobre angelito” cuando es olvidado en su casa?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("En la película 'Matilda' ¿De que trabaja el padre?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿En qué película/serie aparece la frase 'No es tan difícil hacer dinero cuando es solo hacer dinero lo que pretende?'", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién es este 
                    https://replit.com/@iaramareco/TP-Final#imagenes_bdd/pelipreg18.jpg?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién fue el director de la Saga Star Wars?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuántas películas tiene la saga Harry Potter?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cómo se llaman las protagonistas de Pretty Little Liars?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estos no interpretó al hombre araña?", "Cine");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cual es el nombre de esta película?
                    https://replit.com/@iaramareco/TP-Final#imagenes_bdd/pelipreg24.jpg", "Cine");""")
conn.commit()
# ----------------------- PREGUNTAS DE LIBROS --------------------------------------
conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuando ganó el premio Nobel de Literatura, el escritor Gabriel Garcia Marquez?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cómo se llama el protagonista de la novela 'Relatos de un Náufrago'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿De qué género es 'Romeo y Julieta'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas es una obra del escritor Charles Dickens?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál es el cuento más reconocido de Edgar Allan Poe?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién es este escritor?
                    https://replit.com/@iaramareco/TP-Final#imagenes_bdd/libropreg6.jpg", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál fue el primer libro de Alfonsina Storni?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién ganó en 1945 el Premio Nobel De Literatura?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estos libros fue escrito por Pablo Neruda?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estos libros no fue escrito por Gabriel Garcia Marquez?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quién escribió la novela 'Crónicas de una Muerte Anunciada'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estas no es una editorial?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál de estos no era un ministerio de 1984?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Con qué artista tuvo una relación Sackville-West?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cómo se llamaba la droga que se utilizaba en 'Un Mundo Feliz'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿En qué ciudad alemana estuvo basado el libro 'La Ladrona de Libros'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Qué enfermedad tenía el protagonista de 'La Lección de August'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuáles fueron las promesas que hicieron las hermanas en 'Mujercitas'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Quiénes eran los hijos de Pilar Ternera en 'Cien Años de Soledad'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿A qué corriente filosófica pertenece el libro 'El Extranjero'?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿En qué libro de la saga 'Harry Potter' se utiliza el giratiempo?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál es el libro más leído del mundo?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál es el libro más aclamado de Simone de Beauvoir?", "Libros");""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Preguntas
                    (contenido_pregunta, categoria)
                VALUES
                    ("¿Cuál es el libro que se dice que hay que leerlo a diferentes edades?", "Libros");""")
conn.commit()

# ------------------------------- RESPUESTAS ----------------------------------------
conn.execute('''CREATE TABLE IF NOT EXISTS Respuestas
                (id_respuesta INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido_respuesta TEXT NOT NULL,
                categoria TEXT NOT NULL,
                id_pregunta INT,
                es_correcta BOOLEAN);''')
conn.commit()

# ------------------------- RESPUESTAS DE MUSICA ------------------------------------
# 1
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Los brillos bajo los ojos", 1, "Musica", 1);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Tener el cuerpo con muchos tatuajes", 0, "Musica", 1);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Tener muchos piercings", 0, "Musica", 1);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todas son Correctas ", 0, "Musica", 1);""")
conn.commit()

# 2
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("No vendo Trap", 1, "Musica", 2);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Loca", 0, "Musica", 2);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Givenchy", 0, "Musica", 2);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Perreo  bendito", 0, "Musica", 2);""")
conn.commit()

# 3
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("ya quiero que te vayas", 0, "Musica", 3);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Será que no me amas", 1, "Musica", 3);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Será que me amas", 0, "Musica", 3);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ninguna de las anteriores", 0, "Musica", 3);""")
conn.commit()

# 4
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lit Killah", 0, "Musica", 4);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Neo Pistea", 0, "Musica", 4);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Dillom", 1, "Musica", 4);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("YSY A", 0, "Musica", 4);""")
conn.commit()

# 5
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Promesas Sobre el bidet", 0, "Musica", 5);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Los años salvajes", 1, "Musica", 5);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Demoliendo Hoteles", 0, "Musica", 5);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Rezo por vos", 0, "Musica", 5);""")
conn.commit()

# 6
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Carlos Baute y Marta Sanchez", 1, "Musica", 6);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Carlos Baute", 0, "Musica", 6);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Carlos Baute y Thalia", 0, "Musica", 6);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Thalía y David Bisbal", 0, "Musica", 6);""")
conn.commit()

# 7
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Andres Calamaro", 0, "Musica", 7);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Luis Alberto Spinetta", 0, "Musica", 7);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Gustavo Cerati", 0, "Musica", 7);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Fito Paez", 1, "Musica", 7);""")
conn.commit()

# 8
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Benito Antonio Martínez Ocasio", 1, "Musica", 8);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Emmanuel Gazmey Santiago", 0, "Musica", 8);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Noel Santos Román", 0, "Musica", 8);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("José Daniel Betances", 0, "Musica", 8);""")
conn.commit()

# 9
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Freddie Mercury", 0, "Musica", 9);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Roger Taylor", 0, "Musica", 9);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Brian May", 0, "Musica", 9);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Peter Criss", 0, "Musica", 9);""")
conn.commit()

# 10
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Para Elisa", 0, "Musica", 10);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La Flauta Mágica", 1, "Musica", 10);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Marcha Turca", 0, "Musica", 10);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Himno a la Alegría", 0, "Musica", 10);""")
conn.commit()

# 11
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La Renga", 0, "Musica", 11);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Intoxicados", 0, "Musica", 11);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Los piojos", 1, "Musica", 11);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Las Pelotas", 0, "Musica", 11);""")
conn.commit()

# 12
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Pity Álvarez", 0, "Musica", 12);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Emiliano Branccia", 0, "Musica", 12);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Rolando Sartori", 0, "Musica", 12);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ricardo Mollo", 1, "Musica", 12);""")
conn.commit()

# 13
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Taylor Swift", 0, "Musica", 13);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lady Gaga", 1, "Musica", 13);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ariana Grande", 0, "Musica", 13);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Britney Spears", 1, "Musica", 13);""")
conn.commit()

# 14
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Rolling Stones", 1, "Musica", 14);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Pink Floyd", 0, "Musica", 14);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("AC/DC", 0, "Musica", 14);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Metallica", 0, "Musica", 14);""")
conn.commit()

# 15
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lover", 0, "Musica", 15);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Taylor Swift (Taylor's version)", 1, "Musica", 15);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Red", 0, "Musica", 15);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Evermore", 0, "Musica", 15);""")
conn.commit()

# 16
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ángela Torres", 0, "Musica", 16);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Miguel Ángel Rodríguez", 1, "Musica", 16);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Natalia Oreiro", 0, "Musica", 16);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lali Espósito", 0, "Musica", 16);""")
conn.commit()

# 17
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Sin pena ni gloria", 1, "Musica", 17);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Campanas en la noche", 0, "Musica", 17);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ambas", 0, "Musica", 17);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ninguna de las anteriores", 0, "Musica", 17);""")
conn.commit()

# 18
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Obras cumbres", 1, "Musica", 18);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ruido blanco", 0, "Musica", 18);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Zona de promesas", 0, "Musica", 18);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Sueño stereo", 0, "Musica", 18);""")
conn.commit()

# 19
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Callejeros", 0, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("No pertenecío a ninguna banda", 0, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Calle 13", 1, "Musica", 19);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Los tigres del Norte", 0, "Musica", 19);""")
conn.commit()

# 20
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Chambean", 0, "Musica", 20);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Jangueo", 0, "Musica", 20);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Pa’ que retozen", 0, "Musica", 20);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todas lo son", 1, "Musica", 20);""")
conn.commit()

# 21 
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Norberto Aníbal Napolitano", 1, "Musica", 21);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Alejandro Andrés Lococo", 0, "Musica", 21);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Luciano Napolitano", 0, "Musica", 21);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Adrián Otero", 0, "Musica", 21);""")
conn.commit()

# 22
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Daniel Agostini", 0, "Musica", 22);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ulises Bueno", 0, "Musica", 22);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Walter Olmos", 0, "Musica", 22);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Leo Mattioli", 1, "Musica", 22);""")
conn.commit()

# 23
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Daniel Agostini", 0, "Musica", 23);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ulises Bueno", 0, "Musica", 23);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Walter Olmos", 0, "Musica", 23);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Leo Mattioli", 1, "Musica", 23);""")
conn.commit()

# 24
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Roar", 0, "Musica", 24);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("I kissed a girl", 1, "Musica", 24);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Dark horse", 0, "Musica", 24);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("E.T", 0, "Musica", 24);""")
conn.commit()

# ------------------------------ RESPUESTAS DE CINE ---------------------------------------

# 1)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Una jirafa", 0, "Cine", 25);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Un ratón", 0, "Cine", 25);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Un cuervo", 0, "Cine", 25);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Un elefante", 1, "Cine", 25);""")
conn.commit()

# 2)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Un perro de juguete", 0, "Cine", 26);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Un tenedor de plástico", 0, "Cine", 26);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Una cuchara descartable", 1, "Cine", 26);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Una papa", 0, "Cine", 26);""")
conn.commit()

# 3)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("15", 0, "Cine", 27);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("8", 0, "Cine", 27);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("11", 1, "Cine", 27);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("9", 0, "Cine", 27);""")
conn.commit()

# 4)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Derek", 0, "Cine", 28);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("George", 0, "Cine", 28);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lexie", 0, "Cine", 28);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todos lo hacen", 1, "Cine", 28);""")
conn.commit()

# 5)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("5", 0, "Cine", 29);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("8", 1, "Cine", 29);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("4", 0, "Cine", 29);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("7", 0, "Cine", 29);""")
conn.commit()

# 6)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Otis", 0, "Cine", 30);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Maeve", 0, "Cine", 30);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Dra. Jean", 0, "Cine", 30);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Otis y Maeve", 1, "Cine", 30);""")
conn.commit()

# 7)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Uno", 0, "Cine", 31);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Dos", 0, "Cine", 31);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Cuatro", 0, "Cine", 31);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Seis", 1, "Cine", 31);""")
conn.commit()

# 8)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Guillermo Francella", 0, "Cine", 32);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Pablo Rago", 0, "Cine", 32);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ricardo DArín", 1, "Cine", 32);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("José Luis Gioia", 0, "Cine", 32);""")
conn.commit()

# 9)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Franco Masini", 0, "Cine", 33);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Stefania Koessl", 0, "Cine", 33);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Fernando Miró", 0, "Cine", 33);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lorenzo Ferro", 1, "Cine", 33);""")
conn.commit()

# 10)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Luis Ortega", 1, "Cine", 34);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Pablo Trapero", 0, "Cine", 34);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Adrián Suar", 0, "Cine", 34);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Damián Szifron", 0, "Cine", 34);""")
conn.commit()

# 11)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Rory y Lorelai", 1, "Cine", 35);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Emily y Lorelai", 0, "Cine", 35);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Emily y Rory", 0, "Cine", 35);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("París y Rory", 0, "Cine", 35);""")
conn.commit()

# 12)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lucía", 0, "Cine", 36);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Raquel", 1, "Cine", 36);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Alicia", 0, "Cine", 36);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Francesca", 0, "Cine", 36);""")
conn.commit()

# 13)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Argentina, Tierra de amor y venganza", 0, "Cine", 37);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Solamente vos", 0, "Cine", 37);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Esperanza mía", 0, "Cine", 37);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El clo", 1, "Cine", 37);""")
conn.commit()

# 14)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Floricienta", 0, "Cine", 38);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Patito Feo", 0, "Cine", 38);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La malparida", 1, "Cine", 38);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Rebelde Way", 0, "Cine", 38);""")
conn.commit()

# 15)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Regina George", 0, "Cine", 39);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Cady Heron", 0, "Cine", 39);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Gretchen Wieners", 1, "Cine", 39);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Sharon Norbury", 0, "Cine", 39);""")
conn.commit()

# 16)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Diez", 0, "Cine", 40);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ocho", 1, "Cine", 40);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Siete", 0, "Cine", 40);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Nueve", 0, "Cine", 40);""")
conn.commit()

# 17)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Vendedor de autos", 1, "Cine", 41);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Arquitecto", 0, "Cine", 41);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Vendedor de casas", 0, "Cine", 41);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("No trabajaba", 0, "Cine", 41);""")
conn.commit()

# 18)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El robo del siglo", 0, "Cine", 42);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ciudadano kane", 1, "Cine", 42);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La casa de papel", 0, "Cine", 42);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("En ninguna aparece esa frase", 0, "Cine", 42);""")
conn.commit()

# 19)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Mark Wahlberg", 0, "Cine", 43);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Dominic Holland", 0, "Cine", 43);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Andrew Garfield", 0, "Cine", 43);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Tom Holland", 1, "Cine", 43);""")
conn.commit()

# 20)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("George Lucas", 1, "Cine", 44);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Gareth Edwars", 0, "Cine", 44);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("J.K Rowling", 0, "Cine", 44);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ninguno de ellos", 0, "Cine", 44);""")
conn.commit()

# 21)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Diez", 0, "Cine", 45);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ocho", 1, "Cine", 45);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Nueve", 0, "Cine", 45);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Siete", 0, "Cine", 45);""")
conn.commit()

# 22)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Aria, Hanna, Emily, Spencer y Alison", 1, "Cine", 46);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Aria, Hanna, Emily y Spencer", 0, "Cine", 46);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ashley, Ella y Emily", 0, "Cine", 46);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Emily, Mona y Spencer", 0, "Cine", 46);""")
conn.commit()

# 23)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Nicolas Hammond", 0, "Cine", 47);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Shinji Toudou", 0, "Cine", 47);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Reeve Carney", 0, "Cine", 47);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todos lo interpretaron", 1, "Cine", 47);""")
conn.commit()

# 24)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Buenos muchachos", 0, "Cine", 48);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El padrino", 1, "Cine", 48);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Sueño de fuga", 0, "Cine", 48);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Tiempos violentos", 0, "Cine", 48);""")
conn.commit()
# ---------------------------- RESPUESTAS DE LIBROS ---------------------------------------

# 1)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("1782", 0, "Libros", 49);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("1872", 0, "Libros", 49);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "1982", 1, "Libros", 49);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "1975", 0, "Libros", 49);""")
conn.commit()

# 2)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Luis Velasco", 1, "Libros", 50);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Angel Velasco", 0, "Libros", 50);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ariel Velasco", 0, "Libros", 50);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ninguno de ellos", 0, "Libros", 50);""")
conn.commit()

# 3)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                (contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Dramático", 1, "Libros", 51);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Narrativo", 0, "Libros", 51);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Lírico", 0, "Libros", 51);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Didáctico", 0, "Libros", 51);""")
conn.commit()

# 4)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Historia de dos ciudades", 0, "Libros", 52);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Calle Sin Salida", 0, "Libros", 52);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("The Frozen Deep", 0, "Libros", 52);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todas lo son", 1, "Libros", 52);""")
conn.commit()

# 5)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Lenore", 0, "Libros", 54);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El gato negro", 1, "Libros", 53);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La carta Robada", 0, "Libros", 53);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Silencio", 0, "Libros", 53);""")
conn.commit()

# 6)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Edgar Allan Poe", 0, "Libros", 54);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Julio Cortazar", 0, "Libros", 54);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ruben Dario", 0, "Libros", 54);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Horacio Quiroga", 1, "Libros", 54);""")
conn.commit()

# 7)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La inquietud del Rosal", 1, "Libros", 55);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Poemas de amor", 0, "Libros", 55);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Antologia Poetica", 0, "Libros", 55);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                (220, "Languidez", 0, "Libros", 55);""")
conn.commit()

# 8)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Alfonsina Storni", 0, "Libros", 56);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Nicanor Parra", 0, "Libros", 56);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Gabriela Mistral", 1, "Libros", 56);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Miguel Angel Asturias", 0, "Libros", 56);""")
conn.commit()

# 9)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todos lo son", 0, "Libros", 57);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Desolación", 0, "Libros", 57);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Tala", 0, "Libros", 57);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Canto General", 1, "Libros", 57);""")
conn.commit()

# 10)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Cien años de soledad", 0, "Libros", 58);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "El amor es los tiempos del cólera", 0, "Libros", 58);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Memoria de mis putas tristes", 0, "Libros", 58);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Cien sonetos de amor", 1, "Libros", 58);""")
conn.commit()

# 11)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Julio Cortazar", 0, "Libros", 59);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Jorge Luis Borges", 0, "Libros", 59);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Gabriel Garcia Marquez", 1, "Libros", 59);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Pablo Neruda", 0, "Libros", 59);""")
conn.commit()

# 12)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Acantilado", 0, "Libros", 60);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ariel", 0, "Libros", 60);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La Esfera de los Libros", 0, "Libros", 60);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todas lo son", 1, "Libros", 60);""")
conn.commit()

# 13)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("De verdad", 0, "Libros", 61);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "De Sanación", 1, "Libros", 61);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "De paz", 0, "Libros", 61);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Del amor", 0, "Libros", 61);""")
conn.commit()

# 14)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Vanessa Bell", 0, "Libros", 62);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Katherine Mansfield", 0, "Libros", 62);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Virginia Woolf", 1, "Libros", 62);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Jane Austen", 0, "Libros", 62);""")
conn.commit()

# 15)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Sentey", 0, "Libros", 63);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Escape", 0, "Libros", 63);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Soma", 1, "Libros", 63);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Vasri", 0, "Libros", 63);""")
conn.commit()

# 16)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Munich", 1, "Libros", 64);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Nuremberg", 0, "Libros", 64);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Stuttgart", 0, "Libros", 64);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Colonia", 0, "Libros", 64);""")
conn.commit()

# 17)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Síndrome de Guillain-Barré", 0, "Libros", 65);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Cáncer", 0, "Libros", 65);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Síndrome de down", 0, "Libros", 65);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Síndrome de Treacher Collins", 1, "Libros", 65);""")
conn.commit()

# 18)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ser menos vanidosa, tímida, egoísta y tosca", 1, "Libros", 66);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ser más responsables", 0, "Libros", 66);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Ser menos aburridas, molestas y crueles", 0, "Libros", 66);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Ser más amables, encantadoras, originales y pacientes", 0, "Libros", 66);""")
conn.commit()

# 19)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Arcadio y Jose Arcadio Segundo", 0, "Libros", 67);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Aurellano Jose y Arcadio", 1, "Libros", 67);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Aureliano y Mauricio Babilonia", 0, "Libros", 67);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Meme y Rebeca", 0, "Libros", 67);""")
conn.commit()

# 20)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Existencialismo", 0, "Libros", 68);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Positivismo", 0, "Libros", 68);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Absurdismo", 1, "Libros", 68);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Racionalismo", 0, "Libros", 68);""")
conn.commit()

# 21)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Animales fantásticos y dónde encontrarlos", 0, "Libros", 69);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Harry Potter y la piedra filosofal", 0, "Libros", 69);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Harry Potter y el misterio del príncipe", 0, "Libros", 69);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "Harry Potter y el prisionero de Azkaban", 1, "Libros", 69);""")
conn.commit()

# 22)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La Biblia", 1, "Libros", 70);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La saga de 'Harry Potter'", 0, "Libros", 70);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El Alquimista", 0, "Libros", 70);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El Señor de los anillos", 0, "Libros", 70);""")
conn.commit()

# 23)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("La vejez", 0, "Libros", 71);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El segundo sexo", 1, "Libros", 71);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ( "La mujer rota", 0, "Libros", 71);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Todos los hombres son mortales", 0, "Libros", 71);""")
conn.commit()

# 24)
conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Don Quijote de la Mancha", 0, "Libros", 72);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Crimen y castigo", 0, "Libros", 72);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("El principito", 1, "Libros", 72);""")
conn.commit()

conn.execute("""INSERT OR IGNORE INTO Respuestas
                ( contenido_respuesta, es_correcta, categoria, id_pregunta)
            VALUES
                ("Pedro Paramo", 0, "Libros", 72);""")
conn.commit()