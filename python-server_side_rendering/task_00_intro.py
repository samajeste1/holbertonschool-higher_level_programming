#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
Function that generates personalized invitation files from a template
"""
import logging
import os

logging.basicConfig(level=logging.ERROR)


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and a list of attendees

    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee data

    Returns:
        None: Creates output files or logs errors
    """
    # Check input types
    if not isinstance(template, str):
        logging.error(f"Invalid input type: template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        logging.error(f"Invalid input type: attendees must be a list, got {type(attendees).__name__}")
        return

    # Check if template is empty
    if not template:
        logging.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            continue

        # Create a copy of the template for each attendee
        processed_template = template[:]

        # Replace placeholders with values from attendee dictionary
        # If value is missing, replace with "N/A"
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A')
        event_date = attendee.get('event_date', 'N/A')
        event_location = attendee.get('event_location', 'N/A')

        # Replace placeholders
        processed_template = processed_template.replace('{name}', str(name))
        processed_template = processed_template.replace('{event_title}', str(event_title))
        processed_template = processed_template.replace('{event_date}', str(event_date))
        processed_template = processed_template.replace('{event_location}', str(event_location))

        # Generate output file
        output_filename = f'output_{index}.txt'
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(processed_template)
        except Exception as e:
            logging.error(f"Error writing file {output_filename}: {e}")

