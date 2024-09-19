import time
def time_ticking(func):
    def wrapper():
        t1 = time.time()
        result = func()
        t2 = time.time() - t1
        print(f"Took {t2} seconds")
        return result
    return wrapper

@time_ticking
def say_hi():
    time.sleep(2)
    return "hello there"
    



def main():
    result = say_hi()
    print(result)
    

if __name__ == "__main__":
    main()