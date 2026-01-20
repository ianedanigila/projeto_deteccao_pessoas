from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2

cfg = get_cfg()

cfg.merge_from_file(
    model_zoo.get_config_file(
        "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
    )
)

cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
cfg.MODEL.WEIGHTS = "/content/output/model_final.pth"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.2
cfg.MODEL.DEVICE = "cuda"

predictor = DefaultPredictor(cfg)

img_path = "/content/train/Captura-de-tela-2026-01-18-180600_png.rf.528912db756aa5497fd0f77585130d89.jpg"
im = cv2.imread(img_path)

outputs = predictor(im)

print(outputs["instances"])

v = Visualizer(
    im[:, :, ::-1],
    MetadataCatalog.get("pessoas_train"),
    scale=1.2
)

out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])



