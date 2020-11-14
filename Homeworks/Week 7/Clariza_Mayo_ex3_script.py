def main(args):
    file = open("output.html", "a")
    file.write(f"<body>\n")
    for arg in args:
        file.write(arg)
        file.write(" ")
    file.write(f"\n</body>")
    file.close()
    
if __name__== "__main__":
    import sys
    main(sys.argv[1:])
