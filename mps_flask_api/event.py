from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H;%M,%S"))


def read_all():
    from app import MYSQL_DB
    cursor = MYSQL_DB.connection.cursor()
    cursor.execute("select * from agenda_evento;")
    events_db = cursor.fetchall()
    json = []
    for event in events_db:
        json.append({
            "evento_id": event[0],
            "evento_data_hora": event[1],
            "evento_descricao": event[2],
            "evento_nome": event[3],
            "evento_status": event[4],
            "usuario_id": event[5]
        })
    return json


def create(event):
    from app import MYSQL_DB
    event_id = event.get("event_id")
    event_name = event.get("event_name", "")
    event_description = event.get("event_description", "")
    event_date_hour = event.get("event_date_hour", "")
    event_status = event.get("event_status")
    user_id = event.get("user_id")

    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"insert into agenda_evento(evento_id, evento_data_hora, evento_descricao, evento_nome, \
                       evento_status, usuario_id) values ('{event_id}', '{event_date_hour}', '{event_description}', \
                       '{event_name}', '{event_status}','{user_id}');")
        MYSQL_DB.connection.commit()
        cursor.close()
    except:
        abort(
            406,
            f"Event with id {event_id} already exits",
        )


def read_one(event_id):
    from app import MYSQL_DB
    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"select * from agenda_evento where evento_id='{event_id}';")
        event_db = cursor.fetchall()
        json = {
            "evento_id": event_db[0][0],
            "evento_data_hora": event_db[0][1],
            "evento_descricao": event_db[0][2],
            "evento_nome": event_db[0][3],
            "evento_status": event_db[0][4],
            "usuario_id": event_db[0][5]
        }
        return json
    except:
        abort(
            404, f"Event with ID {event_id} not found"
        )


def update(event_id, event):
    from app import MYSQL_DB
    event_date_hour = event.get("event_date_hour")
    event_description = event.get("event_description")
    event_name = event.get("event_name")
    event_status = event.get("event_status")

    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"update agenda_evento set evento_data_hora='{event_date_hour}', \
                       evento_descricao='{event_description}', evento_nome='{event_name}', \
                       evento_status='{event_status}' where evento_id={event_id};")
        MYSQL_DB.connection.commit()
        cursor.close()
    except:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )


def delete(event_id):
    from app import MYSQL_DB
    try:
        cursor = MYSQL_DB.connection.cursor()
        cursor.execute(f"delete from agenda_evento where evento_id={event_id};")
        MYSQL_DB.connection.commit()
        cursor.close()
    except:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )