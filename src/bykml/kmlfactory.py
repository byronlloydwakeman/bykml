import xmltodict


def placemark_template(placemark_name, description, longitude, latitude, altitude, color="FF00FEB7"):
    return {
        "name": placemark_name,
        "open": 1,
        "Placemark": {
            "name": placemark_name,
            "description": description,
            "Style": {
                "IconStyle": {
                    "color": color
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
        :return:
        """
        self.kml_dict["kml"]["Document"]["Folder"].append(dict_element)