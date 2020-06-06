import ibm_db


class DbOperation:
    def __init__(self):
        pass

    def db_select(self, ani, loading):
        """db select"""

        db2conn = ibm_db.connect(loading.db_link, loading.db_username, loading.db_password)
        if db2conn:
            sql = "SELECT SESSION_ID FROM AFRIEND WHERE ANI=?"
            stmt = ibm_db.prepare(db2conn, sql)
            ibm_db.bind_param(stmt, 1, ani)
            ibm_db.execute(stmt)
            result = ibm_db.fetch_assoc(stmt)
            if not result:
                return False
            ibm_db.close(db2conn)
            return result.get('SESSION_ID')

    def db_update(self, session_id, ani, loading):
        """db update"""

        try:
            db2conn = ibm_db.connect(loading.db_link, loading.db_username, loading.db_password)
            if db2conn:
                sql = "UPDATE AFRIEND SET SESSION_ID = ? WHERE ANI = ?"
                stmt = ibm_db.prepare(db2conn, sql)
                ibm_db.bind_param(stmt, 1, session_id)
                ibm_db.bind_param(stmt, 2, ani)
                ibm_db.execute(stmt)
                return True
        except Exception as e:
            return False

    def db_insert(self, session_id, ani, loading):
        """db insert"""

        try:
            db2conn = ibm_db.connect(loading.db_link, loading.db_username, loading.db_password)
            if db2conn:
                sql = "INSERT INTO  AFRIEND(ANI,SESSION_ID) VALUES(?,?)"
                stmt = ibm_db.prepare(db2conn, sql)
                ibm_db.bind_param(stmt, 1, ani)
                ibm_db.bind_param(stmt, 2, session_id)
                ibm_db.execute(stmt)
                return True
        except Exception as e:
            return False
