def search(board, word):

    if not word:    # return true if word is empty
        return True
      
    if not board:   # return false if board is empty
        return False
    
    row_no, col_no, word_len = len(board), len(board[0]), len(word) - 1
    # i meaning row, j meaning column, and  k is the character index of the 'word' 
    
    def dfs(i, j, k):
    
        # go back if it reach the edges of the 'board' or the cell already visited or the cell does not equal to the current 'word' character
  
        if (i < 0 or i >= row_no or j < 0 or j >= col_no) or board[i][j] == '#' or board[i][j] != word[k]:    
            return False

        # here it means the cell equal to the current  'word' character. 
        # just check if it was the last character in the 'word'. 
        # if so, we are done: the 'word' matches completely, so return True
    
        if k == word_len:
            return True
                
        # if still not the last character then...
        # save the cell in case we need to backtrack later.  mark the cell as '#' (meaning visited)
        tmp = board[i][j] 
        board[i][j] = '#'
        # here all charcters to the kth index  matched up to board then ...
        # move the pointer one step forward to the next 'word' character
        k += 1
        
        # the next for clause: continue with up, down, left and right of the current cell: 
        # as soon as a match is found out, happily return true (meaning from that point on to the end of 'word', 
        # everything was matched up (due to the dfs)
    
        for x, y in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
            if dfs(i + x, j + y, k):
                return True
        
        #here, meaning none of 4 potential paths (inside the for clause above) got matched up to the end. 
        # meaning the current cell is not a good candidate, 
        # so return it back to its original value 'tmp', then return False
        
        board[i][j] = tmp
        return False
     
    # check the entire board, cell by cell as the starting point. 
    # the value of k is zero means we will start from the first 'word' character  
    
    for i in range(row_no):
        for j in range(col_no):
            if dfs(i, j, 0):
                return True
    # here, no matched from any coordination point in the 'board', return False
    return False