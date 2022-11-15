def dec(fun):
    def obertka():
        print('паап')
        fun()
    return obertka

def main():
    print('basic')

main = dec(main)
main()