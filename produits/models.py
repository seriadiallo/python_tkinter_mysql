'''
Dans ce module il y a la gestion de l'acces base de donnees pour 
la table 'produits'

'''

from connection import CONNECTION

class Produit:

    @staticmethod
    def create(nom, quantite, prix, date_expiration, id_categorie):
        'enrgeistrement d\'une ligne de produit dans la base de données'

        CONNECTION.ping() # ouvrire la connexion (si elle a été fermée par une autre fonction)
        try:
            val = 0
            with CONNECTION.cursor() as cursor:
                SQL = ''' INSERT INTO produits (nom, quantite, prix, date_expiration, id_categorie) 
                    VALUES(%s, %s, %s, %s, %s)
                    '''
                val = cursor.execute(SQL, ( nom, quantite, prix, date_expiration, id_categorie))
        except Exception as ex: # si une exception survient, on annulle toutes les modifications
            print(ex)
            CONNECTION.rollback()
        else: # si toutes les requetes ont été executées normalement, on valide les modifications
            CONNECTION.commit()
        finally: # dans les deux cas on ferme la connexion vers la base de données
            CONNECTION.close()
        return val

    
    @staticmethod
    def all():
        ' retourner tous les enregistrements de produits se trouvant dans la base de donnees '
        CONNECTION.ping()
        try:
            pts = 0
            with CONNECTION.cursor() as cursor:
                SQL = '''SELECT * FROM produits'''
                cursor.execute(SQL)
                pts = cursor.fetchall()
        except Exception as ex: 
            print(ex)
        finally: 
            CONNECTION.close()
        return pts

    