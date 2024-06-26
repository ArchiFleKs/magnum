# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itertools
from oslo_config import cfg

DEFAULT_CERT_MANAGER = 'barbican'
TLS_STORAGE_DEFAULT = '/var/lib/magnum/certificates/'

certificates_group = cfg.OptGroup(name='certificates',
                                  title='Certificate options for the '
                                        'cert manager.')

cert_manager_opts = [
    cfg.StrOpt('cert_manager_type',
               default=DEFAULT_CERT_MANAGER,
               help='Certificate Manager plugin.')
]

local_cert_manager_opts = [
    cfg.StrOpt('storage_path',
               default=TLS_STORAGE_DEFAULT,
               help='Absolute path of the certificate storage directory.')
]

ALL_OPTS = list(itertools.chain(
    cert_manager_opts,
    local_cert_manager_opts
))


def register_opts(conf):
    conf.register_group(certificates_group)
    conf.register_opts(ALL_OPTS, group=certificates_group)


def list_opts():
    return {
        certificates_group: ALL_OPTS
    }
