import base64
import os
import uuid
from datetime import datetime

from autogluon.multimodal import MultiModalPredictor
from pydantic.types import UUID, List

from app.core.models.entities.Detection import Detection
from app.core.usecases.image import crud_usecase as image_crud_usecase
from app.outer.interfaces.controllers.requests.detection_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.detection_controller.patch_one_request import PatchOneRequest
from app.outer.repositories import detection_repository


def read_all() -> List[Detection]:
    return detection_repository.read_all()


def read_one_by_id(id: UUID) -> Detection:
    return detection_repository.read_one_by_id(id)


def create_one(request: CreateOneRequest) -> Detection:
    entity = Detection()
    entity.id = uuid.uuid4()
    entity.image_id = request.image_id
    entity.updated_at = datetime.now()
    entity.created_at = datetime.now()

    file_path = f"{os.getcwd()}\\app\\core\\usecases\\detection\\image_temp\\{str(entity.image_id)}"
    with open(file_path, "wb") as file:
        image = image_crud_usecase.read_one_by_id(entity.image_id)
        decoded_image_file = base64.urlsafe_b64decode(image.file)
        file.write(decoded_image_file)

        predictor = MultiModalPredictor(label="label").load(path="autogluon_models/ag-20221215_054846")
        prediction_probability = predictor.predict_proba({'image': [file_path]}, as_pandas=True)
        entity.result = prediction_probability.to_json(orient="records")

        file.close()
        os.remove(file_path)

    created_entity = detection_repository.create_one(entity)
    return created_entity


def create_many(requests: List[CreateOneRequest]) -> List[Detection]:
    file_paths = []
    entities = []
    for request in requests:
        entity = Detection()
        entity.id = uuid.uuid4()
        entity.image_id = request.image_id
        entity.updated_at = datetime.now()
        entity.created_at = datetime.now()
        entities.append(entity)

        file_path = f"{os.getcwd()}\\app\\core\\usecases\\detection\\image_temp\\{str(request.image_id)}"
        file_paths.append(file_path)
        with open(file_path, "wb") as file:
            image = image_crud_usecase.read_one_by_id(request.image_id)
            decoded_image_file = base64.urlsafe_b64decode(image.file)
            file.write(decoded_image_file)
            file.close()

    predictor = MultiModalPredictor(label="label").load(path="autogluon_models/ag-20221215_054846")
    prediction_probability = predictor.predict_proba({'image': file_paths}, as_pandas=True)

    os.remove(file.name)
    created_entities = []
    for index, value in enumerate(zip(entities, file_paths)):
        entity, file_path = value
        entity.result = prediction_probability[index].to_json(orient="records")
        created_entity = detection_repository.create_one(entity)
        created_entities.append(created_entity)

    return created_entities


def patch_one_by_id(id, request: PatchOneRequest) -> Detection:
    entity = detection_repository.read_one_by_id(id)
    entity.image_id = request.image_id
    entity.result = request.result
    entity.updated_at = datetime.now()
    return detection_repository.patch_one_by_id(id, entity)


def delete_one_by_id(id) -> Detection:
    return detection_repository.delete_one_by_id(id)
