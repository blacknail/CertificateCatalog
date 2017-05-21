from django.db import connection
import datetime


class DataOps(object):
    def update_subject(self, cd, id):
        with connection.cursor() as cursor:
            sql = "UPDATE cert_catalog.CertCat_cert_subj " \
                 "SET OU=%s, C=%s, CN=%s, O=%s, L=%s, ST=%s, street=%s, title=%s, emailAddress=%s, serial=%s, " \
                 "notafter=%s, notbefore=%s, dt_update=%s " \
                 "WHERE id = %s"
            cursor.execute(sql, (cd.get("OU"), cd.get("C"), cd.get("CN"), cd.get("O"), cd.get("L"), cd.get("ST"),
                                 cd.get("street"), cd.get("title"), cd.get("emailAddress"), cd.get("serial"),
                                 cd.get("notafter") if cd.get("notafter") else None,
                                 cd.get("notbefore") if cd.get("notbefore") else None,
                                 datetime.datetime.now(), id))

        return self.get_subject(cert_id=id)

    def insert_subject(self, cd):
        with connection.cursor() as cursor:
            sql = "INSERT INTO cert_catalog.CertCat_cert_subj(" \
                  "OU, C, CN, O, L, ST, street, title, emailAddress, serial, notafter, notbefore, dt_create, dt_update" \
                  ") " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (cd.get("OU"), cd.get("C"), cd.get("CN"), cd.get("O"), cd.get("L"), cd.get("ST"),
                                 cd.get("street"), cd.get("title"), cd.get("emailAddress"), cd.get("serial"),
                                 cd.get("notafter") if cd.get("notafter") else None,
                                 cd.get("notbefore") if cd.get("notbefore") else None,
                                 datetime.datetime.now(), datetime.datetime.now()))

    def get_subject(self, cert_id):
        with connection.cursor() as cursor:
            sql = "SELECT id, OU, C, CN, O, L, ST, street, title, emailAddress, serial, notafter, notbefore " \
                  "FROM cert_catalog.CertCat_cert_subj WHERE id = %s"
            cursor.execute(sql, [cert_id])
            res = cursor.fetchone()
        return res
