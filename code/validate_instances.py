__author__ = 'agbeltran'

import json,os
from jsonschema import RefResolver, Draft4Validator
from os.path import join


def validate_instance(filename, error_printing, path = None):
    schemasPath = os.path.abspath("../json-schemas")
    #path = "../examples"
    if None != path:
        instance = json.load(open(join(path,filename)))
    else:
        instance = json.load(open(filename))
    datasetSchema = json.load(open(join(schemasPath,"dataset_schema.json")))
    instrumentSchema = json.load(open(join(schemasPath,"instrument_schema.json")))
    resolver = RefResolver('file://'+schemasPath+'/'+"dataset_schema.json", datasetSchema) #, base_uri=schemasPath)
    validator = Draft4Validator(datasetSchema, resolver=resolver)
    print("Validating ", filename)

    if (error_printing == 0):
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        for error in errors:
             print(error.message)
    elif (error_printing == 1):
        errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        for error in errors:
            for suberror in sorted(error.context, key=lambda e: e.schema_path):
                print(list(suberror.schema_path), suberror.message, sep=", ")
    else:
        validator.validate(instance, datasetSchema)

    print("...done")

if __name__ == '__main__':
    import sys
    if 1 < len(sys.argv):
        for i in range(1, len(sys.argv) ):
            fname = sys.argv[i]
            validate_instance( fname, 2 )
    else:
        print('format is: validate_instance.py [input file]')
        sys.exit(1)

