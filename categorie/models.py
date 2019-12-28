from connection import CONNECTION

class Categorie:
    """
    cette classe represente la table 'categories' elle permet de faire toutes les manipulations
    -INSERT
    -UPDATE
    -SELECT
    -DELETE
    qui sont representees par des fonctions (methodes statiques)
    """

    @staticmethod
    def create(nom):
        '''
        Enregistrement d\'une categorie dans la base de donnees

        elle recoit le nom de la categorie
        
        apres insertion, il retourne le nombre de lignes enrgistrées qui peux etre 0 ou 1
        0: l'insertion a échoué
        1: l'insertion s'est bien passée
        
        '''

        ligne = 0
        try:
            CONNECTION.ping() # ouvrir la connexion si elle a été fermée
            with CONNECTION.cursor() as cursor:
                # Enregistrer
                sql = "INSERT INTO `categories` (`nom`) VALUES (%s)"
                ligne = cursor.execute(sql, (nom, ))

        except Exception as e:
            print('une erreur est survenue')
            print(e)
            CONNECTION.rollback()
        else:
            CONNECTION.commit()
        finally:
            CONNECTION.close()
        return ligne

    @staticmethod
    def getAll():
        """
        Cette fonction permet de recuperer toutes lignes de la table categories
        ensuite retourner le resultat sous form de dictionaire
        """
        categories = None
        try:
            CONNECTION.ping() # ouvrir la connexion si elle a été fermée
            with CONNECTION.cursor() as cursor:
                # Enregistrer
                sql = "SELECT * FROM `categories` "
                cursor.execute(sql)
                categories = cursor.fetchall()

        except Exception as e:
            print('une erreur est survenue')
            print(e)
        
        finally:
            CONNECTION.close()
        
        return categories

    @staticmethod
    def getByName(nom):
        """
        selectionner en fonction du nom de la categorie
        """
        categorie = None
        try:
            CONNECTION.ping() # ouvrir la connexion si elle a été fermée
            with CONNECTION.cursor() as cursor:
                # Enregistrer
                sql = "SELECT * FROM `categories` WHERE nom=%s"
                cursor.execute(sql, (nom, ))
                categorie = cursor.fetchone()

        except Exception as e:
            print('une erreur est survenue')
            print(e)
        
        finally:
            CONNECTION.close()
        
        return categorie
