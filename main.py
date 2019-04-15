import matplotlib.pyplot as plt
from openpyxl import Workbook, load_workbook
from matplotlib.pyplot import figure
figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')

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
    plt.xticks(range(-1,11),fontsize=15)

    plt.yticks(fontsize=15)

    plt.plot(secs,[accumulated /100 for accumulated in accumulateds], c='#C80000', linewidth=3.0)
    # plt.bar(secs, accumulateds)
    plt.xlabel('Elapsed time (seconds)',fontsize=20)
    plt.ylabel('Cumulative distribution function',fontsize=20)
    plt.savefig('propagation.eps', format='eps', dpi=1000)
    plt.show()