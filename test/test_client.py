import unittest
from unittest import TestCase

from powerbi.client import PowerBiClient
from powerbi.auth import PowerBiAuth
from powerbi.session import PowerBiSession
from powerbi.config import TENANT_ID, CLIENT_ID, CLIENT_SECRET

from powerbi.services.dashboards import Dashboards
from powerbi.services.groups import Groups
from powerbi.services.users import Users
from powerbi.services.dataflow_storage_accounts import DataflowStorageAccounts
from powerbi.services.push_datasets import PushDatasets
from powerbi.services.available_features import AvailableFeatures
from powerbi.services.capacities import Capacities
from powerbi.services.reports import Reports
from powerbi.services.pipelines import Pipelines
from powerbi.services.apps import Apps

class TestPowerBiSession(TestCase):

    """Will perform a unit test for the `PowerBiClient` object."""

    def setUp(self) -> None:
        """Set up the `PowerBiClient` object."""

        auth = PowerBiAuth(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
        session = PowerBiSession(auth)

        # Initialize the Client.
        self.power_bi_client = PowerBiClient(session)

    def test_creates_instance_of_client(self):
        """Create an instance and make sure it's a `PowerBiClient` object"""

        self.assertIsInstance(self.power_bi_client, PowerBiClient)

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `PowerBiSession` object"""

        self.assertIsInstance(
            self.power_bi_client.power_bi_session,
            PowerBiSession
        )

    def test_creates_instance_of_auth(self):
        """Create an instance and make sure it's a `PowerBiAuth` object"""

        self.assertIsInstance(
            self.power_bi_client.power_bi_auth_client,
            PowerBiAuth
        )

    def test_creates_instance_of_apps(self):
        """Create an instance and make sure it's a `Apps` object"""

        self.assertIsInstance(
            self.power_bi_client.apps(),
            Apps
        )

    def test_creates_instance_of_dashboards(self):
        """Create an instance and make sure it's a `Dashboards` object"""

        self.assertIsInstance(
            self.power_bi_client.dashboards(),
            Dashboards
        )

    def test_creates_instance_of_groups(self):
        """Create an instance and make sure it's a `Groups` object"""

        self.assertIsInstance(
            self.power_bi_client.groups(),
            Groups
        )

    def test_creates_instance_of_users(self):
        """Create an instance and make sure it's a `Users` object"""

        self.assertIsInstance(
            self.power_bi_client.users(),
            Users
        )

    def test_creates_instance_of_dataflow_storage_account(self):
        """Create an instance and make sure it's a `DataflowStorageAccount` object"""

        self.assertIsInstance(
            self.power_bi_client.dataflow_storage_account(),
            DataflowStorageAccounts
        )

    def test_creates_instance_of_push_datasets(self):
        """Create an instance and make sure it's a `PushDatasets` object"""

        self.assertIsInstance(
            self.power_bi_client.push_datasets(),
            PushDatasets
        )

    def test_creates_instance_of_available_features(self):
        """Create an instance and make sure it's a `AvailableFeatures` object"""

        self.assertIsInstance(
            self.power_bi_client.available_features(),
            AvailableFeatures
        )

    def test_creates_instance_of_capacities(self):
        """Create an instance and make sure it's a `Capacities` object"""

        self.assertIsInstance(
            self.power_bi_client.capactities(),
            Capacities
        )

    def test_creates_instance_of_reports(self):
        """Create an instance and make sure it's a `Capacities` object"""

        self.assertIsInstance(
            self.power_bi_client.reports(),
            Reports
        )

    def test_creates_instance_of_pipelines(self):
        """Create an instance and make sure it's a `Pipelines` object"""

        self.assertIsInstance(
            self.power_bi_client.pipelines(),
            Pipelines
        )

    def tearDown(self) -> None:
        """Teardown the `PowerBiClient` object."""

        del self.power_bi_client

if __name__ == '__main__':
    unittest.main()