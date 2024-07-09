class Context:
    def __enter__(self):
        print("Enter the block")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        if exc_type:
            print(f"Error {exc_val}")
        return  False

with Context() as file:
    print("Inside the block")
    raise Exception("something wrong")
