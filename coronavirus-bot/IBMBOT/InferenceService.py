import random

from IBMBOT.dbOperations import DbOperation
from IBMBOT.loadapi import API

DbOperation = DbOperation()
API = API()


class InferenceService:
    def __init__(self):
        pass

    def inference(self, text, ani, loading):
        """ Main inference logic"""

        session_id = DbOperation.db_select(ani, loading)
        if not session_id:
            session_id = API.session_API(loading)
            db_results = DbOperation.db_insert(session_id, ani, loading)
            if not db_results:
                return False
            final_response, url = API.message_API(loading, text, session_id)
        else:
            response, url = API.message_API(loading, text, session_id)
            if not response:
                session_id = API.session_API(loading)
                db_results = DbOperation.db_update(session_id, ani, loading)
                if not db_results:
                    return False
                final_response, url = API.message_API(loading, text, session_id)
            else:
                final_response, url = response, url

        return final_response, url

    @staticmethod
    def randomize(listrandom):
        """Randomizer"""

        random.shuffle(listrandom)
        select_1 = listrandom[0]

        return select_1
