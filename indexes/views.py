from rest_framework.views import APIView
from rest_framework.response import Response
from joblib import load
from scraper.scraper import FinanceScraper
from .utils import utils
from RengoApi import settings
from os import listdir
import os


class DAX(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = load(settings.BASE_DIR + "/RengoApi/models/DAX.joblib")
        self.scraper = FinanceScraper()

    def get(self, request):
        return Response(
            utils.calculate_response("INDEXDB: DAX", self.scraper, self.model)
        )


class NYSEComposite(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scraper = FinanceScraper()
        self.model = load(settings.BASE_DIR + "/RengoApi/models/NYSE.joblib")

    def get(self, request):
        return Response(
            utils.calculate_response("INDEXNYSEGIS: NYA", self.scraper, self.model)
        )
