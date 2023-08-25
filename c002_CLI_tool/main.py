#! /usr/bin/python3
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="New CLI program")
    parser.add_argument('message', help='Message to echo.')  # positional arg

    parser.add_argument('--twice', '-t',  # - or -- means the args are optional (всё до help будет относиться к одному аргументу)
                        help="Do it twice.",  
                        action='store_true'  # make it boolean                        
                        )

    args = parser.parse_args()
    print(args.message)
    if args.t:
        print(args.message)

