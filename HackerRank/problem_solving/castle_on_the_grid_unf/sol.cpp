    // I messed up and didn't read the directions.
    // The below code can be slightly modified with an ascii-level
    // system to satisfy the problem optimally.
    int sizeY = grid.size();
    int sizeX = grid[0].size();
    cout << sizeY << endl;
    cout << sizeX << endl;
    // need to do BFS
    deque<pair<int, int>> queue;
    queue.push_back({startX, startY});
    grid[startY][startX] = '1';
    int curr = 1;
    int next = 0;
    int level = 0;
    pair<int, int> popped;
    while(true){ 
        popped = queue.back();
        queue.pop_back();
        // kinda cheating
        cout << popped.first << ", " << popped.second << endl;
        if(popped.first==goalX && popped.second==goalY){
            return level;
        }
        if(popped.first-1 >= 0 && grid[popped.second][popped.first-1] == '.'){
            next++;
            queue.push_front({popped.first-1, popped.second});
            grid[popped.second][popped.first-1] = '1';
        }
        if(popped.first+1 < sizeX && grid[popped.second][popped.first+1] == '.'){
            next++;
            queue.push_front({popped.first+1, popped.second});
            grid[popped.second][popped.first+1] = '1';
        }
        if(popped.second+1 < sizeY && grid[popped.second+1][popped.first] == '.'){
            next++;
            queue.push_front({popped.first, popped.second+1});
            grid[popped.second+1][popped.first] = '1';
        }
        if(popped.second-1 >=0 && grid[popped.second-1][popped.first] == '.'){
            next++;
            queue.push_front({popped.first, popped.second-1});
            grid[popped.second-1][popped.first] = '1';
        }
        curr--;
        if(curr==0){
            curr = next;
            next = 0;
            level++;
        }        
        for(const auto &e: grid){
            cout << e << endl;
        }
    }
    return -1;
