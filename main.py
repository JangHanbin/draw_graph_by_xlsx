import matplotlib.pyplot as plt
from openpyxl import Workbook, load_workbook


class ExcelReader:
    def __init__(self, file_name):
        self.name = file_name

    def read_from_file(self):
        document = load_workbook(self.name, data_only=True)
        sheet = document['Sheet1']

        all_values = list()
        for row in sheet.rows:
            row_value = list()
            for cell in row:
                row_value.append(cell.value)
            all_values.append(row_value)

        return all_values.copy()

if __name__=='__main__':
    excelReader = ExcelReader('propagation.xlsx')

    results = excelReader.read_from_file()
    secs = list()
    eachs = list()
    accumulateds = list()

    # [sec, each, accumulated]
    for result in results:
        for sec, each, accumulated in zip(result[0::3], result[1::3], result[2::3]):
            secs.append(sec)
            eachs.append(each)
            accumulateds.append(accumulated)


    plt.grid()
    # plt.xlim( )
    plt.xticks(range(1,11))
    plt.bar(secs, accumulateds,width=0.2)
    print(secs)
    print(accumulateds)

    plt.xlabel('Time')
    plt.ylabel('Accumulate Propagation')
    plt.show()