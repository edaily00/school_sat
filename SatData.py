import json


class SatData:

    def __init__(self):
        self._everything = []
        self._line = ['DBN', 'School Name', 'Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean', 'Writing Mean']

        with open("sat.json", "r") as infile:
            self._everything = json.load(infile)

    def save_as_csv(self, database_nums):
        with open('results.csv', 'w') as outfile:
            outfile.write(','.join(self._line))
            self._line.clear()
            outfile.write("\n")
            for data in self._everything["data"]:
                for i in range(len(database_nums)):
                    if data[8].lower() == database_nums[i].lower():

                        for j in range(8, len(data)):
                            if j == 9:
                                if ',' in data[j]:
                                    self._line.append('"' + data[j] + '"')
                                else:
                                    self._line.append(data[j])
                            else:
                                self._line.append(data[j])

                        outfile.write(','.join(self._line))
                        self._line.clear()
                        outfile.write("\n")






#dbns = ["02M303", "02M294", "01M450", "02M418", "01m539"]


#thing = SatData()
#thing.save_as_csv(dbns)
