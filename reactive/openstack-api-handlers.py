# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# need/want absolute imports for the package imports to work properly
from __future__ import absolute_import

import charms.reactive as reactive

import charms_openstack.charm as charm

#TODO remove this import
import charmhelpers.core.hookenv as hookenv

@reactive.when('amqp.connected')
def setup_amqp_req(amqp):
    """Use the amqp interface to request access to the amqp broker using our
    local configuration.
    """
    charm.do_default_handler('amqp.connected', amqp)


@reactive.when('shared-db.connected')
def setup_database(database):
    """Use the database interface to request databases on the database.
    Uses the default handler, which will inquire the charm class to discover
    which databases to access.
    """
    charm.do_default_handler('shared-db.connected', database)


@reactive.when('identity-service.connected')
def setup_endpoint_connected(keystone):
    """Set up the endpoint in keystone.  This uses the default handler which
    can be enabled in the charm.
    """
    hookenv.log("\nidentity-service.connection hook called...")
    charm.do_default_handler('identity-service.connected', keystone)


@reactive.when('identity-service.available')
def setup_endpoint_available(keystone):
    """Any further setup for the endpoint when the connection becomes
    available.  Typically, this is used for SSL configuration.  This uses the
    default handler.
    """
    hookenv.log("\nidentity-service.available hook called...")
    charm.do_default_handler('identity-service.available', keystone)
