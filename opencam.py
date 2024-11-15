import os
import cv2
import numpy as np
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util

# Define paths relative to the current working directory
base_path = os.getcwd()
CUSTOM_MODEL_NAME = 'my_ssd_mobnet_tunedv3'

paths = {
    'CHECKPOINT_PATH': os.path.join(base_path, 'Tensorflow', 'workspace', 'models', CUSTOM_MODEL_NAME),
    'LABELMAP': os.path.join(base_path, 'Tensorflow', 'workspace', 'annotations', 'label_map.pbtxt')
}

configs = config_util.get_configs_from_pipeline_file(os.path.join(paths['CHECKPOINT_PATH'], 'pipeline.config'))
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(paths['CHECKPOINT_PATH'], 'ckpt-21')).expect_partial()

@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

category_index = label_map_util.create_category_index_from_labelmap(paths['LABELMAP'])

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    image_np = np.array(frame)
    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections = detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    label_id_offset = 1
    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np,
        detections['detection_boxes'],
        detections['detection_classes'] + label_id_offset,
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=5,
        min_score_thresh=.8,
        agnostic_mode=False
    )

    cv2.imshow('Live Feed! Press "Q" to exit', cv2.resize(image_np, (800, 600)))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
