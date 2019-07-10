from .artifactory_controller import get_latest_vision_web_version
from .mongo_controller import update_vision_client_web_version
import json
from setup_logger import *


def update_web_version(solution, client_id):
    logger.debug('update_web_version called')
    client_id_str = str(client_id)
    hold_solution = solution # I need to refactor the update_vision_client_web_version so it takes solution as a parameter
    try:
        latest_web_version = json.loads(get_latest_vision_web_version())
        logger.info("Successfully pulled latest version from artifactory: {}".format(latest_web_version))
    except RuntimeError:
        logger.warning('unable to pull latest web version from artifactory')

    try:
        update_vision_client_web_version(client_id_str, latest_web_version)
        successMessage="Successful update of client mongo document to {}".format(latest_web_version)
        logger.info(successMessage)
    except RuntimeError:
        logger.warning('unable to update client mongo record to latest web version.')
    return json.dumps(successMessage)