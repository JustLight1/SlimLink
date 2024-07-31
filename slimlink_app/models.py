from datetime import datetime, timezone

from flask import url_for

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True,
                          default=datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'url': self.original,
            'short_link': url_for('redirect_to_original',
                                  short_id=self.short, _external=True),
        }
