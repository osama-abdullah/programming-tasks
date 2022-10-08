def search(board, word):

    if not word:    # return true if word is empty
        return True
      
    if not board:   # return false if board is empty
        return False
    
    row_no, col_no, word_len = len(board), len(board[0]), len(word) - 1
    # i meaning row, j meaning column, and  k is the character index of the 'word' 
    
     
    # check the entire board, cell by cell as the starting point. 
    # the value of k is zero means we will start from the first 'word' character  
    
    for i in range(row_no):
        for j in range(col_no):
            print(i,j)
    # here, no matched from any coordination point in the 'board', return False
    return False