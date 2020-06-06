import requests


class API:
    def __init__(self):
        pass

    def session_API(self, loading):
        """Session API"""

        querystring = dict()
        for session_params in loading.session_url_params:
            querystring[session_params['param_name']] = session_params['param_value']  # noqa

        headers = dict()
        for session_header in loading.session_headers:
            headers[session_header['header_name']] = session_header['header_value']

        session_response = requests.request(
            loading.session_url_method_type, loading.session_url,
            headers=headers, params=querystring)
        session_response = session_response.json()

        return session_response.get('session_id')

    def message_API(self, loading, text, session_id):
        """Message API"""

        querystring = dict()
        for predict_params in loading.predict_url_params:
            querystring[predict_params['param_name']] = predict_params['param_value']  # noqa

        headers = dict()
        for predict_header in loading.predict_headers:
            headers[predict_header['header_name']] = predict_header['header_value']

        payload = dict()
        for predict_payload in loading.predict_url_raw_params:
            if predict_payload['param_type'] == 'evaluate':
                if predict_payload['param_value'] == '%text%':
                    payload[predict_payload['param_name']] = {"text": text}
            else:
                payload[predict_payload['param_name']] = {"text": predict_payload['param_value']}

        url = loading.predict_url
        url = url.replace('<session_id>', session_id)
        predict_response_status = requests.request(
            loading.predict_url_method_type, url,
            headers=headers, params=querystring, json=payload)
        predict_response = predict_response_status.json()

        predict_final_response = list()
        url = list()

        if predict_response_status.status_code == 404:
            return predict_final_response, url
        if predict_response_status.ok:
            for predict_final in predict_response['output']['generic']:
                for label, value in predict_final.items():
                    if label == 'text':
                        predict_final_response.append(predict_final.get('text'))
                    elif label == 'source':
                        url.append(predict_final.get('source'))

        return predict_final_response, url
