#!/usr/bin/python3
"""
Application Factory for HBnB Part 2
"""
from flask import Flask
from flask_restx import Api

from app.config import Config


def create_app(config_class=Config):
    """
    Create and configure the Flask application
    
    Args:
        config_class: Configuration class to use
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize API
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB API Documentation',
        doc='/api/v1/'
    )
    
    # Register blueprints/namespaces here
    # from app.api.v1 import users, places, reviews, amenities
    # api.add_namespace(users.ns)
    # api.add_namespace(places.ns)
    # api.add_namespace(reviews.ns)
    # api.add_namespace(amenities.ns)
    
    return app



