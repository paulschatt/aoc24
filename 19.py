def main(filename:str):
    def is_possible(design:str):
        n = len(design)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if design[j:i] in patterns and dp[j] == True:
                    dp[i] = True
                    break
        return dp[-1]
    
    #GET PATTERNS AND DESIGNS
    patterns = set()
    designs = []
    counter = 0
    with open(filename, 'r') as file:
        lines = file.read()
        patterns_in_file,designs_in_file = lines.split("\n\n")

        for pattern in patterns_in_file.split(','):
            if pattern:
                patterns.add(pattern.strip())

        for design in designs_in_file.split('\n'):
            designs.append(design)

    #CHECK HOW MANY DESIGNS POSSIBLE WITH GIVEN PATTERNS
    for design in designs:
        if is_possible(design):
            counter += 1
    
    print(counter)
    

main('input.txt')
