import xmltodict


def placemark_template(placemark_name, description, longitude, latitude, altitude, icon="", color="FF00FEB7"):
    """
    Placemark template is what will get passed through to the add_element function to be added to the kml document
    :param placemark_name: The name of the placemark that will show up on Google (if empty input "")
    :param description: Description of the placemark that will show when the user clicks on the placemark
    :param longitude: The longitude of the placemark
    :param latitude: The latitude of the placemark
    :param altitude: The altitude of the placemark
    :param icon: Optional parameter of a placemark image, such as http://maps.google.com/mapfiles/kml/shapes/caution.png
    :param color: Color of the placemark as a html color value, default is FF00FEB7
    :return: Dictionary of the placemark
    """
    if icon != "":
        return {
            "name": placemark_name,
            "open": 1,
            "Placemark": {
                "name": placemark_name,
                "description": description,
                "Style": {
                    "IconStyle": {
                        "color": color,
                        "Icon": {
                            "href": icon
                        }
                    }
                },
                "Point": {
                    "coordinates": str(f"{longitude},{latitude},{altitude}")
                }
            }
        }
    else:
        return {
            "name": placemark_name,
            "open": 1,
            "Placemark": {
                "name": placemark_name,
                "description": description,
                "Style": {
                    "IconStyle": {
                        "color": color,
                    }
                },
                "Point": {
                    "coordinates": str(f"{longitude},{latitude},{altitude}")
                }
            }
        }


class KmlFactory:
    def __init__(self, document_name):
        self.kml_dict = {
            "kml": {
                "@xmlns": "http://www.opengis.net/kml/2.2",
                "@xmlns:gx": "http://www.google.com/kml/ext/2.2",
                "@xmlns:kml": "http://www.opengis.net/kml/2.2",
                "@xmlns:atom": "http://www.w3.org/2005/Atom",
                "Document": {
                    "name": document_name,
                    # Style elements here
                    "Folder": [
                        # Add place marks
                    ]
                }
            }
        }

    def save_kml(self, file_name):
        xml_content = xmltodict.unparse(self.kml_dict)
        with open(f"{file_name}.kml", "w") as file:
            file.write(xml_content)

    def add_element(self, dict_element):
        """
        Add an element to the kml document in the form of a dict.
        You can pass through your custom dictionary or use one of the templates in the kmlfactory package.
        :param dict_element:
        :return: None
        """
        self.kml_dict["kml"]["Document"]["Folder"].append(dict_element)