from django.test import TestCase
from .models import Colheitas

# Create your tests here.
class ColheitasModelTest(TestCase):
    def test_criação_colheita(self):
        colheita = Colheitas.objects.create(
            cultura="Trigo",
            data_plantio="2023-01-01",
            data_colheita="2023-06-01",
            quantidade_colhida=100.0
        )
        self.assertEqual(colheita.cultura, "Trigo")
        self.assertEqual(colheita.data_plantio, "2023-01-01")
        self.assertEqual(colheita.data_colheita, "2023-06-01")
        self.assertEqual(colheita.quantidade_colhida, 100.0)

    def test_cultura_max_length(self):
        colheita = Colheitas.objects.create(
            cultura="Milho muito longo que excede o limite do campo de texto",
            data_plantio="2023-02-01",
            data_colheita="2023-07-01",
            quantidade_colhida=200.0
        )
        max_length = colheita._meta.get_field("cultura").max_length
        self.assertLessEqual(len(colheita.cultura), max_length)

    def test_quantidade_colhida_negativa(self):
        with self.assertRaises(ValueError):
            Colheitas.objects.create(
                cultura="Soja",
                data_plantio="2023-03-01",
                data_colheita="2023-08-01",
                quantidade_colhida=-50.0
            )