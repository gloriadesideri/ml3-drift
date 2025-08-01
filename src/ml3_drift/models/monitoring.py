from __future__ import annotations

from dataclasses import dataclass

from ml3_drift.enums.monitoring import DataDimension, DataType, MonitoringType


@dataclass(frozen=True, kw_only=True)
class MonitoringAlgorithmSpecs:
    """Data class containing the specification of monitoring algorithms
    that helps to define a taxonomy over them.
    """

    data_dimension: DataDimension
    data_type: DataType
    monitoring_type: MonitoringType


@dataclass(frozen=True, kw_only=True)
class MonitoringOutput:
    """Data class containing the output of the monitoring algorithm
    after one update step over a sample.

    If drift is detected then a drift info data model is present with
    additional information about the drift"""

    drift_detected: bool
    drift_info: DriftInfo | None


@dataclass(frozen=True, kw_only=True)
class DriftInfo:
    """Data class containing information of the detected drift.
    It is generated by the drift detector.
    """

    test_statistic: float | None = None
    statistic_threshold: float | None = None
