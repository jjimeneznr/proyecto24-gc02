import oracledb as db
#from . import database

def dbConectar():
    ip = "localhost"
    puerto = 1521
    s_id = "xe"

    usuario = "system"
    contrasena = "12345"

    print("---dbConectar---")
    print("---Conectando a Oracle---")

    try:
        conexion = db.connect(user=usuario, password=contrasena, host=ip, port=puerto, sid=s_id)
        print("Conexión realizada a la base de datos",conexion)
        return conexion
    except db.DatabaseError as error:
        print("Error en la conexión")
        print(error)
        return None

def dbSignUp(email=str, firstName=str, secondName=str, password1=str, password2=str):
    print("---dbSignUp---")
    
    try:
        cursor = conexion.cursor()
        print(email)
        print(firstName)
        print(secondName)
        print(password1)
        print(password2)
        consulta = "INSERT INTO asee_users VALUES(:email, :firstName, :secondName, :password1)"
        if(password1 == password2):
            cursor.execute(consulta, [email, firstName, secondName, password1])
            print("Tupla insertada correctamente")
            print('------------------------------')
            cursor.close()
            conexion.commit()
            return True
        else:
            print("Error: Las contraseñas no coinciden")
            cursor.close()
            return False
    except db.DatabaseError as error:
        print("Error. No se ha podido crear el usuario")
        print(error)
        return False

def dbLogIn(email=str, password=str):
    print("---dbLogIn---")

    try:
        cursor = conexion.cursor()
        print(email)
        print(password)
        consulta = "SELECT email, passwd FROM asee_users WHERE email = :email AND passwd = :password"
        cursor.execute(consulta, [email, password])
        resul = cursor.fetchone()
        if(cursor.rowcount == 1):
            print("Usuario encontrado correctamente")
            if(resul[1] == password):
                print('Usuario y contraseña correctos')
            else:
                print('La contraseña no es correcta')
                return False
        else:
            print("Usuario no existente:",cursor.rowcount)
            return False
        print('------------------------------')
        cursor.close()
        conexion.commit()
        return True
    except db.DatabaseError as error:
        print("Error. No se ha podido iniciar sesión")
        print(error)
        return False

def dbPrint():
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_users"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total usuarios:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No hay nada")

def dbGetActors():
    print("---dbGetActors---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_actors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total actores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los actores")
        print(error)

def dbGetActor(actor_id):
    print("---dbGetActor---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_actors WHERE actor_id = :actor_id"
        cursor.execute(consulta, [actor_id,])
        for tupla in cursor:
            print(tupla)
        print("Total actores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener el actor")
        print(error)

def dbGetDirectors():
    print("---dbGetDirectors---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_directors"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total directores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener los directores")
        print(error)

def dbGetEpisodes():
    print("---dbGetEpisodes---")

def dbGetSeasons():
    print("---dbGetSeasons---")

def dbGetSeries():
    print("---dbGetSeries---")

def dbGetMovies():
    print("---dbGetMovies---")

    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM asee_movies"
        cursor.execute(consulta)
        for tupla in cursor:
            print(tupla)
        print("Total películas:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas")
        print(error)

def dbGetActorsInMovie(movie_id):
    print("---dbGetActorsInMovie---")
    try:
        cursor = conexion.cursor()
        consulta = "SELECT actor, actor_role FROM asee_actor_movie WHERE movie = :movie_id"
        cursor.execute(consulta, [movie_id,])
        for tupla in cursor:
            print(tupla)
        print("Total actores:", cursor.rowcount)
        cursor.close()
    except db.DatabaseError as error:
        print("Error: No se pueden obtener las películas")
        print(error)

conexion = dbConectar()