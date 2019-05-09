import xlrd,xlwt
from xlutils.copy import copy
class OperationExcel:
    def __init__(self,file_path=None,sheet_id=None):
        if file_path:
            self.file_name=file_path
            self.sheet_id=sheet_id
        else:
            self.file_name='../data_config/Excel_data.xls'
            self.sheet_id=0
        self.data=self.get_data()
    def get_data(self):
        """打开文件,通过索引获取表格数据"""
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheet_by_index(self.sheet_id)
        # tables=data.get_sheets()[self.sheet_id]
        # tables=data.sheet_by_name()
        return tables
    def get_lines(self):
        """获取Excel行数"""
        return self.data.nrows
    def get_cell_value(self,row,col):
        """获取某个单元格内容"""
        return self.data.cell_value(row,col)
    def write_value(self,row,col,value):
        """写入数据"""
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)
        return value
    def get_cols_data(self,col_id=None):
        """获取某一列的数据"""
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols
    def get_row_num(self,case_id):
        """根据对应的caseid找到对应的行号"""
        num=0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num=num+1
    def get_row_values(self, row):
        """根据行号,获取某一行的数据"""
        tables = self.data
        row_data = tables.row_values(row)
        return row_data
    def get_rows_data(self,case_id):
        """根据对应的caseid 找到对应行的内容"""
        row_num = self.get_row_num(case_id)
        rows_data=self.get_row_values(row_num)
        return rows_data
if __name__ == '__main__':
    opers = OperationExcel()
    # print('获取Excel行数为:{}'.format(opers.get_lines()))
    # print('获取Excel某个单元格数据为:{}'.format(opers.get_cell_value(0,2)))
    # print('写入数据为:{}'.format(opers.write_value(7,4,'写入数据')))
    # print('获取某一列的数据为:{}'.format(opers.get_cols_data(0)))
    # print('获取某一行数据为:{}'.format(opers.get_row_values(2)))
    # print('根据对应的caseid找到对应的行号为:{}'.format(opers.get_row_num('test002')))
    # print('根据对应的caseid 找到对应行的内容为:{}'.format(opers.get_rows_data('test002')))