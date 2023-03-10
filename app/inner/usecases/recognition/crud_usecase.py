import base64
import os
import uuid
from datetime import datetime

from autogluon.multimodal import MultiModalPredictor
from pydantic.types import UUID, List

from app.inner.models.entities.Recognition import Recognition
from app.inner.usecases.image import crud_usecase as image_crud_usecase
from app.outer.interfaces.controllers.requests.recognition_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.recognition_controller.patch_one_request import PatchOneRequest
from app.outer.repositories import recognition_repository


def fix_path(path):
    return os.path.abspath(os.path.expanduser(path))


def read_all() -> List[Recognition]:
    return recognition_repository.read_all()


def read_one_by_id(id: UUID) -> Recognition:
    return recognition_repository.read_one_by_id(id)


def create_one(request: CreateOneRequest) -> Recognition:
    entity = Recognition()
    entity.id = uuid.uuid4()
    entity.image_id = request.image_id
    entity.updated_at = datetime.now()
    entity.created_at = datetime.now()

    current_path = fix_path(f"{os.getcwd()}/app/inner/usecases/recognition")
    file_path = fix_path(f"{current_path}/image_temp/{str(entity.image_id)}")
    with open(file_path, "wb") as file:
        image = image_crud_usecase.read_one_by_id(entity.image_id)
        decoded_image_file = base64.urlsafe_b64decode(image.file)
        file.write(decoded_image_file)

        predictor = MultiModalPredictor(
            label="label"
        ).load(
            path=fix_path(f"{current_path}/autogluon_models/ag-20221215_054846")
        )
        prediction_probability = predictor.predict_proba({'image': [file_path]}, as_pandas=True)
        entity.result = prediction_probability.to_json(orient="records")

        file.close()
        if os.path.exists(file_path):
            os.remove(file_path)

    created_entity = recognition_repository.create_one(entity)
    return created_entity


def create_many(request: List[CreateOneRequest]) -> List[Recognition]:
    file_paths = []
    entities = []
    current_path = fix_path(f"{os.getcwd()}/app/inner/usecases/recognition")
    for one_request in request:
        entity = Recognition()
        entity.id = uuid.uuid4()
        entity.image_id = one_request.image_id
        entity.updated_at = datetime.now()
        entity.created_at = datetime.now()
        entities.append(entity)

        file_path = fix_path(f"{current_path}/image_temp/{str(one_request.image_id)}")
        file_paths.append(file_path)
        with open(file_path, "wb") as file:
            image = image_crud_usecase.read_one_by_id(one_request.image_id)
            decoded_image_file = base64.urlsafe_b64decode(image.file)
            file.write(decoded_image_file)
            file.close()

    predictor = MultiModalPredictor(
        label="label"
    ).load(
        path=fix_path(f"{current_path}/autogluon_models/ag-20221215_054846")
    )
    prediction_probability = predictor.predict_proba({'image': file_paths}, as_pandas=True)

    created_entities = []
    for index, value in enumerate(zip(entities, file_paths)):
        entity, file_path = value
        entity.result = prediction_probability.iloc[[index], :].to_json(orient="records")
        created_entity = recognition_repository.create_one(entity)
        created_entities.append(created_entity)

        if os.path.exists(file_path):
            os.remove(file_path)

    return created_entities


def patch_one_by_id(id, request: PatchOneRequest) -> Recognition:
    entity = recognition_repository.read_one_by_id(id)
    entity.image_id = request.image_id
    entity.result = request.result
    entity.updated_at = datetime.now()
    return recognition_repository.patch_one_by_id(id, entity)


def delete_one_by_id(id) -> Recognition:
    return recognition_repository.delete_one_by_id(id)
