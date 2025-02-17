from powerbi.session import PowerBiSession
from powerbi.logger import get_logger

from powerbi.services.apps import Apps
from powerbi.services.dashboards import Dashboards
from powerbi.services.groups import Groups
from powerbi.services.users import Users
from powerbi.services.dataflow_storage_accounts import DataflowStorageAccounts
from powerbi.services.push_datasets import PushDatasets
from powerbi.services.imports import Imports
from powerbi.services.reports import Reports
from powerbi.services.available_features import AvailableFeatures
from powerbi.services.capacities import Capacities
from powerbi.services.pipelines import Pipelines
from powerbi.services.dataflows import Dataflows
from powerbi.services.datasets import Datasets

class PowerBiClient:
    def __init__(self, session: PowerBiSession):
        self.session = session
        self.logger = get_logger(self.__class__.__name__)

    def apps(self) -> Apps:
        return Apps(session=self.session)

    def dashboards(self) -> Dashboards:
        return Dashboards(session=self.session)

    def groups(self) -> Groups:
        return Groups(session=self.session)

    def users(self) -> Users:
        return Users(session=self.session)

    def dataflow_storage_account(self) -> DataflowStorageAccounts:
        return DataflowStorageAccounts(session=self.session)

    def push_datasets(self) -> PushDatasets:
        return PushDatasets(session=self.session)

    def imports(self) -> Imports:
        return Imports(session=self.session)

    def reports(self) -> Reports:
        return Reports(session=self.session)

    def available_features(self) -> AvailableFeatures:
        return AvailableFeatures(session=self.session)

    def capactities(self) -> Capacities:
        return Capacities(session=self.session)

    def pipelines(self) -> Pipelines:
        return Pipelines(session=self.session)

    def dataflows(self) -> Dataflows:
        return Dataflows(session=self.session)

    def datasets(self) -> Datasets:
        return Datasets(session=self.session)