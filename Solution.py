#!/bin/python3

def fillGrid(grid, words, index):
    #This is the function to fill the words in the given grid.
    # Here, parameter grid is the grid to be filled;
    # parameter words is the list of words;
    # parameter index shows the index of current word.		
    

    # The updated grid after one recursion
    updatedGrid = []
    
    if index < len(words):
        # We have more words to be filled.
        word = words[index];
        
        # Fill the current word in the grid by column
        for col in range(DIM):
            for row in range(DIM - len(word) + 1):
                updatedGrid = fillByColumn(grid, word, row, col) 
                if updatedGrid is not None:	
                    # This current column can match this word
                    fillGrid(updatedGrid, words, index + 1)
		
        # Fill the current word in the grid by row
        for row in range(DIM):
            for col in range(DIM - len(word) + 1):
                updatedGrid = fillByRow(grid, word, row, col)
                if updatedGrid is not None:
                    # row can match this word
                    fillGrid(updatedGrid, words, index + 1);	 
    else:
        # All words have been filled, and then we show the result.
        for row in grid:
            print(row)	


def fillByRow(grid, word, row, col):
    # This is the function to fill a specific word by rows.
    # Here, parameter grid is the grid to be filled;
    # parameter word is the current words;
    # parameter row shows the index of the row in the grid;
    # parameter col shows the index of the column in the grid.
    
    for idx in range(len(word)): 
        if grid[row][col + idx] == NEGATIVE or grid[row][col + idx] == word[idx]: 
            continue
        else: 
            # If this row is not suitable, return null 
            return None
    
    idx += 1
		
    if (col + idx < DIM and grid[row][col + idx] != POSITIVE) or (col > 0 and grid[row][col - 1] == NEGATIVE):
        # This current row is too broad. 
        return None
    else:
        # If this row is suitable, replace and return
       grid[row] = grid[row].replace(grid[row][col: col + len(word)], word)        
       return grid
	
	
def fillByColumn(grid, word, row, col):
    # Fill a specific word by columns.
    # Here, parameter grid is the grid to be filled;
    # parameter word is the current words;
    # parameter row shows the index of the row in the grid;
    # parameter col shows the index of the column in the grid.
        
    for idx in range(len(word)):
        if grid[row + idx][col] == NEGATIVE or grid[row + idx][col] == word[idx]:
            # If the current entry of grid can be filled or already be filled by the match letter, continue to check next one
            continue
        else:
            # If this column is not suitable, return null 
            return None
    
    idx += 1
    
    if (row + idx < DIM and grid[row + idx][col] != POSITIVE) or (row > 0 and grid[row - 1][col] == NEGATIVE):
        # This column is too broad.
        return None
    else:
        
        for idx in range(len(word)):
            ## If this column is suitable, replace and return
            line = list(grid[row + idx])
            line[col] = word[idx]
            grid[row + idx] = ''.join(line)
        return grid
    

if __name__ == '__main__':
    # The dimension of the grid
    DIM = 10
    
    # The constant of positive char "+"
    POSITIVE = '+'
    
    # The constant of negative char "-"
    NEGATIVE = '-'
    
    # The index to show how many words have been filled
    index = 0
    
    # The grid to hold the words
    grid = []
    
    # Enter the rows of the grid
    for idx in range(DIM):
        grid.append(input('Please enter the row {row} of the input grid: '
                        .format(row = idx + 1)))
        
    # Enter the list of words separated by semi-colons (;)
    words = input('Please enter the words: ')
    words = words.split(";")

    fillGrid(grid, words, index)