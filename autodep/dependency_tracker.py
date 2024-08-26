import os
import argparse

def scan_for_dependencies(directory='.'):
    dependencies = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file)) as f:
                    for line in f:
                        if line.startswith('import') or line.startswith('from'):
                            dependencies.add(line.strip().split()[1])
    return dependencies

def generate_requirements_file(dependencies, output_path='requirements.txt'):
    with open(output_path, 'w') as f:
        for dep in dependencies:
            f.write(f"{dep}\n")
    print(f"Requirements file generated successfully at {output_path}.")

def main():
    parser = argparse.ArgumentParser(description="AutoDep - Automatically scan your Python project for dependencies and generate a requirements.txt file.")
    parser.add_argument('--dir', type=str, default='.', help='Directory to scan for dependencies (default: current directory).')
    parser.add_argument('--output', type=str, default='requirements.txt', help='Path to save the generated requirements.txt file (default: requirements.txt).')
    args = parser.parse_args()

    dependencies = scan_for_dependencies(args.dir)
    generate_requirements_file(dependencies, args.output)

if __name__ == "__main__":
    main()
