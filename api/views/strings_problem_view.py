from rest_framework.views import APIView
from rest_framework.response import Response
import json

class StringsProblemView(APIView):
    @staticmethod
    def calculate_max_value(string):
        max_value = 0
        for i in range(len(string)):
            for j in range(i + 1, len(string) + 1):
                substring = string[i:j]
                # formula
                value = len(substring) * StringsProblemView.count_occurrences(substring, string)
                max_value = max(max_value, value)

        return max_value

    @staticmethod
    def count_occurrences(substring, string):
        count = 0
        index = 0

        while True:
            index = string.find(substring, index)
            if index == -1:
                break
            count += 1
            index += 1

        return count
    
    def post(self, request):
        body = request.body.decode('utf-8')
        data = json.loads(body)
        string = data['string']

        max_value = self.calculate_max_value(string)
        response = {
            'message': 'Maximum value obtained',
            'data': {
                'max_value': max_value
            },
            'success': True
        }
        return Response(response)