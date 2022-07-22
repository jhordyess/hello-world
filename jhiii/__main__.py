import os, argparse
from .funcmodule import valid_url


def main():
    parser = argparse.ArgumentParser(description="CLI app for 3 tasks for pandoc")
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="Command, markdown path or url"
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=str,
        choices=["help", "md"],
        default="help",
        required=True,
        help="Choose between help or md",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=False,
        default="aux",
        help="Output filename",
    )
    parser.add_argument("-im", "--image", type=str, required=False, help="Docker image")
    args = parser.parse_args()
    command = "pwd"
    if args.mode == "help":
        if args.image == None:
            # apt-get update && apt-get install help2man -y
            command = 'bash -c "help2man {command} > {file_name}.txt"'.format(
                command=args.input, file_name=args.output
            )
            state = os.system(command)
        else:
            command = 'docker run --rm --volume "`pwd`:/data" --user 0:0 {image} bash -c "apt-get update && apt-get install help2man -y && help2man {command} > /data/{file_name}.txt"'.format(
                image=args.image, command=args.input, file_name=args.output
            )
            state = os.system(command)
        command = 'docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` pandoc/latex -f man {file_name}.txt -o {file_name}.pdf'.format(
            file_name=args.output
        )
    elif args.mode == "md":
        if valid_url(args.input) == True:
            state = os.system(
                "wget -O {file_name}.md -q {url}".format(
                    url=args.input, file_name=args.output
                )
            )
            args.input = "{}.md".format(args.output)
        command = 'docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` pandoc/latex -f markdown {path_url} -o {file_name}.pdf'.format(
            path_url=args.input, file_name=args.output
        )
    state = os.system(command)


if __name__ == "__main__":
    main()
