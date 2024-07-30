from datetime import datetime, timezone

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Colum(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True,
                          default=datetime.now(timezone.utc))

    def to_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp
        )

    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
