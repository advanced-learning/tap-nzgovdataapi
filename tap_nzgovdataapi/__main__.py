"""NZGovDataAPI entry point."""

from __future__ import annotations

from tap_nzgovdataapi.tap import TapNZGovDataAPI

TapNZGovDataAPI.cli()
