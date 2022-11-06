import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

class TestVarasto2(unittest.TestCase):
    def setUp(self):
        self.tyhja_varasto = Varasto(-1)
        self.varasto = Varasto(3, alku_saldo=-1)

    def test_konstruktori_luo_tyhjan_varaston_neg_tilavuudella(self):
        self.assertAlmostEqual(self.tyhja_varasto.tilavuus, 0)

    def test_konstruktori_nollaa_neg_saldon(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

class TestVarasto3(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(5, alku_saldo=6)

    def test_varasto_ei_hyvaksy_tilavuutta_enempaa(self):
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_varasto_ei_hyvaksy_neg_lisaysta(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_varaston_saldo_ei_ylivuoda(self):
        self.varasto.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_varastosta_ei_saa_neg_maaraa(self):
        otettu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otettu_maara, 0)

    def test_varastosta_ei_saa_saldoa_enempaa(self):
        koko_varaston_saldo = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(koko_varaston_saldo, 5)

    def test_saldo_voidaan_tulostaa(self):
        print(str(self.varasto))
