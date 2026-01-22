"""
Review model for HBnB Part 3
"""
from app.models.baseclass import BaseModel
from app import db


class Review(BaseModel):
    """Review model representing a user's review of a place"""
    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    def __init__(self, text, rating, place_id, user_id, **kwargs):
        """Initialize a Review instance"""
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
        self.validate()

    def validate(self):
        """Validate review attributes"""
        if not self.text or not self.text.strip():
            raise ValueError("Review text is required")
        if self.rating is None:
            raise ValueError("Rating is required")
        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")

    def to_dict(self):
        """Return dictionary representation of review"""
        data = super().to_dict()
        data.update({
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place_id,
            'user_id': self.user_id
        })
        return data

    def __repr__(self):
        """String representation for debugging"""
        return f"<Review {self.id}: {self.rating}/5 for Place {self.place_id}>"
