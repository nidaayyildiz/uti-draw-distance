from sdks.novavision.src.helper.package import PackageHelper
from components.DrawDistance.src.models.PackageModel import (
    PackageModel, PackageConfigs, ConfigExecutor,
    OutputImage, DrawDistanceOutputs, DrawDistanceResponse, DrawDistanceExecutor,
)


def build_response(context):
    output_image = OutputImage(value=context.image)
    outputs = DrawDistanceOutputs(outputImage=output_image)
    response = DrawDistanceResponse(outputs=outputs)
    executor = ConfigExecutor(value=DrawDistanceExecutor(value=response))
    package_configs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)
