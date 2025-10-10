#!/usr/bin/python3
"""task_03_xml

Serialize a dictionary to XML and deserialize XML to a dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize `dictionary` to `filename` as simple XML.

    The produced XML structure:
    <data>
      <key1>value1</key1>
      <key2>value2</key2>
    </data>
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        # keys must be valid tag names; here we assume input keys are safe strings
        child = ET.SubElement(root, str(key))
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Read `filename` XML and reconstruct a dictionary.

    Returns the dict on success, or None on error.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except Exception:
        return None
