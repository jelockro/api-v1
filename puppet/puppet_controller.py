import os
import json
from setup_logger import *
async def get_uri(client_id):
    query = "inventory[certname] { facts{ name='client_id and value='%s'}}" % client_id
    command = "puppet query %s" % query
    logger.info('query result: ', query)
    cert_object = await os.system(command)
    await logger.info('cert_object result: ', cert_object)
    return await cert_object