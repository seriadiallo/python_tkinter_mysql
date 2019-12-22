from connection import CONNECTION

# class Categorie:

#     def __init__(self, nom=None):
#         self.nom = nom


#     def create(self, nom):

#         try:
#             with connection.cursor() as cursor:
#                 # Create a new record
#                 sql = "INSERT INTO `categories` (`nom`) VALUES (%s)"
#                 cursor.execute(sql, (nom, ))

#             # connection is not autocommit by default. So you must commit to save
#             # your changes.
#             CONNECTION.commit()

            
#         finally:
#             CONNECTION.close()

def create(nom):

    ligne = 0
    try:
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