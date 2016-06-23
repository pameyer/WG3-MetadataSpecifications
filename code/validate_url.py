#!/usr/bin/env python


from validate_instances import validate_instance_text
import requests

def validate_instance_url( url , error_printing ):
    r = requests.get(url)
    txt = r.text
    validate_instance_text( txt , error_printing )

if __name__ == '__main__':
    import sys
    try:
        url = sys.argv[1]
    except IndexError:
        print('format is: validate_url.py [url]')
        sys.exit(1)
    validate_instance_url( url, 2 )
