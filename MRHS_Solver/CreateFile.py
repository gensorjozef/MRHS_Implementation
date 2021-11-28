class CreateFile:
    def __init__(self, mrhs):
        self.rowsNumber = len(mrhs.block_array[0].matrix)
        self.blocksNumber = len(mrhs.block_array)
        self.rows = []
        self.blockMatrix = []
        self.rhsMatrices = []
        for block in mrhs.block_array:
            rhs = len(block.rhsMatrix.matrix)
            col_number = len(block.matrix[0])
            self.rows.append([col_number, rhs])
            self.rhsMatrices.append(block.rhsMatrix.matrix)

        for row_id in range(self.rowsNumber):
            row_array = []
            for block in mrhs.block_array:
                row_array.append(block.matrix[row_id])
            self.blockMatrix.append(row_array)



    def create_file(self, file_name):
        file = open(file_name, 'w')
        file.write(str(self.rowsNumber) + '\n')
        file.write(str(self.blocksNumber) + '\n')
        for row in self.rows:
            file.write(str(row[0]) + ' ' + str(row[1]) + '\n')

        for row_array in self.blockMatrix:
            file.write('[{0}]'.format(str(row_array).replace('[', ' ').replace(']', '').replace(',', '')[2:]) + '\n')

        for rhs_matrix in self.rhsMatrices:
            for rhs_row in rhs_matrix:
                file.write(str(rhs_row).replace(',', '') + '\n')
            file.write('\n')

        file.close()
