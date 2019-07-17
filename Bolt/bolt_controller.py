import os
import json
from puppet.puppet_controller import get_uri


async def bolt_upgrade_vision(client_id):
    uri = await get_uri(client_id)
    stout = await os.popen("bolt command run 'pwd' -n %s --transport winrm --user Administrator --password 'Ping3y3!!!!'" % uri)
    return await stout
