import pymysql.cursors
# Connect to the database
CONNECTION = pymysql.connect(host='localhost',
                             user='python',
                             password='12345678',
                             db='stock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)