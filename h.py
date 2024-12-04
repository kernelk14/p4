class HelloWorld:
    def greet(*names):
        for name in names:
            print(f"Hello {name}!")

# HelloWorld.greet("pakyu", "jouram", "maitim", "isa", "kang","n_")



class Check:
    def board(count):
        for j in range(count):
            for i in range(count):
                print("# ", end="")
            print(" #")


Check.board(5)      