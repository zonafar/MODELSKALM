from django.db import models
import exercices.Exercices
import missions.VehiculesParc

class PiecesEchanges(models.Model):
    nom = models.CharField(max_length=250)
    date_creation = models.DateTimeField(auto_now_add=True)


class Mantenances(models.Model):
    motif = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_maintenance = models.DateTimeField()
    montant = models.DecimalField(digits=19)

    exerciceConcerne =  models.ForeignKeyField(Exercices, related_name='maintenances')
    vehiculeConcerne = models.ForeignKeyField(VehiculesParc, related_name='maintenances_effectuees')
    piecesEchangees = models.ManyToManyField(
        PiecesEchanges, through='InfosPieces', through_fields=('maintenanceConcernee', 'nomPiece'),
        null=True
        ) #main.pieces.add(pie1), remove 

    class Meta:
        ordering=['vehicule','-date_creation']
    
    def __str__(self):
        return self.vehicule

    
class InfosPieces(models.Model): 
    coutUnitaire = models.DecimalField(max_digits=19, decimal_places=10)
    nombre = models.PositiveIntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    maintenanceConcernee = models.ForeignKey(Mantenances,related_name='pieces_enregistrees' ,on_delete=models.CASCADE)
    nomPiece = models.ForeignKey(PiecesEchanges, on_delete=models.CASCADE)

    @property
    def prix_Achat(self):
        return ".2f" %(self.nombre * self.coutUnitaire)
