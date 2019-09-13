from flask import Blueprint
from artifactory.artifactory_controller import get_latest_vision_web_version
from mongo.routes.hiera_vision_routes import vision_environments_live_web_version
from Bolt.bolt_controller import bolt_upgrade_vision
from zeus.task_controller import set_web_version
import requests
import asyncio
import aiohttp
import async_timeout
import json

loop = asyncio.get_event_loop()
checks = Blueprint('checks', __name__)
async def fetch(url):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

@checks.route("/bolt/test")
def test_zeus_connection():
    res = loop.run_until_complete(asyncio.gather(
        fetch("https://zeus.netsmartcloud.com/bolt/test/12345")
    ))
    return res

@checks.route("/vision/<client_id>/webcheck")
def vision_environments_uat_db(client_id):
    json_dict = {}
    client_current_ver = (vision_environments_live_web_version(client_id))
    loaded_cv = json.loads(client_current_ver)
    print(type(loaded_cv), loaded_cv)
    json_dict['client_current_ver'] = loaded_cv
    print('client current version: ', client_current_ver, "<--", type(client_current_ver))
    latest_ver = get_latest_vision_web_version()
    latest_ver = json.loads(latest_ver)
    print(latest_ver)
    print('artifactory latest version: ', latest_ver, "<---", type(latest_ver))
    json_dict['artifactory_latest_ver'] = latest_ver
    return json.dumps(json_dict)

@checks.route("/vision/upgrade/<client_id>/<version>")
def vision_web_upgrade_set(client_id, version):
    results = set_web_version(client_id, version)
    return results



@checks.route("/vision/<client_id>")
async def vision_upgrade(client_id):
    some_object = await bolt_upgrade_vision(client_id)
    return await some_object