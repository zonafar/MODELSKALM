from django.db import models
from missions.models import Produits , Clients

class depenseMissions(models.Model):
    DEPENSES_TYPES = (
        ('carburant', 'carburant'),
        ('frais du transport', 'frais du transport'),
        ('frais de douane', 'frais de douane')
    )

    intitule = models.CharField(max_length=250, choices=DEPENSES_TYPES, default='carburant', unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['intitule']

    def __str__(self):
        return self.intitule 

class Missions(models.Model):
    infosDepenses = models.ManyToManyField(
        depenseMissions, through="CoutDepensesMission", through_fields=('depenseNom','missionConsernee')
        )

    produitsTransport =models.ManyToManyField(
        Produits, through="RecetteMissions", through_fields=('produitTransportes','missionConsernee')
        )

    @property
    def total_recette(self):
        return "cout total des recettes"
    
    @property
    def total_depense(self):
        return "total des depenses"
 
class CoutDepensesMission(models.Model):
    cout = models.DecimalField(max_digits=19, decimal_places=10)
    depenseNom = models.ForeignKey(depenseMissions, related_name='cout_depenses', on_delete=models.CASCADE)
    missionConsernee = models.ForeignKey(Missions, related_name='cout_depenses', on_delete=models.CASCADE)

class RecetteMissions(models.Model):
    clientConsernee = models.ForeignKey(Clients, related_name='mission', on_delete=models.CASCADE)
    missionConsernee = models.ForeignKey(Missions, related_name='recette', on_delete=models.CASCADE)
    produitTransportes = models.ForeignKey(Produits, related_name='recette', on_delete=models.CASCADE)
    quantiteProduits = models.PositiveIntegerField(default=0)
    date_entree  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date_entree']

    def __str__(self):
        return self.missionConsernee
    
    @property
    def prix_recette(self):
        return ".2f" % (self.quantiteProduits * self.produitTransportes.montant)
    

class RecetteSansPesage(RecetteMissions):
    pass

class RecetteAvecPesage(RecetteMissions):
    premierPesee = models.PositiveIntegerField(default=0)
    deuxiemePese = models.PositiveIntegerField(default=0)

