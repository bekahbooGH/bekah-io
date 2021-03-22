"""CRUD operations."""

from model import db, Project, connect_to_db


def create_project(name, date, topic):
    """Create and return a new project."""

    project = Project(
                name=name, 
                date=date, 
                topic=topic, 
                )
    db.session.add(project)
    db.session.commit()
    return project


if __name__ == '__main__':
    from server import app
    connect_to_db(app)