from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from greeting_app.application.use_cases import GreetPersonUseCase

class GreetPersonView(APIView):
    def post(self, request):
        name = request.data.get("nombre")
        use_case = GreetPersonUseCase()

        try:
            greeting_message = use_case.execute(name=name)
            return Response(
                {"mensaje": greeting_message},
                status=status.HTTP_200_OK
            )
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )