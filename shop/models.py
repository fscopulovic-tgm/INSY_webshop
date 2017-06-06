from django.db import models


class Land(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Adresse(models.Model):
    strasse = models.CharField(max_length=255)
    hnr = models.IntegerField()
    plz = models.CharField(max_length=20)
    ort = models.CharField(max_length=255)
    land = models.ForeignKey(Land, on_delete=models.PROTECT)

    def __str__(self):
            return '{} {}, {} {} - {}'.format(self.strasse, self.hnr, self.plz, self.ort, self.land)

    class Meta:
        verbose_name_plural = "Adressen"


class Artikel(models.Model):
    artikelnummer = models.IntegerField(primary_key=True)
    artikelbez = models.CharField(max_length=255)
    npreis = models.DecimalField(max_digits=7, decimal_places=2)
    verfuegbareStucke = models.SmallIntegerField()
    artikelinfo = models.CharField(max_length=255)

    def __str__(self):
        return 'Anr: {} , Abez: {}'.format(self.artikelnummer, self.artikelbez)


class Kunde(models.Model):
    name = models.CharField(max_length=255)
    knr = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)
    feedbackKunde = models.ManyToManyField(Artikel, through="Feedback")
    zuletzt_online = models.DateField(null=True)

    def __str__(self):
        return 'Name: {}, Email: {}'.format(self.name, self.email)


class Bestellung(models.Model):
    bestellnummer = models.IntegerField(primary_key=True)
    datum = models.DateField()
    bestatus = models.CharField(max_length=255)
    kunde = models.OneToOneField(Kunde, on_delete=models.CASCADE)
    lieferabez = models.CharField(max_length=255)
    rechnungabez = models.CharField(max_length=255)
    artikel = models.ManyToManyField(Artikel, through="Bestellartikel")

    def __str__(self):
        return 'Bestellnr: {}, Datum: {}, Bestatus: {}, Kundennr: {}'\
               .format(self.bestellnummer, self.datum, self.bestatus, self.kunde.knr)


class Bestellartikel(models.Model):
    artikel = models.OneToOneField(Artikel, on_delete=models.CASCADE)
    bestell = models.OneToOneField(Bestellung, on_delete=models.CASCADE)
    anzahl = models.IntegerField()

    def __str__(self):
        return 'Artikel: {}, Bestellung: {}, Anzahl: {}'\
            .format(self.artikel.artikelnummer, self.bestell.bestellnummer, self.anzahl)


class Feedback(models.Model):
    artikel = models.OneToOneField(Artikel, on_delete=models.CASCADE)
    kunde = models.OneToOneField(Kunde, on_delete=models.CASCADE)
    feedbackdatum = models.DateField()

    def __str__(self):
        return 'Knr: {}, Anr: {}, Datum: {}, Bewertung: {}'\
            .format(self.kunde.knr, self.artikel.artikelnummer, self.feedbackdatum, self.feedbackbewertung)


class Bluray(Artikel):
    spieldauer = models.TimeField()
    regie = models.CharField(max_length=255)
    verjahr = models.DateField()
    genre = models.CharField(max_length=255)

    def __str__(self):
        return 'Anr: {}, Dauer: {}, Regie: {}, Genre: {}'\
            .format(self.artikelnummer, self.spieldauer, self.regie, self.genre)


class Buch(Artikel):
    seitenanzahl = models.IntegerField()
    autor = models.CharField(max_length=255)
    verlag = models.CharField(max_length=255)
    isbn = models.IntegerField()

    def __str__(self):
        return 'Anr: {}, Seiten: {}, Autor: {}, ISBN: {}'\
            .format(self.artikelnummer, self.seitenanzahl, self.autor, self.isbn)


class SonstigerArtikel(Artikel):
    pass
