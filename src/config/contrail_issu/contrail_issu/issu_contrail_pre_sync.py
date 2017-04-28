#!/usr/bin/python
#
# Copyright (c) 2016 Juniper Networks, Inc. All rights reserved.
#

from issu_contrail_common import ICCassandraClient
from pysandesh.gen_py.sandesh.ttypes import SandeshLevel
import logging
import issu_contrail_config


def _issu_cassandra_pre_sync_main():

    logging.basicConfig(
        level=logging.INFO,
        filename='/var/log/contrail/issu_contrail_pre_sync.log',
        format='%(asctime)s %(message)s')

    args, remaining_args = issu_contrail_config.parse_args()
    issu_cass_pre = ICCassandraClient(
        args.old_cassandra_address_list,
        args.new_cassandra_address_list,
        args.odb_prefix, args.ndb_prefix,
        issu_contrail_config.issu_info_pre, issu_contrail_config.logger)
    issu_cass_pre.issu_merge_copy(
        issu_contrail_config.issu_keyspace_config_db_uuid)
    issu_contrail_config.lognprint("Done syncing Configdb uuid",
                                   level=SandeshLevel.SYS_INFO)
    issu_cass_pre.issu_merge_copy(
        issu_contrail_config.issu_keyspace_to_bgp_keyspace)
    issu_contrail_config.lognprint("Done syncing bgp keyspace",
                                   level=SandeshLevel.SYS_INFO)
    issu_cass_pre.issu_merge_copy(
        issu_contrail_config.issu_keyspace_user_agent)
    issu_contrail_config.lognprint("Done syncing useragent keyspace",
                                   level=SandeshLevel.SYS_INFO)
    issu_cass_pre.issu_merge_copy(
        issu_contrail_config.issu_keyspace_svc_monitor_keyspace)
    issu_contrail_config.lognprint("Done syncing svc-monitor keyspace",
                                   level=SandeshLevel.SYS_INFO)
    issu_cass_pre.issu_merge_copy(
        issu_contrail_config.issu_keyspace_dm_keyspace)
    issu_contrail_config.lognprint("Done syncing dm keyspace",
                                   level=SandeshLevel.SYS_INFO)

if __name__ == "__main__":
    _issu_cassandra_pre_sync_main()
