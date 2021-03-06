# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import abc
import typing
import pkg_resources

from google import auth  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore

from google.area120.tables_v1alpha1.types import tables
from google.protobuf import empty_pb2 as empty  # type: ignore


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-area120-tables",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class TablesServiceTransport(abc.ABC):
    """Abstract transport class for TablesService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/spreadsheets.readonly",
    )

    def __init__(
        self,
        *,
        host: str = "area120tables.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

        # Lifted into its own function so it can be stubbed out during tests.
        self._prep_wrapped_messages(client_info)

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.get_table: gapic_v1.method.wrap_method(
                self.get_table, default_timeout=60.0, client_info=client_info,
            ),
            self.list_tables: gapic_v1.method.wrap_method(
                self.list_tables, default_timeout=60.0, client_info=client_info,
            ),
            self.get_row: gapic_v1.method.wrap_method(
                self.get_row, default_timeout=60.0, client_info=client_info,
            ),
            self.list_rows: gapic_v1.method.wrap_method(
                self.list_rows, default_timeout=60.0, client_info=client_info,
            ),
            self.create_row: gapic_v1.method.wrap_method(
                self.create_row, default_timeout=60.0, client_info=client_info,
            ),
            self.batch_create_rows: gapic_v1.method.wrap_method(
                self.batch_create_rows, default_timeout=60.0, client_info=client_info,
            ),
            self.update_row: gapic_v1.method.wrap_method(
                self.update_row, default_timeout=60.0, client_info=client_info,
            ),
            self.batch_update_rows: gapic_v1.method.wrap_method(
                self.batch_update_rows, default_timeout=60.0, client_info=client_info,
            ),
            self.delete_row: gapic_v1.method.wrap_method(
                self.delete_row, default_timeout=60.0, client_info=client_info,
            ),
        }

    @property
    def get_table(
        self,
    ) -> typing.Callable[
        [tables.GetTableRequest],
        typing.Union[tables.Table, typing.Awaitable[tables.Table]],
    ]:
        raise NotImplementedError()

    @property
    def list_tables(
        self,
    ) -> typing.Callable[
        [tables.ListTablesRequest],
        typing.Union[
            tables.ListTablesResponse, typing.Awaitable[tables.ListTablesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_row(
        self,
    ) -> typing.Callable[
        [tables.GetRowRequest], typing.Union[tables.Row, typing.Awaitable[tables.Row]]
    ]:
        raise NotImplementedError()

    @property
    def list_rows(
        self,
    ) -> typing.Callable[
        [tables.ListRowsRequest],
        typing.Union[
            tables.ListRowsResponse, typing.Awaitable[tables.ListRowsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_row(
        self,
    ) -> typing.Callable[
        [tables.CreateRowRequest],
        typing.Union[tables.Row, typing.Awaitable[tables.Row]],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_rows(
        self,
    ) -> typing.Callable[
        [tables.BatchCreateRowsRequest],
        typing.Union[
            tables.BatchCreateRowsResponse,
            typing.Awaitable[tables.BatchCreateRowsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_row(
        self,
    ) -> typing.Callable[
        [tables.UpdateRowRequest],
        typing.Union[tables.Row, typing.Awaitable[tables.Row]],
    ]:
        raise NotImplementedError()

    @property
    def batch_update_rows(
        self,
    ) -> typing.Callable[
        [tables.BatchUpdateRowsRequest],
        typing.Union[
            tables.BatchUpdateRowsResponse,
            typing.Awaitable[tables.BatchUpdateRowsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_row(
        self,
    ) -> typing.Callable[
        [tables.DeleteRowRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()


__all__ = ("TablesServiceTransport",)
