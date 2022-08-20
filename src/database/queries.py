from src import db
from src.database import models
from sqlalchemy import and_

# films = db.session.query(models.Film).all()
# films = db.session.query(models.Film).order_by(models.Film.rating).all()
# films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
# film = db.session.query(models.Film).filter(
#     models.Film.title == 'Harry Potter and Chamber of Secrets'
# ).first()
# film = db.session.query(models.Film).filter_by(
#     title='Harry Potter and the Prizoner of Azkaban'
# ).first()
# films = db.session.query(models.Film).filter(
#     models.Film.title != 'Harry Potter and Chamber of Secrets',
#     models.Film.rating >= 7.5
# ).all()
# films = db.session.query(models.Film).filter(
#     models.Film.title != 'Harry Potter and Chamber of Secrets'
# ).filter(models.Film.rating >= 7.5).all()
# films = db.session.query(models.Film).filter(
#     and_(
#         models.Film.title != 'Harry Potter and Chamber of Secrets',
#         models.Film.rating >= 8.0
#     )
# ).all()
# films = db.session.query(models.Film).filter(
#     models.Film.title.like('%Deathly Hallows%')
# ).all()
# films = db.session.query(models.Film).filter(
#     models.Film.title.ilike('%deathly HALLOWS%')
# ).all()
# films = db.session.query(models.Film).filter(
#     models.Film.length.in_([146, 161])
# ).all()
# films = db.session.query(models.Film).filter(
#     ~models.Film.length.in_([146, 161])
# ).all()
# films = db.session.query(models.Film).filter(
#     ~models.Film.length.in_([146, 161])
# )[:2]
films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
print(films_with_actors)