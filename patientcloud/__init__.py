import os
try:
    uname = os.uname()
    print("Unix-Like, os.uname:",uname)
except AttributeError:

    print("Windows maybe, excute :",'''
    import pymysql
    pymysql.version_info = (1, 4, 0, "final", 0)
    pymysql.install_as_MySQLdb()''')

    import pymysql
    pymysql.version_info = (1, 4, 0, "final", 0)
    pymysql.install_as_MySQLdb()