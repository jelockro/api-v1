import logging, sys, json
import requests
from setup_logger import logger
sys.path.append('/home/vagrant/api_v1/application_package/routes')
import ast

def init_logging():
    logger_format_string = '%(thread)5s %(module)-20s %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=logger_format_string, stream=sys.stdout)

# API_KEY
# init_logging()
# try:
#     path = ArtifactoryPath(
#         "http://npcrepo.netsmartcore.lan:8081/artifactory/api",
#         apikey='AKCp5dK4mFad6GwBUPEKjxdvZAL8MWakA92xMRmVvMPfRrXUw2F9SSQkThwDaiwYijHg8zS6Y')
#     for p in path:
#         print(p)
# except RuntimeError:
#     print('API_KEY doesnt work')
# _headers={'X-JFrog-ART-Api':'AKCp5Z3BiscJvzCUp58prVrh4pR8fcPpXBGza81ZjMNqsxiz6yxhKETkBM1HLeuSSnp9jfeMs',
#          'Content-Type': 'application/json' }
#
# r = requests.get("http://npcrepo.netsmartcore.lan:8081/artifactory/api/repositories", headers=_headers)
# repositories = r.content

# x = ast.literal_eval(repositories.decode('utf-8'))
# print(type(x), ": ", x)
# for repo in x:
#     print(repo)
# d = json.dumps(repositories.decode('utf-8'))

def get_latest_vision_web_version():
    #     print('API_KEY doesnt work')
    _headers = {'X-JFrog-ART-Api': 'AKCp5Z3BiscJvzCUp58prVrh4pR8fcPpXBGza81ZjMNqsxiz6yxhKETkBM1HLeuSSnp9jfeMs',
                'Content-Type': 'application/json'}
    logger.info('Creating artifactory Connection..')
    try:
        r = requests.get("http://npcrepo.netsmartcore.lan:8081/artifactory/api/search/latestVersion?g=web&a=vision", headers=_headers)
        logger.info('request was made to artifactory')
        return json.dumps(r.content.decode())
    except RuntimeError:
        logger.debug('artifactory request failed')

#artifacts = path.aql("items.find", {"repo": "docker"})
#printnested(artifacts, 0)

# # User and password OR API_KEY
# try:
#     path = ArtifactoryPath(
#         "http://npcrepo.netsmartcore.lan:8081/artifactory/docker/npc_agora_app",
#         auth=('jlockrow', 'AKCp5dK4mFad6GwBUPEKjxdvZAL8MWakA92xMRmVvMPfRrXUw2F9SSQkThwDaiwYijHg8zS6Y'))
#     path.touch()
# except RuntimeError:
#     print('User & Password doesnt work')
# #
# # path = curl -H 'X-JFrog-Art-Api:AKCp5dK4mFad6GwBUPEKjxdvZAL8MWakA92xMRmVvMPfRrXUw2F9SSQkThwDaiwYijHg8zS6Y'
# # path.touch()
# #
#
# # # Other authentication types
# try:
#     from requests.auth import HTTPDigestAuth
#
#     path = ArtifactoryPath(
#         "http://npcrepo.netsmartcore.lan:8081/artifactory/docker/npc_agora_app",
#         auth=('jlockrow', 'KIPnit!2419'),
#         auth_type=HTTPDigestAuth,
#
#     )
#     path.touch()
# except RuntimeError:
#     print('HTTPDDIgestAuth doesnt work')
# #
# try:
#     from requests.auth import HTTPBasicAuth
#
#     path = ArtifactoryPath(
#         "http://npcrepo.netsmartcore.lan:8081/artifactory/docker/npc_agora_app",
#         auth=('jlockrow', 'KIPNit!2419'),
#         auth_type=HTTPBasicAuth,
#     )
#     path.touch()
# except RuntimeError:
#     print('HTTPBasicAuth doesnt work')
#
# try:
#     from requests.auth import HTTPBasicAuth
#
#     path = ArtifactoryPath(
#         "http://npcrepo.netsmartcore.lan:8081/artifactory/docker/npc_agora_app",
#         auth=('jlockrow', 'AKCp5dK4mFad6GwBUPEKjxdvZAL8MWakA92xMRmVvMPfRrXUw2F9SSQkThwDaiwYijHg8zS6Y'),
#         auth_type=HTTPBasicAuth,
#     )
#     path.touch()
# except RuntimeError:
#     print('HTTPBasicAuth with apikey doesnt work')
#
# # Load username, password from global config if exist:
# path = ArtifactoryPath(
#     "http://my-artifactory/artifactory/myrepo/restricted-path",
#     auth_type=HTTPBasicAuth,
# )
#
# path.touch()

if __name__ == "__main__":
    get_latest_vision_web_version()
