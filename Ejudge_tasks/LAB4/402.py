def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    try:
        n = int(input().strip())
        print(",".join(map(str, even_generator(n))))

    except ValueError:
        pass
if __name__== "__main__":
    main()