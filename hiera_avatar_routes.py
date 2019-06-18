from flask import Blueprint
from controllers.mongo_controller import *
from setup_logger import logger, error_logger
hiera_avatar = Blueprint('hiera_avatar', __name__)




@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmso/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmso_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmso_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmso']['size'])
    return avmso_size

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces/dat/cws")
def avatar_cachedb_client_config_namespaces_dat_cws(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    dat_cws = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces']['dat']['cws'])
    return dat_cws

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups")
def avatar_rhel_lvm_volume_groups(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    lvm_volume_groups = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups'])
    return lvm_volume_groups

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg")
def avatar_rhel_lvm_volume_groups_cachedbvg(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    volume_groups_cachedbvg = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg'])
    return volume_groups_cachedbvg

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfms/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfms_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfms_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfms']['ensure'])
    return avcfms_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcws/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcws_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcws_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcws']['options'])
    return avcws_options

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcfmstmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcfmstmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avcfmstmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcfmstmp'])
    return permissions_avcfmstmp

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpmtmp/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpmtmp_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpmtmp_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpmtmp']['size'])
    return avpmtmp_size

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfmstmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfmstmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avcfmstmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfmstmp'])
    return logical_volumes_avcfmstmp

      
@hiera_avatar.route("/avatar/<client_id>/rhel")
def avatar_rhel(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avatar_rhel = json.dumps(client_dictionary['avatar']['rhel'])
    return avatar_rhel

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfmstmp/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfmstmp_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfmstmp_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfmstmp']['size'])
    return avcfmstmp_size

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcwstmp/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcwstmp_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcwstmp_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcwstmp']['mountpath'])
    return avcwstmp_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avpm/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avpm_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpm_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avpm']['group'])
    return avpm_group

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmso/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmso_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmso_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmso']['mountpath'])
    return avmso_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces/dat/cfms")
def avatar_cachedb_client_config_namespaces_dat_cfms(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    dat_cfms = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces']['dat']['cfms'])
    return dat_cfms

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcfms")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcfms(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avcfms = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcfms'])
    return permissions_avcfms

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcws/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcws_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcws_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcws']['size'])
    return avcws_size

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmsotmp/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmsotmp_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmsotmp_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmsotmp']['mountpath'])
    return avmsotmp_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmsotmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmsotmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avmsotmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmsotmp'])
    return logical_volumes_avmsotmp

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcws")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcws(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avcws = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcws'])
    return logical_volumes_avcws

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config")
def avatar_cachedb_client_config(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    cachedb_client_config = json.dumps(client_dictionary['avatar']['cachedb']['client_config'])
    return cachedb_client_config

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcwstmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcwstmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avcwstmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcwstmp'])
    return logical_volumes_avcwstmp

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmso/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmso_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmso_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmso']['ensure'])
    return avmso_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfmstmp/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfmstmp_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfmstmp_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfmstmp']['mountpath'])
    return avcfmstmp_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfms")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfms(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avcfms = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfms'])
    return logical_volumes_avcfms

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcfmstmp/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcfmstmp_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfmstmp_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcfmstmp']['owner'])
    return avcfmstmp_owner

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmsotmp/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmsotmp_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmsotmp_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmsotmp']['size'])
    return avmsotmp_size

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avmsotmp/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avmsotmp_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmsotmp_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avmsotmp']['owner'])
    return avmsotmp_owner

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcwstmp/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcwstmp_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcwstmp_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcwstmp']['options'])
    return avcwstmp_options

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avpm/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avpm_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpm_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avpm']['owner'])
    return avpm_owner

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcfmstmp/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcfmstmp_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfmstmp_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcfmstmp']['group'])
    return avcfmstmp_group

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfms/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfms_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfms_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfms']['size'])
    return avcfms_size

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    cachedbvg_permissions = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions'])
    return cachedbvg_permissions

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces")
def avatar_cachedb_client_config_namespaces(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    client_config_namespaces = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces'])
    return client_config_namespaces

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmsotmp/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmsotmp_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmsotmp_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmsotmp']['ensure'])
    return avmsotmp_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    cachedbvg_logical_volumes = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes'])
    return cachedbvg_logical_volumes

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcfms/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcfms_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfms_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcfms']['group'])
    return avcfms_group

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpm/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpm_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpm_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpm']['mountpath'])
    return avpm_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/copy_pure_dat")
def avatar_cachedb_client_config_copy_pure_dat(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    client_config_copy_pure_dat = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['copy_pure_dat'])
    return client_config_copy_pure_dat

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcfms/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcfms_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfms_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcfms']['owner'])
    return avcfms_owner

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/copy_dat")
def avatar_cachedb_client_config_copy_dat(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    client_config_copy_dat = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['copy_dat'])
    return client_config_copy_dat

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmsotmp/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmsotmp_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmsotmp_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmsotmp']['options'])
    return avmsotmp_options

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfms/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfms_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfms_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfms']['mountpath'])
    return avcfms_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpmtmp/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpmtmp_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpmtmp_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpmtmp']['mountpath'])
    return avpmtmp_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces/disable_tmp_folder")
def avatar_cachedb_client_config_namespaces_disable_tmp_folder(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    namespaces_disable_tmp_folder = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces']['disable_tmp_folder'])
    return namespaces_disable_tmp_folder

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpm/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpm_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpm_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpm']['size'])
    return avpm_size

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpmtmp/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpmtmp_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpmtmp_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpmtmp']['ensure'])
    return avpmtmp_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfms/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfms_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfms_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfms']['options'])
    return avcfms_options

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avpmtmp/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avpmtmp_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpmtmp_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avpmtmp']['owner'])
    return avpmtmp_owner

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcws/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcws_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcws_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcws']['ensure'])
    return avcws_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcwstmp/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcwstmp_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcwstmp_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcwstmp']['group'])
    return avcwstmp_group

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avmsotmp/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avmsotmp_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmsotmp_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avmsotmp']['group'])
    return avmsotmp_group

      
@hiera_avatar.route("/avatar/<client_id>/cachedb")
def avatar_cachedb(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avatar_cachedb = json.dumps(client_dictionary['avatar']['cachedb'])
    return avatar_cachedb

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces/dat")
def avatar_cachedb_client_config_namespaces_dat(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    namespaces_dat = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces']['dat'])
    return namespaces_dat

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmso")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmso(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avmso = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmso'])
    return logical_volumes_avmso

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avmsotmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avmsotmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avmsotmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avmsotmp'])
    return permissions_avmsotmp

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcws/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcws_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcws_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcws']['owner'])
    return avcws_owner

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avpm")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avpm(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avpm = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avpm'])
    return permissions_avpm

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avpmtmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avpmtmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avpmtmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avpmtmp'])
    return permissions_avpmtmp

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpm/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpm_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpm_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpm']['options'])
    return avpm_options

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces/dat/mso")
def avatar_cachedb_client_config_namespaces_dat_mso(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    dat_mso = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces']['dat']['mso'])
    return dat_mso

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avpmtmp/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avpmtmp_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpmtmp_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avpmtmp']['group'])
    return avpmtmp_group

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpm")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpm(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avpm = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpm'])
    return logical_volumes_avpm

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avmso/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avmso_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmso_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avmso']['owner'])
    return avmso_owner

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfmstmp/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfmstmp_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfmstmp_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfmstmp']['ensure'])
    return avcfmstmp_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avmso/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avmso_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmso_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avmso']['group'])
    return avmso_group

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avmso/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avmso_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avmso_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avmso']['options'])
    return avmso_options

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcwstmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcwstmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avcwstmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcwstmp'])
    return permissions_avcwstmp

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcwstmp/size")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcwstmp_size(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcwstmp_size = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcwstmp']['size'])
    return avcwstmp_size

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avmso")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avmso(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avmso = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avmso'])
    return permissions_avmso

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcws/mountpath")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcws_mountpath(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcws_mountpath = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcws']['mountpath'])
    return avcws_mountpath

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces/dat/pm")
def avatar_cachedb_client_config_namespaces_dat_pm(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    dat_pm = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces']['dat']['pm'])
    return dat_pm

      
@hiera_avatar.route("/avatar/<client_id>")
def avatar(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avatar = json.dumps(client_dictionary['avatar'])
    return avatar

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpmtmp")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpmtmp(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    logical_volumes_avpmtmp = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpmtmp'])
    return logical_volumes_avpmtmp

      
@hiera_avatar.route("/avatar/<client_id>/_id")
def avatar__id(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avatar__id = json.dumps(client_dictionary['avatar']['_id'])
    return avatar__id

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcwstmp/owner")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcwstmp_owner(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcwstmp_owner = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcwstmp']['owner'])
    return avcwstmp_owner

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcws")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcws(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    permissions_avcws = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcws'])
    return permissions_avcws

      
@hiera_avatar.route("/avatar/<client_id>/_etag")
def avatar__etag(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avatar__etag = json.dumps(client_dictionary['avatar']['_etag'])
    return avatar__etag

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcwstmp/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcwstmp_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcwstmp_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcwstmp']['ensure'])
    return avcwstmp_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm")
def avatar_rhel_lvm(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    rhel_lvm = json.dumps(client_dictionary['avatar']['rhel']['lvm'])
    return rhel_lvm

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpm/ensure")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpm_ensure(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpm_ensure = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpm']['ensure'])
    return avpm_ensure

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/permissions/avcws/group")
def avatar_rhel_lvm_volume_groups_cachedbvg_permissions_avcws_group(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcws_group = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['permissions']['avcws']['group'])
    return avcws_group

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avpmtmp/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avpmtmp_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avpmtmp_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avpmtmp']['options'])
    return avpmtmp_options

      
@hiera_avatar.route("/avatar/<client_id>/rhel/lvm/volume_groups/cachedbvg/logical_volumes/avcfmstmp/options")
def avatar_rhel_lvm_volume_groups_cachedbvg_logical_volumes_avcfmstmp_options(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    avcfmstmp_options = json.dumps(client_dictionary['avatar']['rhel']['lvm']['volume_groups']['cachedbvg']['logical_volumes']['avcfmstmp']['options'])
    return avcfmstmp_options

      
@hiera_avatar.route("/avatar/<client_id>/cachedb/client_config/namespaces/other")
def avatar_cachedb_client_config_namespaces_other(client_id):
    logger.info('get_hiera_avatar_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_avatar = cx.getDB('hiera_avatar')
    client_document = cx.get_client_collection(hiera_avatar, id_string)
    client_dictionary = json.loads(client_document)
    namespaces_other = json.dumps(client_dictionary['avatar']['cachedb']['client_config']['namespaces']['other'])
    return namespaces_other

      
