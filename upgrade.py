from flask import Blueprint
from controllers.task_controller import *
from setup_logger import logger, error_logger
upgrade = Blueprint('upgrade', __name__)

@upgrade.route("/<solution>/upgrade/web/<client_id>/")
def upgrade_vision_web_version(solution, client_id):
    logger.info("upgrade_vision_web_version route called")
    return update_web_version(solution, client_id)
