from __future__ import annotations

from pathlib import Path

from pkg_resources import DistributionNotFound, get_distribution


try:
    from monty.json import MSONable
except ImportError:
    MSONable = None

if MSONable:
    from crystaltoolkit.msonable import to_plotly_json, _repr_mimebundle_, show_json, _ipython_display_
    MSONable.to_plotly_json = to_plotly_json
    MSONable._repr_mimebundle_ = _repr_mimebundle_
    MSONable.show_json = show_json
    MSONable._ipython_display_ = _ipython_display_

MODULE_PATH = Path(__file__).parents[0]

try:
    __version__ = get_distribution("crystal_toolkit").version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    pass
