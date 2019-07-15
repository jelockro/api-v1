from flask import Blueprint
from artifactory.artifactory_controller import get_latest_vision_web_version
from mongo.routes.hiera_vision_routes import vision_environments_live_web_version
import json

checks = Blueprint('checks', __name__)


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