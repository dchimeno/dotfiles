
"""
Casos de uso
1) Cambia mi ip pública:
   -> Actualizar todos los secgroups con descripción <descrp> a mi nueva ip
2)
"""
from pprint import pprint
import json
import sys
import boto3
ec2 = boto3.client('ec2')



def get_sec_groups_by_descr(descr):
    try:
        response = ec2.describe_security_groups()
    except ClientError as e:
        print(e)
    secgroups = response["SecurityGroups"]

    sec_label = []
    for sec in secgroups:
        for ippermission in sec["IpPermissions"]:
            for iprange in ippermission["IpRanges"]:
                if iprange.get('Description') == descr:
                    sec_label.append(sec)


    sec_label_names = []
    for sec in sec_label:
        for tag in sec.get('Tags', []):
            if tag.get('Key') == 'Name':
                sec_label_names.append(tag.get('Value'))

    return sec_label_names


def update_ip_with_descr_in_secgroups(descr, ip, secgroups):

    client = boto3.client('lambda')
    ipaddress = f"{ip}/32"

    body = {
        "desc": descr,
        "ipaddress": ipaddress,
        "sgList": secgroups
    }


    response = client.invoke(
        FunctionName='CAPupdateSecurityGroups',
        InvocationType='Event',
        LogType='Tail',
        Payload=json.dumps(body),
    )
    return response

def get_current_ip():
    import urllib.request

    external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')

    return external_ip

def parse_arguments():
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Update Sec Groups')

    parser.add_argument('-d', '--description',
        type=str,
        default="danielCh",
        help="Description to update with IP",)


    parser.add_argument('-ip',
        default=get_current_ip(),
        help="New ip")


    parser.add_argument('-s', '--secgroups',
        type=str,
        nargs='*',
        help="Sec groups to update")



    args = parser.parse_args()
    if not args.secgroups:
        args.secgroups = get_sec_groups_by_descr(args.description)
    return args

if __name__ == "__main__":
    """
    By default, it will update all security groups that has a ip associate with
    descr: <descr> with the current ip
    """

    args = parse_arguments()

    print(update_ip_with_descr_in_secgroups(descr=args.description,
                                        ip=args.ip,
                                        secgroups=args.secgroups))
