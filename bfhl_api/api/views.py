from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

class BFHLView(APIView):
    def post(self, request):
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            input_data = data.get('data', [])
            
            numbers = [str(item) for item in input_data if str(item).isdigit()]
            alphabets = [str(item) for item in input_data if str(item).isalpha()]
            highest_lowercase = max((char for char in alphabets if char.islower()), default='')
            
            response = {
                "is_success": True,
                "user_id": "aniket_saxena_21bce8842",
                "email": "aniket.21bce8842@vitapstudent.ac.in",
                "roll_number": "21BCE8842",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
            }
            
            return Response(response)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON input"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        return Response({"operation_code": 1})