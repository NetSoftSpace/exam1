from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company.models import Company, Vacancy, Resume


class StatCountApi(APIView):

    def get(self, request):
        company = Company.objects.all().count()
        vacancy = Vacancy.objects.all().count()
        resume = Resume.objects.all().count()

        context = {"companies": company, "vacancies": vacancy, "resumies":resume}

        return Response(context)
