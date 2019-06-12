import sys
import os
import argparse
import json
sys.path.append(os.path.abspath(os.path.join('..', 'controllers')))
sys.path.append(os.path.abspath(os.path.join('..', 'helpers')))
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('~/home/vagrant/api_v1/application_package')
sys.path.append('~/home/vagrant/api_v1/application_package/helpers')
from mongo_connect import MongoDB
#print(sys.path)


def printnested(dictionary, level):
    level += 1
    offset = level - 1
    indent = "\t" * offset
    for key in sorted(dictionary.keys()):
        if isinstance(dictionary[key], dict):
            print(indent, '{' + str(level) + '}' + ' ' + key + ':')
            printnested(dictionary[key], level)
        else:
            print(indent, '{' + str(level) + '}' + '{}: '.format(key), dictionary[key])
    level -= 1


def add_to_dictionary(hierarchy, key, value):
    if hierarchy.get(key) is None:
        hierarchy[key] = [value]
        #print('HELLO!!', hierarchy[key])

    else:
        hierarchy[key].append(value)
        #print("APPPENDING>>>>  KEY", key, '...to....', hierarchy[key])


def make_hierarchy(dictionaryIn, dictionaryOut, level, parent):
    level += 1
    offset = level - 1
    indent = "\t" * offset
    for key in sorted(dictionaryIn.keys()):
        if key in ('vision', 'evolv', 'avatar'):
            path = '{}'.format(parent)
        else:
            path = '{}/{}'.format(parent, key)

        add_to_dictionary(dictionaryOut, path, dictionaryIn[key])
        if isinstance(dictionaryIn[key], dict):
            print(indent, '{' + str(level) + '}' + ' ' + key + ':')
            make_hierarchy(dictionaryIn[key], dictionaryOut, level, path)
        else:
            print(indent, '{' + str(level) + '}' + '{}: '.format(key), dictionaryIn[key])
    level -= 1


def main(parent, database, client_id):
    if client_id == None:
        client_id = '12345'
    cx = MongoDB('localhost')
    id_string = str(client_id)
    _database = cx.getDB(database)
    client_document = cx.get_client_collection(_database, id_string)
    print('client_document: ', client_document)
    client_dict = json.loads(client_document)
    print('client_dicct: ', client_dict)
    hierarchy = {}
    make_hierarchy(client_dict, hierarchy, 0, parent)
    filepath = os.path.join(sys.path[0], '..', '{}_routes.py'.format(database))
    w = open(filepath, 'w')
    w.write(
"""from flask import Blueprint
from controllers.mongo_controller import *
from setup_logger import logger, error_logger
{} = Blueprint('{}', __name__)
\n
\n
""".format(database, database)
    )
    for key in hierarchy.keys():
        if '$' in key:
            continue
        ###############
        # Prepare the url string & definition string that has to be lowercase, and use underscores
        ###############
        function_def_string = str(key).replace('/', ' ')
        #print(function_def_string)
        function_def_string_lower = function_def_string.lower().replace(' <client_id>', '', 2)
        #print('lowercase: ', function_def_string_lower)
        # add underscores
        function_def_string_lower = function_def_string_lower.replace(' ', '_')
        #print('underscores: ', function_def_string_lower)
        # strip leading uderscore
        function_def_string_lower = function_def_string_lower.strip('_')
        #print('stripped :' , function_def_string_lower)

        ##############
        # Prepare for dictionary lookup, which must not be in lowercase
        ##############
        dict_key_string = function_def_string.replace(' <client_id>', '', 2)
        #print('no <client_id>', dict_key_string)
        # strip leading space
        dict_key_string = dict_key_string.strip(' ')
        #print('stripped: ', dict_key_string)
        dictionary_lookup = dict_key_string.split(' ')
        #print('list: ', dictionary_lookup)
        #
        # try:
        #     dictionary_lookup.remove('<client-id>')
        #
        # except ValueError:
        #     print("oops!, unable to remove <client-id>")
        seperator = '_'
        last_two_words = dictionary_lookup[-2:]
        return_string = seperator.join(last_two_words)
        key_string="['"
        for word in dictionary_lookup:
            key_string += "{}']['".format(word)
        key_string = key_string[:-2]
        w.write(
"""@{}.route("{}")
def {}(client_id):
    logger.info('get_{}_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    {} = cx.getDB('{}')
    client_document = cx.get_client_collection({}, id_string)
    client_dictionary = json.loads(client_document)
    {} = json.dumps(client_dictionary{})
    return {}
\n      
""".format(database, key, function_def_string_lower, database, database, database, database, return_string, key_string, return_string)
        )
    w.close()



    return hierarchy

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="creates routes from solution yaml file")
    parser.add_argument("route", help="path to directory")
    parser.add_argument("database", help="name of database to model")
    parser.add_argument('-c', '--client', help="optional client id to use for model")
    args = parser.parse_args()
    main(args.route, args.database, args.client)
