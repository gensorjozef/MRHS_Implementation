class LoadFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_from_file(self):
        print(self.file_name)

        fileObj = open(self.file_name, "r")  # opens the file in read mode
        words = fileObj.read().splitlines()  # puts the file into an array
        fileObj.close()
        rowsNumber = int(words[0])
        blocksNumber = int(words[1])
        blocksLen = []
        blocksAnswersLen = []
        for i in range(blocksNumber):
            blockRaw = words[i+2]
            blockInfo = blockRaw.split(' ')
            #print(blockInfo)
            blockLen = blockInfo[0]
            blockAnswers = blockInfo[1]
            blocksLen.append(blockLen)
            blocksAnswersLen.append(blockAnswers)
        matrix = []
        for i in range(rowsNumber):
            rowRaw = words[2+blocksNumber+i]
            rowRaw = rowRaw[1:len(rowRaw)-1] # odstrani []
            rowBlocks = rowRaw.split('  ')
            rows = []
            for rowBlock in rowBlocks:
                cols = []
                for col in rowBlock:
                    if(col != ' '):
                        cols.append(int(col))
                rows.append(cols)
            matrix.append(rows)
        sum = 2+blocksNumber+rowsNumber
        rhs = []
        for i in range(blocksNumber):
            number = int(blocksAnswersLen[i])
            rows = []
            for j in range(number):
                rowRaw = words[sum+j]
                row = rowRaw[1:len(rowRaw)-1]
                cols = []
                for col in row:
                    if (col != ' '):
                        cols.append(int(col))
                rows.append(cols)

            rhs.append(rows)
            sum+=number+1
        print(rhs)


        print(matrix)

    pass