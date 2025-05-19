import time


start = time.time()
count = 100_000_000

while count:
    
    count -= 1
 
print(f"Python : {count}")   
end = time.time()
print(f"Python: Took {end - start:.4f} seconds")


