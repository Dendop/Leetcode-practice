class Solution:
    def isValid(self, s: str) -> bool:
        save_char = []
       
        bracket_map = {')' : '(', '}' : '{', ']' : '[' }
        
        for i in s:
            if i in bracket_map.values():
                save_char.append(i)
            elif i in bracket_map:
                if save_char and save_char[-1] == bracket_map[i]:
                    save_char.pop()
                else:
                    return False
            else:
                return False
        return len(save_char) == 0