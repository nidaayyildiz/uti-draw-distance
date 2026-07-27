import os
import sys
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.DrawDistance.src.utils.response import build_response
from components.DrawDistance.src.models.PackageModel import PackageModel


def _hex_to_bgr(hex_color: str) -> tuple:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return (b, g, r)


class DrawDistance(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image = self.request.get_param("inputImage")
        self.detections = self.request.get_param("inputDetections")
        self.color = _hex_to_bgr(self.request.get_param("configColor") or "#00FF00")
        self.thickness = self.request.get_param("configThickness") or 2
        self.font_scale = self.request.get_param("configFontScale") or 0.5

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def draw(self, image):
        for det in self.detections:
            kps = det.get("keyPoints")
            if not kps or len(kps) < 2:
                continue

            p1 = (int(kps[0]["cx"]), int(kps[0]["cy"]))
            p2 = (int(kps[1]["cx"]), int(kps[1]["cy"]))

            cv2.line(image, p1, p2, self.color, self.thickness)

            distance_cm = det.get("distanceCm")
            if distance_cm is not None:
                mid = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
                label = f"{distance_cm:.2f} cm"
                cv2.putText(
                    image, label, mid,
                    cv2.FONT_HERSHEY_SIMPLEX, self.font_scale,
                    self.color, self.thickness, cv2.LINE_AA,
                )

        return image

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.draw(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        return build_response(context=self)


if __name__ == "__main__":
    Executor(sys.argv[1]).run()
import os
import sys
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.DrawDistance.src.utils.response import build_response
from components.DrawDistance.src.models.PackageModel import PackageModel


def _hex_to_bgr(hex_color: str) -> tuple:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return (b, g, r)


class DrawDistance(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image = self.request.get_param("inputImage")
        self.detections = self.request.get_param("inputDetections")
        self.color = _hex_to_bgr(self.request.get_param("configColor") or "#00FF00")
        self.thickness = self.request.get_param("configThickness") or 2
        self.font_scale = self.request.get_param("configFontScale") or 0.5

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def draw(self, image):
        for det in self.detections:
            kps = det.get("keyPoints")
            if not kps or len(kps) < 2:
                continue

            p1 = (int(kps[0]["cx"]), int(kps[0]["cy"]))
            p2 = (int(kps[1]["cx"]), int(kps[1]["cy"]))

            cv2.line(image, p1, p2, self.color, self.thickness)

            distance_cm = det.get("distanceCm")
            if distance_cm is not None:
                mid = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
                label = f"{distance_cm:.2f} cm"
                cv2.putText(
                    image, label, mid,
                    cv2.FONT_HERSHEY_SIMPLEX, self.font_scale,
                    self.color, self.thickness, cv2.LINE_AA,
                )

        return image

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.draw(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        return build_response(context=self)


if __name__ == "__main__":
    Executor(sys.argv[1]).run()
