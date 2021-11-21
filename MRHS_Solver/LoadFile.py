class LoadFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.position = 0
        fileObj = open(self.file_name, "r")
        self.words = fileObj.read().splitlines()
        fileObj.close()
        self.rowsNumber = int(self.words[0])
        self.blocksNumber = int(self.words[1])
        self.blocksAnswersLen = []
        self.matrix = self.get_matrix()
        self.rhs = self.get_rhs()

    def get_matrix(self):
        blocksLen = []
        for i in range(self.blocksNumber):
            blockRaw = self.words[i + 2]
            blockInfo = blockRaw.split(' ')
            blockLen = blockInfo[0]
            blockAnswers = blockInfo[1]
            blocksLen.append(blockLen)
            self.blocksAnswersLen.append(blockAnswers)
        matrix = []
        for i in range(self.rowsNumber):
            rowRaw = self.words[2 + self.blocksNumber + i]
            rowRaw = rowRaw[1:len(rowRaw) - 1]  # odstrani []
            rowBlocks = rowRaw.split('  ')
            rows = []
            for rowBlock in rowBlocks:
                cols = []
                for col in rowBlock:
                    if col != ' ':
                        cols.append(int(col))
                rows.append(cols)
            matrix.append(rows)
        return matrix

    def get_rhs(self):
        sum = 2 + self.blocksNumber + self.rowsNumber
        rhs = []
        for i in range(self.blocksNumber):
            number = int(self.blocksAnswersLen[i])
            rows = []
            for j in range(number):
                rowRaw = self.words[sum + j]
                row = rowRaw[1:len(rowRaw) - 1]
                cols = []
                for col in row:
                    if col != ' ':
                        cols.append(int(col))
                rows.append(cols)

            rhs.append(rows)
            sum += number + 1
        return rhs

    def get_final_matrix(self):
        final_matrix, block, block_main, block_rhs = [], [], [], []
        for i in range(self.blocksNumber):
            for row_main in self.matrix:
                block_main.append(row_main[i])
            for row_rhs in self.rhs[i]:
                block_rhs.append(row_rhs)
            block.append(block_main)
            block.append(block_rhs)
            final_matrix.append(block)
            block, block_main, block_rhs = [], [], []
        return final_matrix