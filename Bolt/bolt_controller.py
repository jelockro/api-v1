import os
import json
from puppet.puppet_controller import get_uri


async def bolt_upgrade_vision(client_id):
    uri = await get_uri(client_id)

    return await stout
