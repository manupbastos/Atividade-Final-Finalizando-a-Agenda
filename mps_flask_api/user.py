from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H;%M,%S"))


def read_all():
    from app import MYSQL_DB
    cursor = MYSQL_DB.connection.cursor()
    cursor.execute("select * from agenda_usuario;")
    users_db = cursor.fetchall()
    json = []
    for user in users_db:
        json.append({
            "usuario_id": user[0],
            "usuario_nome": user[1],
            "usuario_email": user[2],
            "usuario_status": user[3],
            "usuario_senha": user[4]
        })
    return json


def create(user):
    from app import MYSQL_DB
    user_id = user.get("user_id")
    user_name = user.get("user_name", "")
    user_email = user.get("user_email", "")
    user_status = user.get("user_status", "")
    user_password = user.get("user_password", "")

    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"insert into agenda_usuario(usuario_id, usuario_nome, usuario_email, usuario_status, usuario_senha) \
                    values ('{user_id}', '{user_name}', '{user_email}', '{user_status}', '{user_password}')")
        MYSQL_DB.connection.commit()
        cursor.close()
    except:
        abort(
            406,
            f"User with last name {user_id} already exits",
        )


def read_one(user_id):
    from app import MYSQL_DB
    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"select * from agenda_usuario where usuario_id='{user_id}';")
        user_db = cursor.fetchall()
        print(str(user_db))
        json = {
            "usuario_id": user_db[0][0],
            "usuario_nome": user_db[0][1],
            "usuario_email": user_db[0][2],
            "usuario_status": user_db[0][3],
            "usuario_senha": user_db[0][4]
        }
        return json
    except:
        abort(
            404, f"Person with ID {user_id} not found"
        )


def update(user_id, user):
    from app import MYSQL_DB
    usuario_nome = user.get("user_name")
    usuario_email = user.get("user_email")
    usuario_status = user.get("user_status")
    usuario_senha = user.get("user_password")

    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"update agenda_usuario set usuario_nome='{usuario_nome}', usuario_email='{usuario_email}', \
                       usuario_status='{usuario_status}', usuario_senha='{usuario_senha}' where usuario_id={user_id};")
        MYSQL_DB.connection.commit()
        cursor.close()
    except:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )


def delete(user_id):
    from app import MYSQL_DB
    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"delete from agenda_usuario where usuario_id='{user_id}';")
        MYSQL_DB.connection.commit()
        cursor.close()
    except:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )