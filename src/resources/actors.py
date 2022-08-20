from flask_restful import Resource

from src import db
from src.database.models import Actor
from src.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, uuid=None):
        if not uuid:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return '', 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        films = db.session.query(Actor).all()
        for film in films:
            db.session.delete(film)
        db.session.commit()
        return 'Done', 204
