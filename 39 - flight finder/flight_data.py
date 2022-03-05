class FlightData:


    #This class is responsible for structuring the flight data.
    def structure_data(self, data):
        data_structured = [{"dpr": res["data"][0]["cityFrom"] + "-" + res["data"][0]["flyFrom"],
                            "dst": res["data"][0]["cityTo"] + "-" + res["data"][0]["flyTo"],
                            "from": res["data"][0]["route"][0]["local_departure"][8:10] + "-" + res["data"][0]["route"][0]["local_departure"][5:7],
                            "to": res["data"][0]["route"][0]["local_arrival"][8:10] + "-" + res["data"][0]["route"][0]["local_arrival"][5:7],
                            "price": res["data"][0]["price"],
                            "link": res["data"][0]["deep_link"]
                            } for res in data if res["_results"] != 0]
        return data_structured
