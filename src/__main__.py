# Entry point for the application
import argparse
import os
import sys
import json
from .models import FunctionDefinition, FunctionCall, PromptInput

class ArgumentsError(Exception):
    ...

def arguments_checker(args: argparse.Namespace) -> None:
    if not os.path.exists(args.functions_definition):
        raise ArgumentsError(f"functions definition file {args.functions_definition} does not exist")
    if not os.path.exists(args.input):
        raise ArgumentsError(f"input file {args.input} does not exist")

def main() -> None:
    parser = argparse.ArgumentParser(
                description="function calling tool that translates natural language prompts into structured function calls",
                epilog="Author : abdessel"
            )
    parser.add_argument("--functions_definition",
                        default="data/input/functions_definition.json",
                        help="path to the functions definition file")
    
    parser.add_argument("--input",
                        default="data/input/function_calling_tests.json",
                        help="path to the input file")
    parser.add_argument("--output",
                        default="data/output/function_calls.json",
                        help="path to the output file")
    args = parser.parse_args()
    try:
        arguments_checker(args)
    except ArgumentsError as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        with open(args.functions_definition) as f:
            functions = [FunctionDefinition(**item) for item in json.load(f)]
        
        with open(args.input) as f:
            prompts = [PromptInput(**item) for item in json.load(f)]
    except Exception as e:
        print(f"Error loading files: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
