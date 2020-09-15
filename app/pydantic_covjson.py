from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field


class I18NText(BaseModel):
    """Multi-language text."""

    __root__: Dict[str, str]

    # TODO: validate language keys?


class Category(BaseModel):
    id: str
    label: I18NText
    description: Optional[I18NText] = None


class CategoryEncoding(BaseModel):
    """Map category id to data value."""

    __root__: Dict[str, Union[int, List[int]]]

    # TODO: validate each encoding value mapped to only one category id


class ObservedProperty(BaseModel):
    id: Optional[str] = None
    label: I18NText
    description: Optional[I18NText] = None
    categories: Optional[List[Category]] = None


class Symbol(BaseModel):
    type: str = Field("http://www.opengis.net/def/uom/UCUM/", const=True)
    value: str


class Unit(BaseModel):
    id: Optional[str] = None
    label: Optional[I18NText] = None
    symbol: Optional[Union[str, Symbol]] = None

    # TODO: validate at least label or symbol defined


class Parameter(BaseModel):
    type: str = Field("Parameter", const=True)
    id: Optional[str] = None
    label: Optional[I18NText] = None
    description: Optional[I18NText] = None
    observed_property: ObservedProperty
    category_encoding: Optional[CategoryEncoding] = None
    unit: Optional[Unit] = None

    # TODO: unit must be None if observed_property.categories is not None


class GeographicCRS(BaseModel):
    type: str = Field("GeographicCRS", const=True)
    id: Optional[str] = None


class ProjectedCRS(BaseModel):
    type: str = Field("ProjectedCRS", const=True)
    id: Optional[str] = None


class VerticalCRS(BaseModel):
    type: str = Field("VerticalCRS", const=True)
    id: Optional[str] = None


class TemporalRS(BaseModel):
    type: str = Field("TemporalRS", const=True)
    calendar: str = "Gregorian"
