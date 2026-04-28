from pydantic import Field
from typing import List, Union, Literal, Optional
from sdks.novavision.src.base.model import (
    Package, Input, Output, Image, Config,
    Inputs, Configs, Outputs, Response, Request, Detection,
)


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Image
    type: str = "object"

    class Config:
        title = "Image"


class InputDetections(Input):
    name: Literal["inputDetections"] = "inputDetections"
    value: List[Detection]
    type: str = "list"

    class Config:
        title = "Distance Detections"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Image
    type: str = "object"

    class Config:
        title = "Image"


class DrawDistanceInputs(Inputs):
    inputImage: InputImage
    inputDetections: InputDetections


class DrawDistanceOutputs(Outputs):
    outputImage: OutputImage


class ConfigColor(Config):
    """Hex color for the distance lines and labels (e.g. #00FF00)."""

    name: Literal["configColor"] = "configColor"
    value: str = Field(default="#00FF00")
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Line Color"
        json_schema_extra = {"shortDescription": "Hex Color Code"}


class ConfigThickness(Config):
    """Thickness of the drawn line in pixels."""

    name: Literal["configThickness"] = "configThickness"
    value: int = Field(default=2, ge=1, le=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Thickness"
        json_schema_extra = {"shortDescription": "Line Thickness (px)"}


class ConfigFontScale(Config):
    """Scale of the distance label text."""

    name: Literal["configFontScale"] = "configFontScale"
    value: float = Field(default=0.5, ge=0.1, le=3.0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Font Scale"
        json_schema_extra = {"shortDescription": "Label Text Size"}


class DrawDistanceConfigs(Configs):
    configColor: ConfigColor
    configThickness: ConfigThickness
    configFontScale: ConfigFontScale


class DrawDistanceRequest(Request):
    inputs: Optional[DrawDistanceInputs] = None
    configs: DrawDistanceConfigs

    class Config:
        json_schema_extra = {"target": "configs"}


class DrawDistanceResponse(Response):
    outputs: DrawDistanceOutputs


class DrawDistanceExecutor(Config):
    name: Literal["DrawDistance"] = "DrawDistance"
    value: Union[DrawDistanceRequest, DrawDistanceResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Draw Distance"
        json_schema_extra = {"target": {"value": 0}}


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[DrawDistanceExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {"target": "value"}


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["DrawDistance"] = "DrawDistance"
