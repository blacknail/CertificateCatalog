import json
from OpenSSL import crypto
from datetime import datetime


def get_cert_dataOpenSSL(cert_file):
    asn1 = True
    try:
        cert = crypto.load_certificate(crypto.FILETYPE_ASN1, cert_file)
    except Exception as ex:
        asn1 = False

    if not asn1:
        try:
            cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_file)
        except Exception as ex:
            pass

    if cert:
        issuerName = cert.get_issuer()

        res = {name.decode(): value.decode('utf-8')
               for name, value in cert.get_subject().get_components()}

        res['issuer'] = {name.decode(): value.decode('utf-8')
               for name, value in issuerName.get_components()}

        res['notbefore'] = get_date(cert.get_notBefore().decode('utf-8'))
        res['notafter'] = get_date(cert.get_notAfter().decode('utf-8'))
        res['serial'] = '{0:02x}'.format(cert.get_serial_number()).upper()

    else:
        res = {}

    return res


def get_date(date_str):
    data_my = None
    try:
        data_my = datetime.strptime(date_str, '%Y%m%d%H%M%SZ')
    except Exception as ex:
        pass

    if data_my is None:
        try:
            data_my = datetime.strptime(date_str, '%Y%m%d%H%M%S+%H%M')
        except Exception as ex:
            pass

    if data_my is None:
        try:
            data_my = datetime.strptime(date_str, '%Y%m%d%H%M%S-%H%M')
        except Exception as ex:
            pass

    return data_my.isoformat()


def row_to_dict(row):
    res_dict = {"id": row[0],
                "OU": row[1],
                "C": row[2],
                "CN": row[3],
                "O": row[4],
                "L": row[5],
                "ST": row[6],
                "street": row[7],
                "title": row[8],
                "emailAddress": row[9],
                "serial": row[10],
                "notafter": row[11],
                "notbefore": row[12]}

    return res_dict