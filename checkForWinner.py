class CheckForWinner():
    
    def search(self,grid:list[list[int]]):
        for y in range(6):
            for x in range(7):
                if grid[y][x] != 0:
                    if self.check_horizontal(grid,x,y) or self.check_vertical(grid,x,y) or self.check_diagonal(grid,x,y):
                        return True
        return False
    
    def check_horizontal(self,grid:list[list[int]],x:int,y:int):
        """
        If they are 4 element that has the same value in the same row
        :param grid: the matrice of the game
        :param x: the position at column
        :param y: the position at row
        :return: a boolean if they are 4 element that has the same value.
        """
        if x < 4 and grid[y][x] == grid[y][x+1] == grid[y][x+2] == grid[y][x+3]:
                return True
        return False
    
    def check_vertical(self,grid:list[list[int]],x:int,y:int):
        """"
        if they are 4 element that has the same value in the same column
        :param grid: the matrice of the game
        :param x: the position at column
        :param y: the position at row
        :return: a boolean if they are 4 element verticaly that has the same value.
        """
        if y < 3 and grid[y][x] == grid[y+1][x] == grid[y+2][x] == grid[y+3][x]:
                return True
        return False
    
    def check_diagonal(self, grid:list[list[int]], x:int, y:int):
        """"
        test if they are 4 element diagonally
        :param grid: the matrice of the game
        :param x: the position at column
        :param y: the position at row
        :return: a boolean if they are 4 element diagonally that has the same value.
        """
        if y < 3 and (x < 4 and grid[y][x] == grid[y+1][x+1] == grid[y+2][x+2] == grid[y+3][x+3] or x > 2 and grid[y][x] == grid[y+1][x-1] == grid[y+2][x-2] == grid[y+3][x-3]):
            return True
        return False
