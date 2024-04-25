# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from .model import Model
from .multi_series_input import MultiSeriesInput


class MultiSeriesInsampleForecast(pydantic_v1.BaseModel):
    model: typing.Optional[Model] = pydantic_v1.Field(default=None)
    """
    Model to use as a string. Options are: `timegpt-1`, and `timegpt-1-long-horizon.` We recommend using `timegpt-1-long-horizon` for forecasting if you want to predict more than one seasonal period given the frequency of your data.
    """

    freq: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The frequency of the data represented as a string. 'D' for daily, 'M' for monthly, 'H' for hourly, and 'W' for weekly frequencies are available.
    """

    level: typing.Optional[typing.List[typing.Any]] = pydantic_v1.Field(default=None)
    """
    A list of values representing the prediction intervals. Each value is a percentage that indicates the level of certainty for the corresponding prediction interval. For example, [80, 90] defines 80% and 90% prediction intervals.
    """

    y: typing.Optional[typing.Any] = None
    x: typing.Optional[MultiSeriesInput] = pydantic_v1.Field(default=None)
    """
    The exogenous variables provided as a dictionary of two colums: columns and data. The columns contains the columns of the dataframe and data contains eaach data point. For example: {"columns": ["unique_id", "ds", "ex_1", "ex_2"], "data": [["ts_0", "2021-01-01", 0.2, 0.67], ["ts_0", "2021-01-02", 0.4, 0.7]}. This should also include forecasting horizon (fh) additional timestamps for each unique_id to calculate the future values.
    """

    clean_ex_first: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    A boolean flag that indicates whether the API should preprocess (clean) the exogenous signal before applying the large time model. If True, the exogenous signal is cleaned; if False, the exogenous variables are applied after the large time model.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
