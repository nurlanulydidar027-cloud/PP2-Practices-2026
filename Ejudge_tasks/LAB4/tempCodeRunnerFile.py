def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input().strip())
        print(",".join(map(str, even_generator(n))))

    except ValueError:
        pass
if __name__== "__main__":
    main()